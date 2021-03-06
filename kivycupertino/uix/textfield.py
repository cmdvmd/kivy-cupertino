"""
Text fields allow users to enter input
"""

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
    """
    iOS style Text Field to be used for single-line input

    .. image:: ../_static/text_field.gif
    """

    hint_text = StringProperty('')
    """
    Text of hint of :class:`kivycupertino.uix.textfield.CupertinoTextField`
    
    :attr:`hint_text` is a :class:`~kivy.properties.StringProperty` and defaults to `""`
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`kivycupertino.uix.textfield.CupertinoTextField`
    
    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 0]`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`kivycupertino.uix.textfield.CupertinoTextField`
    
    :attr:`foreground_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 1]`
    """


class CupertinoTextView(TextInput):
    """
    iOS style Text View for multiline input

    .. image:: ../_static/text_view.gif
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`kivycupertino.uix.textfield.CupertinoTextView`
    
    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 0]`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`kivycupertino.uix.textfield.CupertinoTextView`
    
    :attr:`foreground_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 1]`
    """
