"""
Symbols
=======

.. codeauthor:: cmdvmd <vcmd43@gmail.com>

A program to show all symbols in Kivy Cupertino
"""

from kivycupertino import root_path
from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from json import load

Builder.load_string("""
<RV>:
    viewclass: 'Symbol'
    
    RecycleBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(5)
        default_size: None, dp(20)
        default_size_hint: 1, None
        size_hint_y: None
        height: dp(self.minimum_height)

<Symbol>:
    orientation: 'horizontal'
    spacing: dp(10)
    
    CupertinoSymbol:
        symbol: root.symbol
        color: 0, 0, 0, 1
        size_hint_x: 0.1
    CupertinoLabel:
        text: root.symbol
        font_size: '14sp'
        halign: 'left'
        text_size: self.size
""")


class RV(RecycleView):
    pass


class Symbol(BoxLayout):
    symbol = StringProperty(' ')


class SymbolsApp(CupertinoApp):
    def build(self):
        with open(root_path + 'symbols.json', 'r') as json:
            symbols = load(json)

        box = BoxLayout()
        box.orientation = 'vertical'

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.size_hint_y = 0.15

        title = CupertinoLabel()
        title.text = 'Symbols'
        title.bold = True
        title.pos_hint = {'center': (0.5, 0.5)}

        rv = RV()
        rv.data = [{'symbol': symbol} for symbol in symbols]

        navigation_bar.add_widget(title)
        box.add_widget(navigation_bar)
        box.add_widget(rv)

        return box


if __name__ == '__main__':
    Window.clearcolor = (0.98, 0.98, 0.98, 1)
    Window.size = (300, 530)
    app = SymbolsApp()
    app.run()
