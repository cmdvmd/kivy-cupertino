"""
Symbols help portray an action with a simple symbol. To view all symbols in Kivy Cupertino,
visit `Framework7 <https://framework7.io/icons/>`_ or run the :download:`Symbols program <../../examples/symbols.py>`
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

    .. image:: ../_static/symbol/demo.png
    """

    symbol = StringProperty(' ')
    """
    Symbol to be displayed by :class:`CupertinoSymbol`.
    
    .. image:: ../_static/symbol/symbol.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbol(symbol='alarm_fill')
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbol:
           symbol: 'alarm_fill'
    """

    color = ColorProperty([0, 0, 0, 1])
    """
    Color of :class:`CupertinoSymbol`
    
    .. image:: ../_static/symbol/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSymbol(color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSymbol:
           color: 1, 0, 0, 1
    """

    def on_symbol(self, instance, symbol):
        """
        Callback when symbol of :class:`~kivy.uix.symbol.CupertinoSymbol` is changed

        :param instance: Instance of :class:`CupertinoSymbol`
        :param symbol: Symbol to be displayed
        """

        with open(root_path + 'symbols.json', 'r') as json:
            symbols = load(json)
        self.text = chr(symbols[symbol]) if symbol != ' ' else '\u2800'
