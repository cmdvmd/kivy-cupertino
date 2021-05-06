"""
Text fields allow users to enter input
"""

from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoTextField',
    'CupertinoTextView',
    'CupertinoSearchBar'
]

Builder.load_string("""
<CupertinoTextField>:
    password_mask: '•'
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
    password: False
    cursor_width: '2sp'
    cursor_color: 0.25, 0.5, 0.95, 1
    font_name: 'San Francisco'

<CupertinoSearchBar>:
    orientation: 'horizontal'
    padding: 5, 0
    
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            radius: self.height/4,
            size: self.size
            pos: self.pos
    
    CupertinoSymbol:
        symbol: 'search'
        color: root.symbol_color
        size_hint_x: 0.05
    TextInput:
        id: textfield
        multiline: False
        password: False
        cursor_width: '2sp'
        cursor_color: 0.25, 0.5, 0.95, 1
        hint_text: 'Search'
        font_size: root.height/2.5
        font_name: 'San Francisco'
        background_color: 0, 0, 0, 0
        foreground_color: root.foreground_color
    CupertinoSymbolButton:
        symbol: 'xmark_circle_fill' if textfield.text else ' '
        color_normal: root.symbol_color
        color_down: 0, 0, 0, 0
        on_release: textfield.text = ''
        size_hint_x: 0.05
""")


class CupertinoTextField(TextInput):
    """
    iOS style Text Field to be used for single-line input

    .. image:: ../_static/text_field/demo.gif
    """

    hint_text = StringProperty('')
    """
    Text of hint of :class:`CupertinoTextField`
    
    .. image:: ../_static/text_field/hint_text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(hint_text='Hello World')
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           hint_text: 'Hello World'
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`CupertinoTextField`
    
    .. image:: ../_static/text_field/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(background_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           background_color: 0.5, 0, 0, 1
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`CupertinoTextField`
    
    .. image:: ../_static/text_field/foreground_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(foreground_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           foreground_color: 1, 0, 0, 1
    """


class CupertinoTextView(TextInput):
    """
    iOS style Text View for multiline input

    .. image:: ../_static/text_view/demo.gif
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`CupertinoTextView`
    
    .. image:: ../_static/text_view/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(background_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           background_color: 0.5, 0, 0, 1
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`CupertinoTextView`
    
    .. image:: ../_static/text_view/foreground_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(foreground_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           foreground_color: 1, 0, 0, 1
    """


class CupertinoSearchBar(BoxLayout):
    """
    iOS style search bar

    .. image:: ../_static/search_bar/demo.gif
    """

    background_color = ColorProperty([0.85, 0.85, 0.85, 0.7])
    """
    Background color of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(background_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           background_color: 1, 0, 0, 1
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/foreground_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(foreground_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           foreground_color: 1, 0, 0, 1
    """

    symbol_color = ColorProperty([0.55, 0.55, 0.6, 1])
    """
    Color of the symbols of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/symbol_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(symbol_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           symbol_color: 1, 0, 0, 1
    """
