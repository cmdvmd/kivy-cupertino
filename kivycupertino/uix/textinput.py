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
    cursor_color: root.cursor_color
    font_name: 'San Francisco'
    
    canvas.after:
        Color:
            rgb: 0.95, 0.95, 0.95
        Rectangle:
            size: dp(self.width), dp(2)
            pos: self.pos

<CupertinoTextView>:
    multiline: True
    password: False
    cursor_width: '2sp'
    cursor_color: root.cursor_color
    font_name: 'San Francisco'

<CupertinoSearchBar>:
    orientation: 'horizontal'
    padding: dp(5), dp(0)
    
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            radius: dp(self.height/4),
            size: self.size
            pos: self.pos
    
    CupertinoSymbol:
        symbol: 'search'
        color: root.symbol_color
        size_hint_x: 0.06
        pos_hint: {'center_y': 0.5}
    TextInput:
        multiline: False
        cursor_width: '2sp'
        cursor_color: root.cursor_color
        text: root.text
        hint_text: root.hint_text
        font_size: (0.8 * min(self.size)) - 9
        font_name: 'San Francisco'
        background_color: 0, 0, 0, 0
        foreground_color: root.foreground_color
        on_text: root.text = self.text
        pos_hint: {'center_y': 0.5}
    CupertinoSymbolButton:
        symbol: 'xmark_circle_fill' if root.text else ' '
        color_normal: root.symbol_color
        color_down: root.color_down
        on_release: root.text = ''
        size_hint_x: 0.05
        pos_hint: {'center_y': 0.5}
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

    cursor_color = ColorProperty([0.25, 0.5, 0.95, 1])
    """
    Color of cursor of :class:`CupertinoTextField`
    
    .. image:: ../_static/text_field/cursor_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextField(cursor_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextField:
           cursor_color: 1, 0, 0, 1
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

    cursor_color = ColorProperty([0.25, 0.5, 0.95, 1])
    """
    Color of cursor of :class:`CupertinoTextView`
    
    .. image:: ../_static/text_view/cursor_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTextView(background_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoTextView:
           background_color: 0.5, 0, 0, 1
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

    text = StringProperty('')
    """
    Text of :class:`CupertinoTextField`
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(text='Hello World')
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           text: 'Hello World'
    """

    hint_text = StringProperty('Search')
    """
    Text of hint of :class:`CupertinoTextField`
    
    .. image:: ../_static/search_bar/hint_text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(hint_text='Hello World')
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           hint_text: 'Hello World'
    """

    cursor_color = ColorProperty([0.25, 0.5, 0.95, 1])
    """
    Color of cursor of :class:`CupertinoTextView`
    
    .. image:: ../_static/search_bar/cursor_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(background_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           background_color: 0.5, 0, 0, 1
    """

    background_color = ColorProperty([0.85, 0.85, 0.85, 0.7])
    """
    Background color of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(background_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           background_color: 1, 0, 0, 1
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/foreground_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(foreground_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           foreground_color: 1, 0, 0, 1
    """

    symbol_color = ColorProperty([0.55, 0.55, 0.6, 1])
    """
    Color of the symbols of :class:`CupertinoSearchBar`
    
    .. image:: ../_static/search_bar/symbol_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(symbol_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           symbol_color: 1, 0, 0, 1
    """

    color_down = ColorProperty([0.4, 0.4, 0.4, 1])
    """
    Color of the clear button of :class:`CupertinoSearchBar` when pressed
    
    .. image:: ../_static/search_bar/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSearchBar(color_down=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSearchBar:
           color_down: 0.5, 0, 0, 1
    """
