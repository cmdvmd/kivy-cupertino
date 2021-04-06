"""
Buttons allow users to execute actions with a single tap
"""

from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.symbol import CupertinoSymbol
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ColorProperty
from kivy.animation import Animation
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
            rgba: self.color_down if self.state == 'down' else self.color_disabled if self.disabled else self.color_normal
        RoundedRectangle:
            radius: self.height/5,
            size: self.size
            pos: self.pos

<CupertinoSystemButton>:
    color: self.color_normal

<CupertinoSymbolButton>:
    color: self.color_normal
    disabled_color: self.color_disabled
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

    transition_duration = NumericProperty(0.075)
    """
    A :class:`~kivy.properties.NumericProperty` defining the duration of the transition of the color of
    :class:`~kivycupertino.uix.button.CupertinoSystemButton` when its state changes
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

    def on_state(self, widget, state):
        """
        Callback when the state of :class:`~kivycupertino.uix.button.CupertinoSystemButton` changes

        :param widget: Instance of :class:`~kivycupertino.uix.button.CupertinoSystemButton`
        :param state: State of :class:`~kivycupertino.uix.button.CupertinoSystemButton`
        """

        if state == 'down':
            animation = Animation(color=self.color_down, duration=self.transition_duration)
        elif state == 'disabled':
            animation = Animation(color=self.color_disabled, duration=self.transition_duration)
        else:
            animation = Animation(color=self.color_normal, duration=self.transition_duration)
        animation.start(widget)


class CupertinoSymbolButton(ButtonBehavior, CupertinoSymbol):
    """
    iOS style button that displays a symbol

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

    transition_duration = NumericProperty(0.075)
    """
    A :class:`~kivy.properties.NumericProperty` defining the duration of the transition of the color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when its state changes
    """

    color_normal = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty`defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when not pressed or disabled
    """

    color_down = ColorProperty([0, 0, 0, 0.7])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when pressed
    """

    color_disabled = ColorProperty([0, 0, 0, 0.7])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.button.CupertinoSymbolButton` when disabled
    """

    def on_state(self, widget, state):
        """
        Callback when the state of :class:`~kivycupertino.uix.button.CupertinoSymbolButton` changes

        :param widget: Instance of :class:`~kivycupertino.uix.button.CupertinoSymbolButton`
        :param state: State of :class:`~kivycupertino.uix.button.CupertinoSymbolButton`
        """

        if state == 'down':
            animation = Animation(color=self.color_down, duration=self.transition_duration)
        elif state == 'disabled':
            animation = Animation(color=self.color_disabled, duration=self.transition_duration)
        else:
            animation = Animation(color=self.color_normal, duration=self.transition_duration)
        animation.start(widget)
