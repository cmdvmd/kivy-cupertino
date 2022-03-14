"""
Buttons allow users to execute actions with a single tap
"""

from kivy.uix.widget import Widget
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.symbol import CupertinoSymbol
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ColorProperty, ListProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoButton',
    'CupertinoSystemButton',
    'CupertinoSymbolButton',
    'CupertinoModalButton'
]

Builder.load_string("""
<CupertinoButton>:
    color: self.color_normal
    
    canvas.before:
        Color:
            rgba: self.color if self.color is not None else (0, 0, 0, 0)
        RoundedRectangle:
            radius: dp(self.height/5),
            size: self.size
            pos: self.pos
    
    CupertinoLabel:
        text: root.text
        font_size: root.font_size
        color: root.text_color
        size: root.size
        pos: root.pos

<CupertinoSystemButton>:
    color: self.color_normal

<CupertinoSymbolButton>:
    color: self.color_normal

<CupertinoModalButton>:    
    canvas.before:
        Clear
        Color:
            rgba: self.color
        RoundedRectangle:
            radius: root._radii
            size: self.size
            pos: self.pos
""")


class _BaseButton(ButtonBehavior):
    """
    Base class for buttons that can only be used with an instance of :class:`kivy.uix.widget.Widget`
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoButton` is disabled
    """

    transition_duration = NumericProperty()
    """
    Duration of the transition of the color of :class:`_BaseButton` when its state changes
    """

    color_normal = ColorProperty()
    """
    Color of :class:`_BaseButton` when not pressed or disabled
    """

    color_down = ColorProperty()
    """
    Color of :class:`_BaseButton` when pressed
    """

    color_disabled = ColorProperty()
    """
    Color of :class:`_BaseButton` when disabled
    """

    def __init__(self, **kwargs):
        """
        Initialize behavior of :class:`_BaseButton`

        :param kwargs: Keyword arguments of :class:`_BaseButton`
        """

        super().__init__(**kwargs)
        self.bind(
            disabled=lambda *args: self.animate_color(),
            state=lambda *args: self.animate_color()
        )

    def animate_color(self):
        """
        Callback when the state of :class:`CupertinoSymbolButton` changes
        """

        if self.state == 'down':
            animation = Animation(color=self.color_down, duration=self.transition_duration)
        elif self.disabled:
            animation = Animation(color=self.color_disabled, duration=self.transition_duration)
        else:
            animation = Animation(color=self.color_normal, duration=self.transition_duration)
        animation.start(self)


class CupertinoButton(_BaseButton, Widget):
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

    font_size = NumericProperty('17sp')
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

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoButton` when its state changes
    
    .. image:: ../_static/button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(transition_duration=0.5)
       
    **KV**
    
    .. code-block::

       CupertinoButton:
           transition_duration: 0.5
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
    
       CupertinoButton(text_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_disabled: 1, 0, 0, 1
    """


class CupertinoSystemButton(_BaseButton, CupertinoLabel):
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


class CupertinoSymbolButton(_BaseButton, CupertinoSymbol):
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


class CupertinoModalButton(CupertinoButton, CupertinoLabel):
    """
    Adaptive button to be used in Dialogs

    .. image:: ../_static/modal_button/demo.gif
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(text='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           text: 'Hello World'
    """

    font_size = NumericProperty('14sp')
    """
    Size of text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(font_size='20sp')
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           font_size: '20sp'
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoButton` when its state changes
    
    .. image:: ../_static/modal_button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(transition_duration=0.5)
       
    **KV**
    
    .. code-block::

       CupertinoModalButton:
           transition_duration: 0.5
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoModalButton` is disabled
    
    .. image:: ../_static/modal_button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           disabled: True
    """

    color_normal = ColorProperty([1, 1, 1, 0.9])
    """
    Background color of :class:`CupertinoModalButton` when not pressed
    
    .. image:: ../_static/modal_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(color_normal=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([0.9, 0.9, 0.9, 1])
    """
    Background color of :class:`CupertinoModalButton` when pressed
    
    .. image:: ../_static/modal_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_down: 0.5, 0, 0, 1
    """

    color_disabled = ColorProperty([0.8, 0.8, 0.8, 1])
    """
    Background color of :class:`CupertinoModalButton` when disabled
    
    .. image:: ../_static/modal_button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([0.05, 0.5, 1, 1])
    """
    Color of the text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(text_color=(1, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_down: 1, 0, 0, 1
    """

    cancel = BooleanProperty(False)
    """
    If :class:`CupertinoModalButton` should be a cancel button when added to an instance of
    :class:`CupertinoActionSheet`
    
    .. image:: ../_static/modal_button/cancel.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(cancel=True)
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           cancel: True
    """

    _radii = ListProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ListProperty` defining the radii values of the corners of :class:`CupertinoModalButton`
    """
