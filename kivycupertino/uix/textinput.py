"""
Text fields allow users to enter input

Usage:
------

**Cupertino Search Bar**

.. image:: ../../_static/search_bar.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.textinput import CupertinoSearchBar
    from kivy.uix.floatlayout import FloatLayout


    class TestApp(CupertinoApp):

        def build(self):
            layout = FloatLayout()

            search_bar = CupertinoSearchBar(size_hint=[0.9, 0.075], pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(search_bar)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

**Cupertino Text Field**

.. image:: ../../_static/text_field.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.textinput import CupertinoTextField
    from kivy.uix.floatlayout import FloatLayout


    class TestApp(CupertinoApp):

        def build(self):
            layout = FloatLayout()

            text = CupertinoTextField(hint_text='Hint', size_hint=[0.9, 0.075], pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(text)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

**Cupertino Text View**

.. image:: ../../_static/text_view.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.textinput import CupertinoTextView
    from kivy.uix.floatlayout import FloatLayout


    class TestApp(CupertinoApp):

        def build(self):
            layout = FloatLayout()

            text = CupertinoTextView(size_hint=[0.9, 0.075], pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(text)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

Api:
-----
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
    hint_text: ''

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
        symbol_color: root.symbol_color
        background_down: 0, 0, 0, 0
        on_release: textfield.text = ''
        size_hint_x: 0.05
""")


class CupertinoTextField(TextInput):
    """
    iOS style Text Field to be used for single-line input
    """

    hint_text = StringProperty('')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of hint of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextField`
    """


class CupertinoTextView(TextInput):
    """
    iOS style Text View for multiline input
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextView`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoTextView`
    """


class CupertinoSearchBar(BoxLayout):
    """
    iOS style search bar
    """

    background_color = ColorProperty([0.85, 0.85, 0.85, 0.7])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """

    foreground_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the text color of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """

    symbol_color = ColorProperty([0.55, 0.55, 0.6, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the symbols of
    :class:`~kivycupertino.uix.textfield.CupertinoSearchBar`
    """
