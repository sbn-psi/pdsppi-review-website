from django import forms, template
from django.conf import settings
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.admin.panels import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail import blocks
from wagtail.blocks import StructBlock, StructValue, BooleanBlock, FieldBlock, ChoiceBlock, CharBlock 
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from .blocks import InlineImageBlock, ScheduleBlock, schedule_table_options, DataBlock, ReviewerChoiceBlock, InstructionBlock

from django_comments_xtd.models import XtdComment

register = template.Library()

# Create your models here.
class HomePage(Page):
    subpage_types = ['MissionIndexPage']
    max_count = 1
    section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text=("Title to display above this section"),
    )
    mission_review_intro = RichTextField(blank=True)
    mission_section = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=("Featured missions for the homepage"),
        verbose_name=("Point to Section")
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('section_title'),
            FieldPanel('mission_review_intro', classname='full', heading="Review intro"),
            PageChooserPanel('mission_section'),
        ], heading=("Review Index Section"), classname='collapsible'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        missionpages = MissionPage.objects.all()
        context['missionpages'] = missionpages
        return context

# =====================================================================
# Mission Page Setup
# =====================================================================
class MissionPage(Page):
    parent_page_types = ['MissionIndexPage']
    subpage_types = ['MissionDataPage', 'MissionCommentsPage', 'MissionLiensPage']
    image = models.ForeignKey(
        'wagtailimages.Image', blank=True, null=True, on_delete=models.SET_NULL, related_name='+', verbose_name=("Image")
    )
    featured = models.BooleanField(default=False)
    site_layout = RichTextField(features=['h5', 'h6', 'bold', 'italic', 'hr',
                                         'ol', 'ul', 'link', 'document-link', 'image', 'embed'], blank=True)
    scheduling = StreamField([('schedule', ScheduleBlock(
        table_options=schedule_table_options, max_num=2, blank=True))], blank=True)
    instructions = StreamField(
        [('instructions', InstructionBlock())], blank=True)
    categories = ParentalManyToManyField('missions.MissionCategory', blank=True)
    reviewers  = ParentalManyToManyField('missions.Reviewer', blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            FieldPanel('reviewers',  widget=forms.CheckboxSelectMultiple),
            FieldPanel('featured'),
        ],
            heading="Mission information",
            classname="collapsible"
        ),
        MultiFieldPanel([
            FieldPanel('site_layout', classname='full'),
            StreamFieldPanel('scheduling'),
        ],
            heading="Review Information",
            classname="collapsible"
        ),
        MultiFieldPanel([
            StreamFieldPanel('instructions'),
        ],
            heading="Review Instructions",
            classname="collapsible"
        ),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        missionpages = MissionPage.objects.all()
        context['missionpages'] = missionpages
        return context


class MissionIndexPage(Page):
    intro = RichTextField(blank=True)
    # Specifies that only these page objects can live under this index page
    parent_page_types = ['HomePage']
    subpage_types = ['MissionPage']
    max_count = 2

    def missionpages(self):
        return MissionPage.objects.child_of(self).live().order_by('-first_published_at')

    def featured_missionpages(self):
        return self.missionpages().filter(featured=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]


# =====================================================================
# Mission Data Page Setup
# =====================================================================
class MissionDataPage(Page):
    parent_page_types = ['MissionPage']
    subpage_types = []
    data = StreamField(
        [('data', DataBlock())], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            StreamFieldPanel('data'),
        ],
            heading="Review Data",
            classname="collapsible"
        ),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        missionpages = MissionPage.objects.all()
        context['missionpages'] = missionpages
        return context


# =====================================================================
# Mission Comments Page Setup
# =====================================================================                                         
class MissionCommentsPage(Page):
    parent_page_types = ['MissionPage']
    subpage_types = []
    allow_comments = models.BooleanField('allow comments', default=True)
    comment = RichTextField(features=['h5', 'h6', 'bold', 'italic', 'hr',
                                      'ol', 'ul', 'link', 'document-link', 'image', 'embed'], blank=True)
    content_panels = Page.content_panels + [
        InlinePanel('customcomments', label=("Comments")),
        ]

    def __str__(self):
        return self.title
    
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        missionpages = MissionPage.objects.all()
        context['missionpages'] = missionpages
        return context

    def get_absolute_url(self):
        return self.get_url()


# =====================================================================
# Mission Liens Page Setup
# =====================================================================
class MissionLiensPage(Page):
    parent_page_types = ['MissionPage']
    subpage_types = []
    info = RichTextField(features=['h5', 'h6', 'bold', 'italic', 'hr',
                                   'ol', 'ul', 'link', 'document-link', 'image', 'embed'], blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        missionpages = MissionPage.objects.all()
        context['missionpages'] = missionpages
        return context

# =====================================================================
# Mission Comments Page Setup
# =====================================================================
class CustomComment(XtdComment):
    page = ParentalKey(MissionCommentsPage, on_delete=models.CASCADE, related_name='customcomments')

    def save(self, *args, **kwargs):
        if self.user:
            self.user_name = self.user.display_name
        self.page = MissionCommentsPage.objects.get(pk=self.object_pk)
        super(CustomComment, self).save(*args, **kwargs)

# =====================================================================
# Snippet Models
# =====================================================================

# Snippet model for mission categories (i.e. cruise data, landed data, etc)
@register_snippet
class MissionCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'mission categories'

# Snippet model for the roles that will be associated with reviewers
@register_snippet
class Role(models.Model):
    role = models.CharField(max_length=50)
    panels = [
        FieldPanel('role'),
    ]

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = 'roles'

# Snippet model for reviewer affiliations
@register_snippet
class Affiliate(models.Model):
    affiliation = models.CharField(max_length=250)
    panels = [
        FieldPanel('affiliation'),
    ]

    def __str__(self):
        return self.affiliation

    class Meta:
        verbose_name_plural = 'affiliations'

# Snippet model for reviewers
@register_snippet
class Reviewer(ClusterableModel):
    name = models.CharField(max_length=250)
    affiliation = models.ForeignKey(
        'missions.Affiliate', on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey(
        'missions.Role', on_delete=models.CASCADE, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    uid = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    panels = [
        MultiFieldPanel([
            FieldPanel('name'),
            FieldPanel('email'),
            FieldPanel('uid'),
            FieldPanel('affiliation', widget=forms.Select),
            FieldPanel('role', widget=forms.Select),
        ], heading="Reviewer information"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'reviewers'

# Snippet model for lien types
@register_snippet
class LienType(models.Model):
    lienType = models.CharField(max_length=100)
    panels = [
        FieldPanel('type'),
    ]

    def __str__(self):
        return self.lienType

    class Meta:
        verbose_name_plural = 'lien types'

# Snippet model for lien statuses
@register_snippet
class LienStatus(models.Model):
    status = models.CharField(max_length=20)
    panels = [
        FieldPanel('status')
    ]

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'lien statuses'

# Snippet model for liens
@register_snippet
class Lien(models.Model):
    lienType = models.ForeignKey(
        LienType, on_delete=models.CASCADE, blank=True, null=True)
    assigned = models.ForeignKey(
        Reviewer, on_delete=models.CASCADE,  blank=True, null=True)
    status = models.ForeignKey(
        LienStatus, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField(blank=True)
    reporter = models.ForeignKey(
        Reviewer,  related_name='%(class)s_related', on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('lienType'),
            FieldPanel('assigned'),
            FieldPanel('status'),
            FieldPanel('comment'),
            FieldPanel('reporter'),
            FieldPanel('notes'),
        ], heading="Lien information"),
    ]

    def __str__(self):
        return 'Description:' + self.description