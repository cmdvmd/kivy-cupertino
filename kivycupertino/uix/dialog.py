from kivycupertino.uix.button import CupertinoDialogButton
from kivy.uix.modalview import ModalView
from kivy.properties import NumericProperty
from kivy.lang.builder import Builder

Builder.load_string("""
#: import images_path kivycupertino.__init__.images_path

<CupertinoActionSheet>:
    actions: actions
    
    background: images_path+'transparent.png'
    background_color: 0, 0, 0, 0.5
    auto_dismiss: False
    size_hint_x: 0.95
    pos_hint: {'center_x': 0.5}
    
    FloatLayout:
        size: root.size
        pos: root.pos
        
        BoxLayout:
            id: actions
            orientation: 'vertical'
            spacing: 2
            size_hint_y: 0
            pos_hint: {'center_x': 0.5}
            y: cancel.y+cancel.height+10
            
            canvas.before:
                Color:
                    rgb: 0.9, 0.9, 0.9
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
        CupertinoButton:
            id: cancel
            text: 'Cancel'
            text_color: 0.05, 0.5, 1
            color_normal: 1, 1, 1, 1
            color_down: 0.9, 0.9, 0.9, 1
            size_hint_y: 0.09
            pos_hint: {'center_x': 0.5, 'y': 0.02}
            on_release: root.dismiss()
""")


class CupertinoActionSheet(ModalView):
    curve = NumericProperty(10)
    
    def add_action(self, text, action):
        button = CupertinoDialogButton(text=text, on_release=action)
        self.actions.size_hint_y += 0.1
        self.actions.add_widget(button, len(self.actions.children))

        self.actions.children[0].radii = (0, 0, self.curve, self.curve)
        self.actions.children[-1].radii[:2] = (self.curve, self.curve)

        for b in self.actions.children[1:-1]:
            b.radii = (0, 0, 0, 0)
