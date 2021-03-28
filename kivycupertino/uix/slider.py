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
    canvas.before:
        Color:
            rgba: self.color_unselected
        RoundedRectangle:
            radius: self.height/6,
            size: self.width, self.height/5
            pos: self.pos
        Color:
            rgba: self.color_selected
        RoundedRectangle:
            radius: self.height/6,
            size: self.width*((self.value-self.min)/(self.max-self.min)), self.height/5
            pos: self.pos
    Widget:
        size: root.height, root.height
        y: root.y+(root.height/12)-(self.height/2)
        x: root.x+root.width*((root.value-root.min)/(root.max-root.min))-self.width/2
        on_touch_down: root._thumb_pressed = self.x <= args[1].x <= self.x+args[0].width and self.y <= args[1].y <= self.y+self.height
        on_touch_up: root._thumb_pressed = False
        on_touch_move: root._move_thumb(args[1])
        
        canvas.before:
            Color:
                rgba: 0, 0, 0, 0.3
            Ellipse:
                size: self.width+2, self.height+2
                pos: self.x-1, self.y-1.5
            Color:
                rgba: 1, 1, 1, 1
            Ellipse:
                size: self.size
                pos: self.pos
                segments: 1000
""")


class CupertinoSlider(Widget):
    """
    iOS style slider

    .. image:: ../_static/slider.gif
    """

    value = NumericProperty(0)
    """
    A :class:`~kivy.properties.NumericProperty` defining the value of
    :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    min = NumericProperty(0)
    """
    A :class:`~kivy.properties.NumericProperty` defining the minimum value of
    :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    max = NumericProperty(100)
    """
    A :class:`~kivy.properties.NumericProperty` defining the maximum value of
    :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the thumb
    of :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    color_selected = ColorProperty([0, 0.5, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of occurred progress
    of :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    color_unselected = ColorProperty([0.7, 0.7, 0.7, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of bar of not yet occurred progress
    of :class:`~kivycupertino.uix.slider.CupertinoSlider`
    """

    _thumb_pressed = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if thumb
    of :class:`~kivycupertino.uix.slider.CupertinoSlider` has been pressed
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.min = int(self.min)
        self.max = int(self.max)
        self.value = self.min if self.value < self.min else self.value

    def _move_thumb(self, touch):
        """
        Callback when thumb of :class:`~kivy.uix.slider.CupertinoSlider` is dragged

        :param touch: Information about mouse position
        """

        if self._thumb_pressed:
            if self.x <= touch.x <= self.x+self.width:
                self.value = int(((touch.x-self.x)/self.width)*(self.max-self.min))+self.min
            else:
                self.value = self.min if touch.x < self.x else self.max
