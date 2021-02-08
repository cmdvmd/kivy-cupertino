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
    color = ColorProperty([0.95, 0.95, 0.95, 1])
