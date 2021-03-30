"""
Buttons allow users to execute actions with a single tap
"""

from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.symbol import CupertinoSymbol
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, BooleanProperty, ColorProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoButton',
    'CupertinoSystemButton',
    'CupertinoSymbolButton'
]

Builder.load_string(f"""
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

<CupertinoSymbolButton>:
    color: root.symbol_color
    
    canvas.before:
        Color:
            rgba: root.background_down if self.state == 'down' else root.background_disabled if root.disabled else root.background_normal
        Rectangle:
            size: self.size
            pos: self.pos
""")


class CupertinoButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style button

    .. image:: ../_static/button.gif
    """

    text = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of
    :class:`~kivycupertino.uix.button.CupertinoButton`
    """

    disabled = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.button.CupertinoButton` is disabled
    """

    color_normal = ColorProperty([0, 0.5, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoButton` when not pressed or disabled
    """

    color_down = ColorProperty([0, 0.15, 0.8, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoButton` when pressed
    """

    color_disabled = ColorProperty([0, 0.35, 0.7, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoButton` when disabled    
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of text of
    :class:`~kivycupertino.uix.button.CupertinoButton`    
    """


class CupertinoSystemButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style System Button

    .. image:: ../_static/system_button.gif
    """

    text = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of
    :class:`~kivycupertino.uix.button.CupertinoSystemButton`
    """

    disabled = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.button.CupertinoSystemButton` is disabled
    """

    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSystemButton` when not pressed or disabled
    """

    color_down = ColorProperty([0, 0.15, 0.3, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSystemButton` when disabled
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSystemButton` when disabled
    """


class CupertinoSymbolButton(ButtonBehavior, CupertinoSymbol):
    """
    iOS style button that displays an symbol

    .. image:: ../_static/symbol_button.gif
    """

    symbol = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the symbol of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton`
    """

    disabled = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` is disabled
    """

    symbol_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty`defining the color of the icon of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when not pressed or disabled
    """

    background_normal = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty`defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when not pressed or disabled
    """

    background_down = ColorProperty([0, 0, 0, 0.3])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when pressed
    """

    background_disabled = ColorProperty([0, 0, 0, 0.2])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when disabled
    """
