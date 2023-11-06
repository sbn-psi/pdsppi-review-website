from django.utils.safestring import mark_safe

from wagtail.admin.ui.components import Component
from wagtail import hooks


class CustomPanel(Component):
	# your code here
	order = 50

	def render_html(self, parent_context):
		return mark_safe("""
				   <h2>Custom Dashboard Panel</h2>
			<p>This is a custom dashboard panel.</p>
		""")

@hooks.register('construct_homepage_panels')
def add_another_panel(request, panels):
	panels.append(CustomPanel())
