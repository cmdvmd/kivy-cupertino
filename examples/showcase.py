"""
Showcase
========
A program to test all widgets in Kivy Cupertino
"""

__author__ = 'Eduardo Mendes'  # dunossauro on GitHub <https://github.com/dunossauro>
__maintainer__ = 'cmdvmd'

from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.button import CupertinoButton, CupertinoSystemButton
from kivycupertino.uix.dialog import CupertinoAlertDialog, CupertinoActionSheet
from kivycupertino.uix.indicator import CupertinoProgressbar
from kivycupertino.uix.control import CupertinoStepper
from kivycupertino.uix.switch import CupertinoSwitch
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class MyApp(CupertinoApp):
    def alert(self):
        alert = CupertinoAlertDialog()
        alert.title = 'Alert!'
        alert.content = 'This an Alert Dialog!'
        alert.add_action('Close', alert.dismiss)
        alert.open()

    def action(self):
        action = CupertinoActionSheet()
        action.add_action('Action', action.dismiss)
        action.open()

    def update_progress(self, amount):
        self.progress.value += amount

    def build(self):
        fl = FloatLayout()

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.size_hint_y = 0.1
        navigation_bar.pos_hint = {'center_x': 0.5, 'top': 1}

        title = CupertinoLabel(text='Navigation Bar')
        title.bold = True
        title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        navigation_bar.add_widget(title)

        label = CupertinoLabel(text='Label')
        label.pos_hint = {'center_x': 0.5, 'center_y': 0.6}

        sys_btn = CupertinoSystemButton(text='System Button to open Action Sheet')
        sys_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
        sys_btn.size_hint_y = 0.06
        sys_btn.on_release = self.action

        btn = CupertinoButton(text='Button to open Alert Dialog')
        btn.size_hint = 0.8, 0.06
        btn.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        btn.on_release = self.alert

        self.progress = CupertinoProgressbar()
        self.progress.size_hint = 0.7, 0.01
        self.progress.pos_hint = {'x': 0.05, 'center_y': 0.3}
        self.progress.value = 50

        stepper = CupertinoStepper()
        stepper.bind(on_plus=lambda x: self.update_progress(5), on_minus=lambda x: self.update_progress(-5))
        stepper.size_hint = 0.1, 0.05
        stepper.pos_hint = {'x': 0.8, 'center_y': 0.3}

        switch = CupertinoSwitch()
        switch.size_hint = 0.1, 0.06
        switch.pos_hint = {'center_x': 0.5, 'center_y': 0.2}

        fl.add_widget(navigation_bar)
        fl.add_widget(label)
        fl.add_widget(sys_btn)
        fl.add_widget(btn)
        fl.add_widget(self.progress)
        fl.add_widget(stepper)
        fl.add_widget(switch)

        return fl


Window.clearcolor = 0.98, 0.98, 0.98, 1
app = MyApp()
app.run()