"""
A program to test all widgets in KivyCupertino
"""


__author__ = 'Eduardo Mendes'  # dunossauro on GitHub <https://github.com/dunossauro>

from functools import partial
from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.button import CupertinoButton, CupertinoSystemButton
from kivycupertino.uix.dialog import CupertinoAlertDialog, CupertinoActionSheet
from kivycupertino.uix.switch import CupertinoSwitch
from kivycupertino.uix.indicator import CupertinoProgressBar
from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class MyApp(CupertinoApp):
    def alert(self):
        alert = CupertinoAlertDialog()
        alert.title = 'Alert!'
        alert.content = 'Yes, this a alert!'
        alert.add_action('Action!', alert.dismiss)
        alert.open()

    def action(self):
        action = CupertinoActionSheet()
        action.add_action('Close', action.dismiss)
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

        btn = CupertinoButton(text='Button')
        btn.size_hint = 0.8, 0.06
        btn.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        btn.on_release = self.alert

        sys_btn = CupertinoSystemButton(text='SystemButton')
        sys_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.4}
        sys_btn.size_hint_y = 0.06
        sys_btn.on_release = self.action

        self.progress = CupertinoProgressBar()
        self.progress.size_hint = 0.8, 0.01
        self.progress.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        self.progress.value = 50

        progress_btn1 = CupertinoSystemButton(text='-')
        progress_btn1.size_hint = 0.1, 0.06
        progress_btn1.pos_hint = {'center_x': 0.25, 'center_y': 0.25}
        progress_btn1.on_release = partial(self.update_progress, -10)

        progress_btn2 = CupertinoSystemButton(text='+')
        progress_btn2.size_hint = 0.1, 0.06
        progress_btn2.pos_hint = {'center_x': 0.75, 'center_y': 0.25}
        progress_btn2.on_release = partial(self.update_progress, 10)

        switch = CupertinoSwitch()
        switch.size_hint = 0.1, 0.06
        switch.pos_hint = {'center_x': 0.5, 'center_y': 0.2}

        fl.add_widget(navigation_bar)
        fl.add_widget(label)
        fl.add_widget(btn)
        fl.add_widget(sys_btn)
        fl.add_widget(self.progress)
        fl.add_widget(progress_btn1)
        fl.add_widget(progress_btn2)
        fl.add_widget(switch)

        return fl


Window.clearcolor = 0.98, 0.98, 0.98, 1
app = MyApp()
app.run()
