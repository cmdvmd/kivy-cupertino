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

<CupertinoStepper>:
    orientation: 'horizontal'
    spacing: 2
    
    CupertinoSystemButton:
        text: '-'
        font_size: 25
        color_normal: root.text_color
        color_down: root.text_color
        on_release: root.dispatch('on_minus')
        
        canvas.before:
            Color:
                rgba: root.color_down if self.state == 'down' else root.color_normal
            RoundedRectangle:
                radius: root.height/4, 0, 0, root.height/4
                size: self.size
                pos: self.pos
    CupertinoSystemButton:
        text: '+'
        font_size: 25
        color_normal: root.text_color
        color_down: root.text_color
        on_release: root.dispatch('on_plus')
        
        canvas.before:
            Color:
                rgba: root.color_down if self.state == 'down' else root.color_normal
            RoundedRectangle:
                radius: 0, root.height/4, root.height/4, 0
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
            action(self)

    def add_tab(self, text, action):
        tab = CupertinoSystemButton(
            text=text,
            color_normal=self.text_color,
            color_down=self.text_color,
            on_release=lambda b: self.__select(b, action)
        )
        self.add_widget(tab)
        self.__select(tab)


class CupertinoStepper(BoxLayout):
    color_normal = ColorProperty([0.95, 0.95, 0.95, 1])
    color_down = ColorProperty([0.8, 0.8, 0.8, 1])
    text_color = ColorProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_minus')
        self.register_event_type('on_plus')

    def on_minus(self):
        pass

    def on_plus(self):
        pass
