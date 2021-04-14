from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_string("""
<TopBar>
    size_hint_y: None
    height: self.minimum_height
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            size: self.size
            pos: self.pos

    CupertinoBackButton:
        size_hint: None, None
        on_release:
            app.root.transition.direction = 'right'
            app.root.current = 'home'

    CupertinoLabel:
        text: root.title
        pos_hint: {'center_y': .5}
        bold: True
        size_hint_y: None
        height: self.texture_size[1]
        font_size: sp(25)
""")


class TopBar(BoxLayout):
    title = StringProperty()
