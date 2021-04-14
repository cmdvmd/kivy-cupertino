from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
    """
<SymbolListItem>
    size_hint_y: None
    padding: dp(20)

    CupertinoSymbol:
        symbol: root.symbol

    CupertinoLabel:
        text: root.text
		font_size: '20sp'
"""
)


class SymbolListItem(BoxLayout):
    symbol = StringProperty()
    text = StringProperty()
