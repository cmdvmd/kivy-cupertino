"""
Sliders allow users to choose values
"""

from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ColorProperty, BooleanProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSlider'
]

Builder.load_string("""
<CupertinoSlider>:
    _track: track
    _selected: selected
    _thumb: thumb
    
    Widget:
        id: track
        size: root.width-thumb.width, root.height*0.1
        pos: root.x+(thumb.width/2), root.y+root.height/2-self.height/2
        canvas.before:
            Color:
                rgba: root.color_unselected
            RoundedRectangle:
                radius: self.height/2,
                size: self.size
                pos: self.pos
    Widget:
        id: selected
        size: track.width*((root.value-root.min)/(root.max-root.min)), track.height
        pos: track.pos
        canvas.before:
            Color:
                rgba: root.color_selected
            RoundedRectangle:
                radius: self.height/2,
                size: self.size
                pos: self.pos
    Widget:
        id: thumb
        size: root.height, root.height
        pos: selected.x+selected.width-self.width/2, root.y
        on_touch_down: args[1].ud['thumb_pressed'] = self.collide_point(args[1].x, args[1].y)
        
        canvas.before:
            Color:
                rgba: 0.5, 0.5, 0.5, 0.5
            Ellipse:
                size: self.size
                pos: self.pos
            Color:
                rgba: root.thumb_color
            Ellipse:
                size: self.width-2, self.height-4
                pos: self.x+1, self.y+3
""")


class CupertinoSlider(Widget):
    """
    iOS style slider
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min = int(self.min)
        self.max = int(self.max)
        self.value = int(self.value) if 'value' in kwargs else self.min

    def _set_value(self, position):
        """
        Callback to set :attr:`value` based on position of touch

        :param position: Position of touch
        """

        self.value = int((self.max-self.min)*(min(1, max(0, (position-self._track.x)/self._track.width))))+self.min

    def on_touch_up(self, touch):
        """
        Callback when :class:`CupertinoSlider` is released

        :param touch: Touch on :class:`CupertinoSlider`
        """

        if self.tap and self._track.collide_point(touch.x, touch.y):
            self._set_value(touch.x)

    def on_touch_move(self, touch):
        """
        Callback when the thumb of :class:`CupertinoSlider` is dragged

        :param touch: Touch on :class:`CupertinoSlider`
        """

        if touch.ud['thumb_pressed']:
            self._set_value(touch.x)
