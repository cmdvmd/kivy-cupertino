"""
Indicators help show progress to users
"""

from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, NumericProperty
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
            size: self.width*(root.value/100), self.height
            pos: self.pos
""")


class CupertinoProgressbar(Widget):
    """
    iOS style Progress Bar

    .. image:: ../_static/progressbar.gif
    """

    value = NumericProperty(0)
    """
    A :class:`~kivy.properties.NumericProperty` defining the amount of progress occurred
    in interval `[0, 100]` of :class:`~kivycupertino.uix.indicator.CupertinoProgressbar`
    """

    color_selected = ColorProperty([0, 0.5, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of occurred progress
    of :class:`~kivycupertino.uix.indicator.CupertinoProgressBar`
    """

    color_unselected = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of not yet occurred progress
    of :class:`~kivycupertino.uix.indicator.CupertinoProgressBar`
    """


class CupertinoActivityIndicator(Widget):
    """
    iOS style activity indicator

    .. image:: ../_static/activity_indicator.gif
    """

    num_spokes = NumericProperty(12)
    """
    A :class:`~kivy.properties.NumericProperty` defining the amount of spokes of
    :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
    """

    color = ColorProperty([0.6, 0.6, 0.65, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the spokes of
    :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`

        :param kwargs: Keyword arguments of :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
        """

        super().__init__(**kwargs)

        self.main_spoke = 0
        self.__event = None
        self.stop()

    def stop(self):
        """
        Hide :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator` (hidden by default)
        """

        Clock.unschedule(self.__event)

    def start(self):
        """
        Show and begin playing animation of :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
        """

        self.__event = Clock.schedule_interval(lambda dt: self.__draw_spokes(), 1/self.num_spokes)

    def __draw_spokes(self):
        """
        Draw spokes of :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
        """

        self.canvas.clear()
        with self.canvas:
            for i in range(self.num_spokes):
                PushMatrix()
                Rotate(angle=i*(360/self.num_spokes), origin=self.center)
                Color(
                    r=self.color[0],
                    g=self.color[1],
                    b=self.color[2],
                    a=self.color[3]-(((i+self.main_spoke) % self.num_spokes)*(self.color[3]/self.num_spokes))
                )
                rect = RoundedRectangle(radius=(self.width/15,), size=(self.width/10, self.height/4))
                rect.pos = self.x+self.width/2-rect.size[0]/2, self.y
                PopMatrix()
        self.main_spoke += 1
