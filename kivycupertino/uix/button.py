from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string(f"""
#: import icons_path kivycupertino.__init__.icons_path

<CupertinoButton>:
    font_size: 17
    color: root.text_color
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_disabled if root.disabled else root.color_normal
        RoundedRectangle:
            radius: self.height/5,
            size: self.size
            pos: self.pos

<CupertinoSystemButton>:
    color: root.color_down if self.state == 'down' else root.color_disabled if root.disabled else root.color_normal

<CupertinoIconButton>:
    canvas.before:
        Color:
            rgba: root.background_down if self.state == 'down' else root.background_disabled if root.disabled else root.background_normal
        Rectangle:
            size: self.size
            pos: self.pos
    Image:
        source: icons_path+root.icon+'.png'
        size: root.size
        pos: root.pos

<CupertinoDialogButton>:
    color: root.text_color
    markup: True
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_normal
        RoundedRectangle:
            radius: root.radii
            size: self.size
            pos: self.pos
""")


class CupertinoButton(ButtonBehavior, CupertinoLabel):
    text = StringProperty('')
    disabled = BooleanProperty(False)
    color_normal = ColorProperty([0, 0.5, 1, 1])
    color_down = ColorProperty([0, 0.15, 0.8, 1])
    color_disabled = ColorProperty([0, 0.35, 0.7, 1])
    text_color = ColorProperty([1, 1, 1, 1])


class CupertinoSystemButton(ButtonBehavior, CupertinoLabel):
    text = StringProperty('')
    disabled = BooleanProperty(False)
    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    color_down = ColorProperty([0, 0.15, 0.3, 1])
    color_disabled = ColorProperty([0, 0.3, 0.4, 1])


class CupertinoIconButton(ButtonBehavior, Widget):
    icon = StringProperty('')
    disabled = BooleanProperty(False)
    background_normal = ColorProperty([0, 0, 0, 0])
    background_down = ColorProperty([0, 0, 0, 0.3])
    background_disabled = ColorProperty([0, 0, 0, 0.2])
