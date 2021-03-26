"""
ScrollViews help show lots of information within a set screen size
"""

from kivy.uix.scrollview import ScrollView
from kivy.properties import ColorProperty
from kivy.lang import Builder

__all__ = [
    'CupertinoScrollView'
]

Builder.load_string("""
<CupertinoScrollView>:
    bar_margin: 2
    bar_width: 4
""")


class CupertinoScrollView(ScrollView):
    """
    iOS style ScrollView

    .. image:: ../_static/scrollview.gif
    """

    bar_color = ColorProperty([0.65, 0.65, 0.65, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of
    :class:`~kivycupertino.uix.scrollview.CupertinoScrollView` when scrolling
    """

    bar_inactive_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of
    :class:`~kivycupertino.uix.scrollview.CupertinoScrollView` when not scrolling
    """
