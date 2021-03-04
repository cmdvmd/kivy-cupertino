from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string("""
<CupertinoTextField>:
    multiline: False
    cursor_width: '2sp'
    cursor_color: 0.25, 0.5, 0.95, 1
    font_name: 'San Francisco'
    
    canvas.after:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            size: self.width, 2
            pos: self.pos

<CupertinoTextView>:
    multiline: True
    cursor_width: '2sp'
    cursor_color: 0.25, 0.5, 0.95, 1
    font_name: 'San Francisco'
    hint_text: ''
""")


class CupertinoTextField(TextInput):
    hint_text = StringProperty('')
    background_color = ColorProperty([0, 0, 0, 0])
    foreground_color = ColorProperty([0, 0, 0, 1])


class CupertinoTextView(TextInput):
    background_color = ColorProperty([0, 0, 0, 0])
    foreground_color = ColorProperty([0, 0, 0, 1])
