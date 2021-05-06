"""
Indicators help show progress to users
"""

from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty
from kivy.graphics import PushMatrix, PopMatrix, Rotate, Color, RoundedRectangle
from kivy.clock import Clock
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoProgressbar',
    'CupertinoActivityIndicator'
]

Builder.load_string("""
<CupertinoProgressBar>:
    canvas.before:
        Color:
            rgba: self.color_unselected
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: self.color_selected
        Rectangle:
            size: self.width*(self.value/100), self.height
            pos: self.pos
""")


class CupertinoProgressbar(Widget):
    """
    iOS style Progress Bar

    .. image:: ../_static/progressbar/demo.gif
    """

    value = NumericProperty(0)
    """
    Amount of progress occurred in interval `[0, 100]` of :class:`CupertinoProgressbar`
    
    .. image:: ../_static/progressbar/value.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoProgressbar(value=50)
    
    **KV**
    
    .. code-block::
    
       CupertinoProgressbar:
           value: 50
    """

    color_selected = ColorProperty([0, 0.5, 1, 1])
    """
    Color of the bar of occurred progress of :class:`CupertinoProgressBar`
    
    .. image:: ../_static/progressbar/color_selected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoProgressbar(color_selected=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoProgressbar:
           color_selected: 1, 0, 0, 1
    """

    color_unselected = ColorProperty([0, 0, 0, 0])
    """
    Color of the bar of not yet occurred progress of :class:`CupertinoProgressBar`
    
    .. image:: ../_static/progressbar/color_unselected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoProgressbar(color_unselected=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoProgressbar:
           color_unselected: 0.5, 0, 0, 1
    """

    def on_value(self, instance, value):
        """
        Callback when value of :class:`CupertinoProgressbar`

        :param instance: Instance of :class:`CupertinoProgressbar`
        :param value: Value of :class:`CupertinoProgressbar`
        """

        self.value = value % 101


class CupertinoActivityIndicator(Widget):
    """
    iOS style activity indicator

    .. image:: ../_static/activity_indicator/demo.gif
    """

    spokes = NumericProperty(12)
    """
    Amount of spokes of :class:`CupertinoActivityIndicator`
    
    .. image:: ../_static/activity_indicator/spokes.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActivityIndicator(spokes=20)
    
    **KV**
    
    .. code-block::
    
       CupertinoActivityIndicator:
           spokes: 20
    """

    color = ColorProperty([0.6, 0.6, 0.65, 1])
    """
    Color of the spokes of :class:`CupertinoActivityIndicator`
    
    .. image:: ../_static/activity_indicator/color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActivityIndicator(color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoActivityIndicator:
           color: 1, 0, 0, 1
    """

    playing = BooleanProperty(False)
    """
    Color of the spokes of :class:`CupertinoActivityIndicator`
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActivityIndicator(playing=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoActivityIndicator:
           playing: True
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`CupertinoActivityIndicator`

        :param kwargs: Keyword arguments of :class:`CupertinoActivityIndicator`
        """

        super().__init__(**kwargs)

        self.__main_spoke = 0
        self.__event = None

    def __draw_spokes(self):
        """
        Draw spokes of :class:`CupertinoActivityIndicator`
        """

        self.canvas.clear()
        with self.canvas:
            for i in range(self.spokes):
                PushMatrix()
                Rotate(angle=i*(360/self.spokes), origin=self.center)
                Color(
                    r=self.color[0],
                    g=self.color[1],
                    b=self.color[2],
                    a=self.color[3]-(((i+self.__main_spoke) % self.spokes)*(self.color[3]/self.spokes))
                )
                rect = RoundedRectangle(radius=(self.width/15,), size=(self.width/10, self.height/4))
                rect.pos = self.x+self.width/2-rect.size[0]/2, self.y
                PopMatrix()
        self.__main_spoke += 1

    def on_playing(self, instance, value):
        """
        Callback when the state of :class:`CupertinoActivityIndicator` changes

        :param instance: Instance of :class:`CupertinoActivityIndicator`
        :param value: State of :class:`CupertinoActivityIndicator`
        """

        if value:
            self.__event = Clock.schedule_interval(lambda dt: self.__draw_spokes(), 1/self.spokes)
        else:
            self.canvas.clear()
            Clock.unschedule(self.__event)
