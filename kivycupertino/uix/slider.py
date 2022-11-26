"""
Sliders allow users to choose values
"""

from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import NumericProperty, ColorProperty, BooleanProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSlider'
]

Builder.load_string("""
<CupertinoSlider>:
    _track: track
    _thumb: thumb
    _multiplier: ((root.value - root.min) / (root.max - root.min))
    
    on_touch_up: args[1].ungrab(self)
    
    CupertinoProgressbar:
        id: track
        value: root._multiplier
        color_selected: root.color_selected
        color_unselected: root.color_unselected
        size_hint: None, 0.1
        width: root.width - (thumb.width / 2)
        pos_hint: {'center': (0.5, 0.5)}
        on_touch_down: if self.collide_point(*args[1].pos) and root.tap: root._set_value(args[1].x)
    Widget:
        id: thumb
        size_hint: None, None
        size: dp(root.height), dp(root.height)
        center_x: track.x + (track.width * root._multiplier)
        pos_hint: {'center_y': 0.5}
        on_touch_down: if self.collide_point(*args[1].pos): args[1].grab(root)
        
        canvas.before:
            Color:
                rgba: 0.5, 0.5, 0.5, 0.5
            Ellipse:
                size: self.size
                pos: self.pos
            Color:
                rgba: root.thumb_color
            Ellipse:
                size: dp(self.width - 2), dp(self.height - 4)
                pos: dp(self.x + 1), dp(self.y + 3)
""")


class CupertinoSlider(RelativeLayout):
    """
    iOS style slider

    .. image:: ../_static/slider/demo.gif
    """

    value = NumericProperty(0)
    """
    Value of :class:`CupertinoSlider`
    
    .. image:: ../_static/slider/value.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(value=50)
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           value: 50
    """

    min = NumericProperty(0)
    """
    Minimum value of :class:`CupertinoSlider`
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(min=-50)
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           min: -50
    """

    max = NumericProperty(100)
    """
    Maximum value of :class:`CupertinoSlider`
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(max=50)
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           max: 50
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    Color of the thumb of :class:`CupertinoSlider`
    
    .. image:: ../_static/slider/thumb_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(thumb_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           thumb_color: 1, 0, 0, 1
    """

    color_selected = ColorProperty([0, 0.5, 1, 1])
    """
    Color of the bar of occurred progress of :class:`CupertinoSlider`
    
    .. image:: ../_static/slider/color_selected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(color_selected=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           color_selected: 1, 0, 0, 1
    """

    color_unselected = ColorProperty([0.7, 0.7, 0.7, 1])
    """
    Color of bar of not yet occurred progress of :class:`CupertinoSlider`
    
    .. image:: ../_static/slider/color_unselected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(color_unselected=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           color_unselected: 0.5, 0, 0, 1
    """

    tap = BooleanProperty(True)
    """
    If tapping :class:`CupertinoSlider` can change its :attr:`value`
    
    .. image:: ../_static/slider/tap.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSlider(tap=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoSlider:
           tap: True
    """

    def _set_value(self, x):
        """
        Set :attr:`value` based on current position of touch

        :param x: Horizontal component of touch position
        """

        self.value = ((x / self._track.width) * (self.max - self.min)) + self.min
        if self.value < self.min:
            self.value = self.min
        elif self.value > self.max:
            self.value = self.max

    def on_touch_move(self, touch):
        """
        Callback when :class:`CupertinoSlider` is dragged

        :param touch: Touch on :class:`CupertinoSlider`
        """

        if touch.grab_current is self:
            converted_x = self._track.to_widget(*touch.pos, True)[0]
            self._set_value(converted_x)
