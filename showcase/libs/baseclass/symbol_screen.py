from json import load

from kivy.uix.screenmanager import Screen
from kivycupertino import root_path
from libs.components.symbol_list_item import SymbolListItem


class SymbolShowcaseScreen(Screen):

    loaded = False

    def on_pre_enter(self):
        if not self.loaded:
            with open(root_path + "/data/symbols.json", "r") as json:
                symbols = load(json)

            for s in symbols:
                item = SymbolListItem(text=s, symbol=s)
                self.ids.box.add_widget(item)
            self.loaded = True
