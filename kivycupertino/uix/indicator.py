"""
Indicators help show progress to users
"""

from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, NumericProperty
from kivy.lang.builder import Builder

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
    Color of bar of occurred progress
    
    :attr:`color_selected` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0.5, 1, 1]`
    """

    color_unselected = ColorProperty([0, 0, 0, 0])
    """
    Color of bar of not occurred progress
    
    :attr:`color_unselected` is a :class:`~kivy.properties.ColorProperty` and defaults to [0, 0, 0, 0]
    """

    value = NumericProperty(0)
    """
    Amount of progress occurred in interval `[0, 100]`
    
    :attr:`value` is a :class:`~kivy.properties.NumericProperty` and defaults to `0`
    """
