"""
Switches allow users to toggle options
"""

from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, NumericProperty, ColorProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSwitch'
]

Builder.load_string("""
<CupertinoSwitch>:
    _padding: self.height*self.thumb_padding
    _thumb: thumb
    _background_color: self.color_untoggled
    
    on_release: self.toggled = not self.toggled
        
    canvas.before:
        Color:
            rgba: self._background_color if self._background_color else self.color_untoggled
        RoundedRectangle:
            radius: self.height/2,
            segments: 500
            size: self.size
            pos: self.pos
    Widget:
        id: thumb
        height: root.height-root._padding
        width: self.height
        x: root.x+root._padding
        center_y: root.y+(root.height/2)
        
        canvas.before:
            Color:
                rgba: root.thumb_color
            Ellipse:
                segments: 500
                size: self.size
                pos: self.pos
""")


class CupertinoSwitch(ButtonBehavior, Widget):
    """
    iOS style Switch. To comply with iOS standard, keep the width to height ratio of
    :class:`CupertinoSwitch` at 1:0.6

    .. image:: ../_static/switch/demo.gif
    """

    toggled = BooleanProperty(False)
    """
    If :class:`CupertinoSwitch` is on
    
    .. image:: ../_static/switch/toggled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(toggled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           toggled: True
    """

    switch_duration = NumericProperty(0.1)
    """
    Duration of color change and thumb movement when state of :class:`CupertinoSwitch` is changed
    
    .. image:: ../_static/switch/switch_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(switch_duration=0.5)
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           switch_duration: 0.5
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    Color of thumb of :class:`CupertinoSwitch`
    
    .. image:: ../_static/switch/thumb_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(thumb_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           thumb_color: 1, 0, 0, 1
    """

    color_toggled = ColorProperty([0.3, 0.85, 0.4, 1])
    """
    Background color of :class:`CupertinoSwitch` when on
    
    .. image:: ../_static/switch/color_toggled.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(color_toggled=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           color_toggled: 1, 0, 0, 1
    """

    color_untoggled = ColorProperty([0.85, 0.85, 0.85, 1])
    """
    Background color of :class:`CupertinoSwitch` when off
    
    .. image:: ../_static/switch/color_untoggled.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(color_untoggled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           color_untoggled: 0.5, 0, 0, 1
    """

    thumb_padding = NumericProperty(0.05)
    """
    Amount of padding around thumb of :class:`CupertinoSwitch` in interval [0, 1] as a percentage of the
    :attr:`height` of :class:`CupertinoSwitch`
    
    .. image:: ../_static/switch/thumb_padding.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(thumb_padding=0.1)
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           thumb_padding: 0.1
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`CupertinoSwitch` and register events

        :param kwargs: Keyword arguments of :class:`CupertinoSwitch`
        """

        super().__init__(**kwargs)
        self.bind(pos=lambda instance, value: self.on_toggled(instance, self.toggled))

    def on_toggled(self, instance, state):
        """
        Callback when state of :class:`CupertinoSwitch` is changed

        :param instance: Instance of :class:`CupertinoSwitch`
        :param state: If :class:`CupertinoSwitch` is toggled
        """

        if state:
            color_animation = Animation(_background_color=self.color_toggled, duration=self.switch_duration)
            thumb_animation = Animation(x=self.x + self.width - self._thumb.width - self._padding,
                                        duration=self.switch_duration)
        else:
            color_animation = Animation(_background_color=self.color_untoggled, duration=self.switch_duration)
            thumb_animation = Animation(x=self.x + self._padding, duration=self.switch_duration)
        color_animation.start(self)
        thumb_animation.start(self._thumb)

    def on_touch_move(self, touch):
        """
        Callback when :class:`CupertinoSwitch` is dragged

        :param touch: :class:`MouseMotionEvent` detected on :class:`CupertinoSwitch`
        """

        if self.collide_point(*touch.opos):
            if touch.x <= self.x:
                self.toggled = False
            elif touch.x >= self.x + self.width:
                self.toggled = True
