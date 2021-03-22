"""
Symbols help portray an action with a simple symbol. To test all symbols
in Kivy Cupertino, run the Symbols program (below)

:download:`Symbols <../../examples/symbols.py>`

.. include:: ../../examples/symbols.py
   :literal:
"""

from kivycupertino import root_path
from kivy.uix.label import Label
from kivy.properties import StringProperty, ColorProperty
from kivy.lang.builder import Builder
from json import load

__all__ = [
    'CupertinoSymbol'
]

Builder.load_string("""
<CupertinoSymbol>:
    font_name: 'SF Symbols'
    font_size: min(self.size)
""")


class CupertinoSymbol(Label):
    """
    Display an iOS style symbol.

    .. image:: ../_static/symbol.png
    """

    symbol = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the symbol to be displayed by
    :class:`~kivycupertino.uix.icon.CupertinoSymbol`.
    """

    color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.icon.CupertinoSymbol`
    """

    def on_symbol(self, widget, symbol):
        with open(root_path + 'symbols.json', 'r') as json:
            symbols = load(json)
        self.text = chr(eval(symbols[symbol]))
