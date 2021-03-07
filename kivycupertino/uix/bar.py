"""
Bars are generally positioned at the top of a screen,
containing widgets and information for easy access by users
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ColorProperty
from kivy.lang.builder import Builder

Builder.load_string("""
<CupertinoNavigationBar>:
    canvas.before:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Rectangle:
            size: self.width, 1
            pos: self.pos
""")


class CupertinoNavigationBar(FloatLayout):
    """
    iOS style Navigation Bar. :class:`~kivycupertino.uix.bar.CupertinoNavigationBar`
    is a :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

    .. image:: ../_static/navigation_bar.png
    """

    color = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.bar.CupertinoNavigationBar`
    """
