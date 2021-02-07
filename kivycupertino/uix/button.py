from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string(f"""
#: import icons kivycupertino.__init__.icons

<CupertinoButton>:
    font_name: 'San Francisco'
    font_size: 17
    color: root.text_color
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_normal
        RoundedRectangle:
            radius: 10,
            size: self.size
            pos: self.pos

<CupertinoSystemButton>:
    font_name: 'San Francisco'
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


class CupertinoButton(ButtonBehavior, Label):
    text = StringProperty('')
    color_normal = ColorProperty([0, 0.5, 1, 1])
    color_down = ColorProperty([0, 0.15, 0.8, 1])
    text_color = ColorProperty([1, 1, 1, 1])


class CupertinoSystemButton(ButtonBehavior, Label):
    text = StringProperty('')
    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    color_down = ColorProperty([0, 0.15, 0.3, 1])


class CupertinoIconButton(ButtonBehavior, Widget):
    icon = StringProperty('')
    background_color = ColorProperty([1, 1, 1, 1])
