from django_component import Library,Component
register=Library()


@register.component
class component_io_Button(Component):template='component/io/Button.html'

@register.component
class component_decoration_RoundBottomBorder(Component):template='component/decoration/RoundBottomBorder.html'

@register.component
class page_About(Component):template='main_templates/About.html'

@register.component
class page_Home(Component):template='main_templates/Home.html'

@register.component
class layout_Root(Component):template='layout/Root.html'

@register.component
class layout_Simple(Component):template='layout/Simple.html'

@register.component
class component_io_AnchorButton(Component):template='component/io/buttons/AnchorButton.html'
@register.component
class component_io_JSButton(Component):template='component/io/buttons/JSButton.html'