"""
Buttons allow users to execute actions with a single tap
"""

from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.symbol import CupertinoSymbol
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ColorProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoButton',
    'CupertinoSystemButton',
    'CupertinoNextButton',
    'CupertinoBackButton',
    'CupertinoSymbolButton'
]

Builder.load_string("""
<CupertinoButton>:    
    font_size: '17sp'
    color: root.text_color
    
    canvas.before:
        Color:
            rgba: self.color_down if self.state == 'down' else self.color_disabled if self.disabled else self.color_normal
        RoundedRectangle:
            radius: dp(self.height/5),
            size: self.size
            pos: self.pos

<CupertinoSystemButton>:
    color: self.color_normal
    disabled_color: self.color_disabled

<CupertinoBackButton>:
    text: '‹'

<CupertinoNextButton>:
    text: '›'

<CupertinoSymbolButton>:
    color: self.color_normal
    disabled_color: self.color_disabled
""")


class CupertinoButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style button

    .. image:: ../_static/button/demo.gif
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoButton`
    
    .. image:: ../_static/button/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(text='Hello World')
   
   **KV**
   
   .. code-block::
   
      CupertinoButton:
          text: 'Hello World'
    """

    font_size = NumericProperty('15sp')
    """
    text of :class:`CupertinoButton`
    
    .. image:: ../_static/button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(font_size='20sp')
   
   **KV**
   
   .. code-block::
   
      CupertinoButton:
          font_size: '20sp'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoButton` is disabled
    
    .. image:: ../_static/button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           disabled: True
    """

    color_normal = ColorProperty([0, 0.5, 1, 1])
    """
    Color of :class:`CupertinoButton` when not pressed or disabled
    
    .. image:: ../_static/button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(color_normal=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0.15, 0.8, 1])
    """
    Background color of :class:`CupertinoButton` when pressed
    
    .. image:: ../_static/button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(color_down=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0.35, 0.7, 1])
    """
    Background color of :class:`CupertinoButton` when disabled
    
    .. image:: ../_static/button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of text of
    :class:`CupertinoButton`
    
    .. image:: ../_static/button/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(text_color=(0, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_disabled: 0, 0, 0, 1
    """


class CupertinoSystemButton(ButtonBehavior, CupertinoLabel):
    """
    iOS style System Button

    .. image:: ../_static/system_button/demo.gif
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoSystemButton`
    
    .. image:: ../_static/system_button/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(text='Send')
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           text: 'Send'
    """

    font_size = NumericProperty('15sp')
    """
    Font size of the text of :class:`CupertinoSystemButton`
    
    .. image:: ../_static/system_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(font_size='20sp')
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           font_size: '20sp'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoSystemButton` is disabled
    
    .. image:: ../_static/system_button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(disabled=True)
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoSystemButton` when its state changes
    
    .. image:: ../_static/system_button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(transition_duration=0.5)
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           transition_duration: 0.5
    """

    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    """
    Color of :class:`CupertinoSystemButton` when not pressed or disabled
    
    .. image:: ../_static/system_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(color_normal=(1, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0.15, 0.3, 1])
    """
    Color of :class:`CupertinoSystemButton` when pressed
    
    .. image:: ../_static/system_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(color_down=(1, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    Color of :class:`CupertinoSystemButton` when disabled
    
    .. image:: ../_static/system_button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSystemButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSystemButton:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """

    def on_state(self, instance, state):
        """
        Callback when the state of :class:`CupertinoSystemButton` changes

        :param instance: Instance of :class:`CupertinoSystemButton`
        :param state: State of :class:`CupertinoSystemButton`
        """

        if state == 'down':
            animation = Animation(color=self.color_down, duration=self.transition_duration)
        else:
            animation = Animation(color=self.color_normal, duration=self.transition_duration)
        animation.start(instance)


class CupertinoBackButton(CupertinoSystemButton):
    """
    iOS style back button

    .. image:: ../_static/back_button/demo.gif
    """

    font_size = NumericProperty('50sp')
    """
    Font size of the text of :class:`CupertinoBackButton`
    
    .. image:: ../_static/back_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(font_size='100sp')
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           font_size: '100sp'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoBackButton` is disabled
    
    .. image:: ../_static/back_button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoBackButton` when its state changes
    
    .. image:: ../_static/back_button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(transition_duration=0.5)
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           transition_duration: 0.5
    """

    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    """
    Color of :class:`CupertinoBackButton` when not pressed or disabled
    
    .. image:: ../_static/back_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(color_normal=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0.15, 0.3, 1])
    """
    Color of :class:`CupertinoBackButton` when pressed
    
    .. image:: ../_static/back_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(color_down=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    Color of :class:`CupertinoBackButton` when disabled
    
    .. image:: ../_static/back_button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoBackButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoBackButton:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """


class CupertinoNextButton(CupertinoSystemButton):
    """
    iOS style next button

    .. image:: ../_static/next_button/demo.gif
    """

    font_size = NumericProperty('50sp')
    """
    Font size of the text of :class:`CupertinoNextButton`
    
    .. image:: ../_static/next_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(font_size='100sp')
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           font_size: '100sp'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoNextButton` is disabled
    
    .. image:: ../_static/next_button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoNextButton` when its state changes
    
    .. image:: ../_static/next_button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(transition_duration=0.5)
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           transition_duration: 0.5
    """

    color_normal = ColorProperty([0.05, 0.5, 0.95, 1])
    """
    Color of :class:`CupertinoNextButton` when not pressed or disabled
    
    .. image:: ../_static/next_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(color_normal=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0.15, 0.3, 1])
    """
    Color of :class:`CupertinoNextButton` when pressed
    
    .. image:: ../_static/next_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(color_down=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    Color of :class:`CupertinoNextButton` when disabled
    
    .. image:: ../_static/next_button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNextButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoNextButton:
           disabled: True
           color_normal: 0.5, 0, 0, 1
    """


class CupertinoSymbolButton(ButtonBehavior, CupertinoSymbol):
    """
    iOS style button that displays a symbol

    .. image:: ../_static/symbol_button/demo.gif
    """

    symbol = StringProperty(' ')
    """
    :ref:`Symbol <symbol>` of :class:`CupertinoSymbolButton`
    
    .. image:: ../_static/symbol_button/symbol.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(symbol='wifi')
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           symbol: 'wifi'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoSymbolButton` is disabled
    
    .. image:: ../_static/symbol_button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoSymbolButton` when its state changes
    
    .. image:: ../_static/symbol_button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(transition_duration=0.5)
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           transition_duration: 0.5
    """

    color_normal = ColorProperty([0, 0, 0, 1])
    """
    Color of :class:`CupertinoSymbolButton` when not pressed or disabled
    
    .. image:: ../_static/symbol_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(color_normal=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0, 0, 0.7])
    """
    Color of :class:`CupertinoSymbolButton` when pressed
    
    .. image:: ../_static/symbol_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(color_down=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0, 0, 0.7])
    """
    Color of :class:`CupertinoSymbolButton` when disabled
    
    .. image:: ../_static/symbol_button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbolButton(color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbolButton:
           color_disabled: 0.5, 0, 0, 1
    """

    def on_state(self, instance, state):
        """
        Callback when the state of :class:`CupertinoSymbolButton` changes

        :param instance: Instance of :class:`CupertinoSymbolButton`
        :param state: State of :class:`CupertinoSymbolButton`
        """

        if state == 'down':
            animation = Animation(color=self.color_down, duration=self.transition_duration)
        elif state == 'disabled':
            animation = Animation(color=self.color_disabled, duration=self.transition_duration)
        else:
            animation = Animation(color=self.color_normal, duration=self.transition_duration)
        animation.start(instance)
