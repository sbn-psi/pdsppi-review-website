from wagtail import blocks
from wagtail.blocks import StructBlock, StructValue
from wagtail.blocks.field_block import CharBlock
from wagtail.images.blocks import ImageChooserBlock

from .custom_table import TableBlock

class InlineImageBlock(blocks.StructBlock):
    image  = ImageChooserBlock(label=("Image"))
    caption= CharBlock(required=False, label=("Caption"))
    float  = blocks.ChoiceBlock(
        required=False,
        choices =[('right', ("Right")), ('left', ("Left")), ('center', ("Center"))],
        default ='right',
        label   =("Float"),
    )
    size = blocks.ChoiceBlock(
        required=False,
        choices =[('small', ("Small")), ('medium', ("Medium")), ('large', ("Large"))],
        default ='small',
        label   =("Size"),
    )

# =====================================================================
# Custom InstructionBlock Setup
# =====================================================================
class ReviewerChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('all', 'All Reviewers'),
        ('science', 'Science Reviewers Only'),
        ('standards', 'Standards Reviewers Only'),
        ('data', 'Data Providers Only'),
    ]
class InstructionBlock(blocks.StructBlock):
    reviewers = ReviewerChoiceBlock()
    instructions = blocks.RichTextBlock(default="Please type out your instructions here.", features=[
                                        'h6', 'bold', 'italic', 'hr', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'])
    class Meta:
        icon = 'doc-empty'

class DataBlock(blocks.StructBlock):
    name = blocks.TextBlock(default="Name of data set")
    link = blocks.RawHTMLBlock(form_classname='link')
    description = blocks.RichTextBlock(default="Description of data set", features=[
                                        'h6', 'bold', 'italic', 'hr', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'])

class MaterialsBlock(blocks.StructBlock):
    name = blocks.TextBlock(default="Material Name")
    link = blocks.RawHTMLBlock(form_classname='link')
    description = blocks.RichTextBlock(default="Description", features=[
                                        'h6', 'bold', 'italic', 'hr', 'ol', 'ul', 'link', 'document-link', 'image', 'embed'])

# =====================================================================
# Custom ScheduleBlock Setup (Implements TableBlock)
# =====================================================================
# Default options for the basic scheduling tables
schedule_table_options = {
    'minSpareRows': 0,
    'startRows': 8,
    'startCols': 2,
    'colHeaders': ['Date', 'Event'],
    'rowHeaders': False,
    'contextMenu': True,
    'columns': [
        {
            'editor': 'date',
            'dateFormat': 'YYYY-MM-DD',
            'correctFormat': True,
            'datePickerConfig': {
                'firstDay': 0,
                'showWeekNumber': True,
                'numberOfMonths': 3,
            },
            'colWidths': 100,
        },
        {
            'editor': 'text'
        }
    ],
    'stretchH': 'last',
    'language': 'en',
    'renderer': 'html',
    'autoColumnSize': True,
}


class ScheduleValue(StructValue):
    def schedule_name(self):
        name = self.get('schedule_name')
        return name

    def schedule(self):
        schedule = self.get('schedule')
        return schedule

    def print_schedule(self):
        value = self.get('schedule')
        x = [['Date', 'Event']]

        for v in value.values():
            if isinstance(v, bool):
                pass
            else:
                for i in v:
                    x.append(i)

        value['data'] = x
        value['first_row_is_table_header'] = True
        value['first_col_is_header'] = False

        block = TableBlock(template='./missions/schedule_table.html')
        result = block.render(value)
        return result

class ScheduleBlock(StructBlock):
    schedule_name = CharBlock(required=True)
    # Here is the culprit, I think
    schedule = TableBlock(table_options=schedule_table_options, blank=True)

    class Meta:
        value_class = ScheduleValue
        template = './missions/schedule_table.html'
        icon = 'date'