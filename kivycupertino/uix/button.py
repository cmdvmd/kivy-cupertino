from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string(f"""
#: import icons kivycupertino.__init__.icons

<CupertinoSystemButton>:
    color: root.color_down if self.state == 'down' else root.color_normal

<CupertinoIconButton>:
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    Image:
        source: icons+root.icon+'.png'
        size: root.size
        pos: root.pos
        allow_stretch: False
        mag_filter: 'nearest'
""")


class CupertinoSystemButton(ButtonBehavior, Label):
    text = StringProperty('')
    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    color_down = ColorProperty([0, 0.15, 3, 1])


class CupertinoIconButton(ButtonBehavior, Widget):
    icon = StringProperty('')
    background_color = ColorProperty([1, 1, 1, 1])
