"""
Indicators help show progress to users

Usage:
------

**Activity Indicator**

.. image:: ../../_static/activity_indicator.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.indicator import CupertinoActivityIndicator
    from kivy.uix.floatlayout import FloatLayout


    class TestApp(CupertinoApp):

        def build(self):
            layout = FloatLayout()

            activity_indicator = CupertinoActivityIndicator(size_hint=[0.1, 0.1], pos_hint={'center': (0.5, 0.2)})
            activity_indicator.start()

            layout.add_widget(activity_indicator)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

**Progress Bar**

.. image:: ../../_static/progressbar.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivy.clock import Clock
    from kivycupertino.uix.indicator import CupertinoProgressbar
    from kivy.uix.floatlayout import FloatLayout
    from kivy.core.window import Window


    class TestApp(CupertinoApp):

        def update(self, bar):
            bar.value += 1

        def build(self):
            layout = FloatLayout()
            bar = CupertinoProgressbar(size_hint_x=0.9, size_hint_y=0.05, pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(bar)

            Clock.schedule_interval(lambda dt: self.update(bar), 0.075)

            return layout


        Window.clearcolor = 0.98, 0.98, 0.98, 1


    Window.size = (300, 500)

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

Api:
----
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

    def on_value(self, widget, value):
        self.value = value % 101


class CupertinoActivityIndicator(Widget):
    """
    iOS style activity indicator
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
        self.__playing = False
        self.stop()

    def stop(self):
        """
        Hide :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator` (hidden by default)
        """

        self.__playing = False
        self.canvas.clear()
        Clock.unschedule(self.__event)

    def start(self):
        """
        Show and begin playing animation of :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
        """

        self.__playing = True
        self.__event = Clock.schedule_interval(lambda dt: self.__draw_spokes(), 1/self.num_spokes)

    def toggle(self):
        """
        Change state of :class:`~kivycupertino.uix.indicator.CupertinoActivityIndicator`
        """

        if not self.__playing:
            self.start()
        else:
            self.stop()

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
