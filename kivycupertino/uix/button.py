"""
Buttons allow users to execute actions with a single tap
"""

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
""")


class CupertinoButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style button

    .. image:: ../_static/button.gif
    """

    text = StringProperty('')
    """
    Text of :class:`~kivycupertino.uix.button.CupertinoButton`
    
    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to `""`
    """

    disabled = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.button.CupertinoButton` is disabled
    
    :attr:`disabled` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    color_normal = ColorProperty([0, 0.5, 1, 1])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoButton` when not pressed or disabled
    
    :attr:`color_normal` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.5, 1, 1]`
    """

    color_down = ColorProperty([0, 0.15, 0.8, 1])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoButton` when pressed
    
    :attr:`color_down` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.15, 0.8, 1]`
    """

    color_disabled = ColorProperty([0, 0.35, 0.7, 1])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoButton` when disabled
    
    :attr:`color_disabled` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.35, 0.7, 1]`
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    Color of text of :class:`~kivycupertino.uix.button.CupertinoButton`
    
    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[1, 1, 1, 1]`
    """


class CupertinoSystemButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style System Button

    .. image:: ../_static/system_button.gif
    """

    text = StringProperty('')
    """
    Text of :class:`~kivycupertino.uix.button.CupertinoSystemButton`
    
    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to `""`
    """

    disabled = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.button.CupertinoSystemButton` is disabled
    
    :attr:`disabled` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    """
    Color of :class:`~kivycupertino.uix.button.CupertinoSystemButton` when not pressed or disabled
    
    :attr:`color_normal` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.05, 0.5, 0.95, 1]`
    """

    color_down = ColorProperty([0, 0.15, 0.3, 1])
    """
    Color of :class:`~kivycupertino.uix.button.CupertinoSystemButton` when disabled
    
    :attr:`color_down` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.15, 0.3, 1]`
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    Color of :class:`~kivycupertino.uix.button.CupertinoSystemButton` when disabled
    
    :attr:`color_disabled` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.3, 0.4, 1]`
    """


class CupertinoIconButton(ButtonBehavior, Widget):
    """
    iOS style button that displays an icon

    .. image:: ../_static/icon_button.gif
    """

    icon = StringProperty('')
    """
    Icon of :class:`~kivycupertino.uix.button.CupertinoIconButton`
    
    :attr:`icon` is a :class:`~kivy.properties.StringProperty` and defaults to `""`
    """

    disabled = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.button.CupertinoIconButton` is disabled
    
    :attr:`disabled` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    background_normal = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoIconButton` when not pressed or disabled
    
    :attr:`background_normal` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 0]`
    """

    background_down = ColorProperty([0, 0, 0, 0.3])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoIconButton` when pressed
    
    :attr:`background_down` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 0.3]`
    """

    background_disabled = ColorProperty([0, 0, 0, 0.2])
    """
    Background color of :class:`~kivycupertino.uix.button.CupertinoButton` when disabled
    
    :attr:`background_disabled` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 0.2]`
    """
