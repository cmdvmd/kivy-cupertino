from kivy.properties import NumericProperty, StringProperty, ColorProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivycupertino.uix.label import CupertinoLabel
from kivy.lang.builder import Builder
from re import sub

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

<CupertinoAlertDialog>:
    actions: actions
    
    background: images_path+'transparent.png'
    background_color: 0, 0, 0, 0.5
    size_hint: 0.8, 0.3
    pos_hint: {'center': (0.5, 0.5)}
    
    canvas:
        Color:
            rgba: root.color
        RoundedRectangle:
            radius: root.curve,
            size: root.size
            pos: root.pos
            
    FloatLayout:
        size: root.size
        pos: root.pos
        
        CupertinoLabel:
            id: title
            text: root.title
            font_size: 15
            halign: 'center'
            bold: True
            text_size: self.width-20, None
            pos_hint: {'center_x': 0.5, 'top': 1.3}
        CupertinoLabel:
            id: content
            text: root.content
            font_size: 12
            halign: 'center'
            text_size: self.width-20, None
            pos_hint: {'center_x': 0.5}
            y: title.y-title.texture_size[1]-10
        BoxLayout:
            id: actions
            orientation: 'horizontal'
            spacing: 1
            padding: 0, 1, 0, 0
            size_hint_y: 0.25
            pos: root.pos
            
            canvas.before:
                Color:
                    rgb: 0.9, 0.9, 0.9
                RoundedRectangle:
                    radius: 0, 0, root.curve, root.curve
                    size: self.size
                    pos: self.pos
""")


class _CupertinoDialogButton(ButtonBehavior, CupertinoLabel):
    color_normal = ColorProperty([1, 1, 1, 0.5])
    color_down = ColorProperty([0.9, 0.9, 0.9, 0.5])
    text_color = ColorProperty([0.05, 0.5, 1, 1])
    radii = ListProperty([0, 0, 0, 0])


class CupertinoActionSheet(ModalView):
    curve = NumericProperty(10)
    
    def add_action(self, text, action):
        button = _CupertinoDialogButton(text=text, on_release=action)
        self.actions.size_hint_y += 0.1
        self.actions.add_widget(button, len(self.actions.children))

        self.actions.children[0].radii = (0, 0, self.curve, self.curve)
        self.actions.children[-1].radii[:2] = (self.curve, self.curve)

        for b in self.actions.children[1:-1]:
            b.radii = (0, 0, 0, 0)


class CupertinoAlertDialog(ModalView):
    title = StringProperty('')
    content = StringProperty('')
    color = ColorProperty([1, 1, 1, 0.95])
    color_pressed = ColorProperty([0.9, 0.9, 0.9, 1])
    curve = NumericProperty(10)

    def add_action(self, text, action):
        self.actions.add_widget(_CupertinoDialogButton(
            text=text,
            on_release=action,
            color_normal=self.color,
            color_down=self.color_pressed
        ))

        if len(self.actions.children) > 2 or len(sub(r'\[.*?\]', '', text)) > 10:
            self.actions.orientation = 'vertical'

        if self.actions.orientation == 'vertical':
            self.size_hint_y += 0.05
            self.actions.size_hint_y += 0.05

            self.actions.children[0].radii[-2:] = [self.curve, self.curve]
            for button in self.actions.children[1:]:
                button.radii = [0, 0, 0, 0]
        else:
            self.actions.children[-1].radii[-2:] = (0, self.curve)
            self.actions.children[0].radii[2] = self.curve
