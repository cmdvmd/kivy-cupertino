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
    A :class:`~kivy.properties.StringProperty` defining the text of hint of
    :class:`kivycupertino.uix.textfield.CupertinoTextField`
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`kivycupertino.uix.textfield.CupertinoTextField`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`kivycupertino.uix.textfield.CupertinoTextField`
    """


class CupertinoTextView(TextInput):
    """
    iOS style Text View for multiline input

    .. image:: ../_static/text_view.gif
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`kivycupertino.uix.textfield.CupertinoTextView`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`kivycupertino.uix.textfield.CupertinoTextView`
    """
