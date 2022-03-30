"""
Symbols
=======

.. codeauthor:: cmdvmd <vcmd43@gmail.com>

A program to show all symbols in Kivy Cupertino. Symbols can be searched for
using Regular Expression syntax or keywords
"""

from kivycupertino import root_path
from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.textinput import CupertinoSearchBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.lang.builder import Builder
from json import load
from re import findall, error

Builder.load_string("""
#: import sub re.sub

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
        markup: False
        symbol: sub('\\[.*?\\]', '', root.symbol)
        color: 0, 0, 0, 1
        size_hint_x: 0.1
    CupertinoLabel:
        markup: True
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
    def add_symbols(self, pattern):
        pattern = pattern.lower().strip().replace(' ', '_')

        with open(root_path + 'symbols.json', 'r') as json:
            symbols = load(json)

        data = []

        try:
            for symbol in symbols:
                if match := findall(pattern, symbol):
                    data.append({'symbol': symbol.replace(match[0], f'[b]{match[0]}[/b]')})
        except error:
            pass

        self.rv.data = data

    def build(self):
        box = BoxLayout()
        box.orientation = 'vertical'
        box.spacing = 7

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.size_hint_y = 0.15

        title = CupertinoLabel()
        title.text = 'Symbols'
        title.bold = True
        title.pos_hint = {'center': (0.5, 0.5)}

        search_bar = CupertinoSearchBar()
        search_bar.size_hint = 0.9, 0.06
        search_bar.pos_hint = {'center_x': 0.5}
        search_bar.bind(text=lambda instance, text: self.add_symbols(text))

        self.rv = RV()

        navigation_bar.add_widget(title)
        box.add_widget(navigation_bar)
        box.add_widget(search_bar)
        box.add_widget(self.rv)

        self.add_symbols('')

        return box


if __name__ == '__main__':
    Window.clearcolor = (0.98, 0.98, 0.98, 1)
    Window.size = (300, 530)
    app = SymbolsApp()
    app.run()
