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
            size: dp(self.width*(self.value/100)), dp(self.height)
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

    duration = NumericProperty(1)
    """
    Time for one cycle of :class:`CupertinoActivityIndicator` (in seconds)
    
    .. image:: ../_static/activity_indicator/duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActivityIndicator(duration=2)
    
    **KV**
    
    .. code-block::
    
       CupertinoActivityIndicator:
           duration: 2
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
        Initialize variables of :class:`CupertinoActivityIndicator`

        :param kwargs: Keyword arguments for :class:`CupertinoActivityIndicator`
        """

        super().__init__(**kwargs)

        self._main_spoke = 0
        self._event = None

        self.bind(
            duration=lambda *args: self._change_state(),
            playing=lambda *args: self._change_state()
        )

    def _draw_spokes(self):
        """
        Draw spokes of :class:`CupertinoActivityIndicator`
        """

        self.canvas.clear()
        with self.canvas:
            for i in range(self.spokes):
                PushMatrix()
                Rotate(angle=i * (360 / self.spokes), origin=self.center)
                Color(
                    r=self.color[0],
                    g=self.color[1],
                    b=self.color[2],
                    a=self.color[3] - (((i + self._main_spoke) % self.spokes) * (self.color[3] / self.spokes))
                )
                rect = RoundedRectangle(radius=(self.width / 15,), size=(self.width / self.spokes, self.height / 4))
                rect.pos = self.x + self.width / 2 - rect.size[0] / 2, self.y
                PopMatrix()
        self._main_spoke += 1

    def _change_state(self):
        """
        Callback when the state of :class:`CupertinoActivityIndicator` changes
        """

        if self.playing:
            self._event = Clock.schedule_interval(lambda dt: self._draw_spokes(), self.duration / self.spokes)
        else:
            self.canvas.clear()
            Clock.unschedule(self._event)
