from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, NumericProperty
from kivy.clock import Clock
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


class CupertinoProgressBar(Widget):
    color_selected = ColorProperty([0, 0.5, 1, 1])
    color_unselected = ColorProperty([0, 0, 0, 0])
    value = NumericProperty(0)
