"""
Indicators help show progress to users
"""

from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, NumericProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoProgressbar'
]

Builder.load_string("""
<CupertinoProgressBar>:
    canvas.before:
        Color:
            rgba: root.color_unselected
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: root.color_selected
        Rectangle:
            size: self.width*(root.value/100), self.height
            pos: self.pos
""")


class CupertinoProgressbar(Widget):
    """
    iOS style Progress Bar

    .. image:: ../_static/progressbar.gif
    """

    color_selected = ColorProperty([0, 0.5, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of bar of occurred progress
    of :class:`~kivycupertino.uix.indicator.CupertinoProgressBar`
    """

    color_unselected = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of bar of not yet occurred progress
    of :class:`~kivycupertino.uix.indicator.CupertinoProgressBar`
    """

    value = NumericProperty(0)
    """
    A :class:`~kivy.properties.NumericProperty` defining the amount of progress occurred
    in interval `[0, 100]`
    """
