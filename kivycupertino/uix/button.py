from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string(f"""
#: import images kivycupertino.__init__.images

<CupertinoIconButton>:
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
    Image:
        source: images+root.icon+'.png'
        size: root.size
        pos: root.pos
        allow_stretch: False
        mag_filter: 'nearest'
""")


class CupertinoSystemButton(ButtonBehavior, Label):
    text = StringProperty('')
    color = ColorProperty([0.1, 0.5, 1, 1])


class CupertinoIconButton(ButtonBehavior, Widget):
    icon = StringProperty('')
    background_color = ColorProperty([1, 1, 1, 1])
