from django import forms
from .models import CustomComment
from django.utils.translation import ugettext_lazy as _

from django_comments_xtd.forms import XtdCommentForm
from django_comments_xtd.models import TmpXtdComment


class CommentForm(XtdCommentForm):
    def get_comment_create_data(self):
        data = super(CustomComment, self).get_comment_create_data()
        return data