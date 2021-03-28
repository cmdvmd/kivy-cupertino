"""
Symbols
=======

A program to show all symbols in Kivy Cupertino
"""

from kivycupertino.uix.scrollview import CupertinoScrollView
from kivycupertino import root_path
from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.symbol import CupertinoSymbol
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from json import load


class SymbolsApp(CupertinoApp):
    def build(self):
        box = BoxLayout()
        box.orientation = 'vertical'

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.size_hint_y = 0.15

        title = CupertinoLabel()
        title.text = 'Symbols'
        title.bold = True
        title.pos_hint = {'center': (0.5, 0.5)}

        scrollview = CupertinoScrollView()

        layout = GridLayout()
        layout.cols = 1
        layout.spacing = 15
        layout.padding = 15
        layout.size_hint_y = None
        layout.bind(
            minimum_height=layout.setter('height')
        )

        navigation_bar.add_widget(title)

        scrollview.add_widget(layout)

        with open(root_path+'symbols.json', 'r') as json:
            symbols = load(json)

        for s in symbols:
            cell = BoxLayout()
            cell.orientation = 'horizontal'
            cell.size_hint_y = None
            cell.height = 20

            symbol = CupertinoSymbol()
            symbol.symbol = s
            symbol.color = 0, 0, 0, 1
            symbol.size_hint_x = 0.3

            name = CupertinoLabel()
            name.text = s
            name.halign = 'left'
            name.bind(
                size=name.setter('text_size')
            )

            cell.add_widget(symbol)
            cell.add_widget(name)

            layout.add_widget(cell)

        box.add_widget(navigation_bar)
        box.add_widget(scrollview)

        return box


Window.clearcolor = (0.98, 0.98, 0.98, 1)
Window.size = (300, 500)

if __name__ == '__main__':
    app = SymbolsApp()
    app.run()
