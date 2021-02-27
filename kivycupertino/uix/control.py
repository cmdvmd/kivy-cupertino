from kivycupertino.uix.button import CupertinoSystemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ColorProperty
from kivy.graphics import Color, RoundedRectangle
from kivy.lang.builder import Builder

Builder.load_string("""
<CupertinoSegmentedControls>:
    orientation: 'horizontal'
    spacing: 3
    padding: 3
    
    canvas.before:
        Color:
            rgba: root.background_color
        RoundedRectangle:
            radius: 10,
            size: self.size
            pos: self.pos
""")


class CupertinoSegmentedControls(BoxLayout):
    background_color = ColorProperty([0.95, 0.95, 0.95, 0.9])
    color_selected = ColorProperty([1, 1, 1, 1])
    text_color = ColorProperty([0, 0, 0, 1])

    def __select(self, tab, action=None):
        for child in self.children:
            child.canvas.before.clear()

        with tab.canvas.before:
            Color(rgba=self.color_selected)
            RoundedRectangle(radius=(10,), size=tab.size, pos=tab.pos)

        if action is not None:
            action(tab)

    def add_tab(self, text, action):
        tab = CupertinoSystemButton(
            text=text,
            color_normal=self.text_color,
            color_down=self.text_color,
            on_release=lambda b: self.__select(b, action)
        )
        self.add_widget(tab)
        self.__select(tab)
