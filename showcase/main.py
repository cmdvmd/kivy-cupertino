import ast
import os

import kivycupertino
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivycupertino.app import CupertinoApp

Factory.register("TopBar", module="libs.components.topbar")


class CupertinoApp(CupertinoApp):
    def build(self):
        Window.clearcolor = 0.98, 0.98, 0.98, 1
        return ScreenManager()

    def on_start(self):
        with open(os.path.join("screens.json")) as read_file:
            self.screens_data = ast.literal_eval(read_file.read())
            screens_data = list(self.screens_data.keys())
            screens_data.sort()
        self.set_screen("home")

        for i in list(self.screens_data):
            if not i == "Home":
                self.root.get_screen("home").ids.rv.data.append(
                    {
                        "text": i,
                        "on_release": lambda x=self.screens_data[i][
                            "screen_name"
                        ]: self.set_screen(x),
                    }
                )

    def set_screen(self, screen_name):
        for i in list(self.screens_data):
            if screen_name in self.screens_data[i]["screen_name"]:
                screen_data = self.screens_data[i]
                break

        if not self.root.has_screen(screen_name):
            Builder.load_file(
                os.path.join("libs", "kv", f"{screen_data['screen_name']}_screen.kv")
            )
            exec(screen_data["import"])
            screen_object = eval(screen_data["factory"])
            screen_object.name = screen_name
            self.root.add_widget(screen_object)
            if "topbar" in screen_object.ids:
                screen_object.ids.topbar.title = screen_name.title()

        self.root.transition.direction = "left"
        self.root.current = screen_name


if __name__ == "__main__":
    CupertinoApp().run()
