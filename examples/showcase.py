"""
Showcase
========

A program to show all widgets in Kivy Cupertino
"""

__author__ = 'Eduardo Mendes'  # dunossauro on GitHub <https://github.com/dunossauro>
__maintainer__ = 'cmdvmd'

from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar, CupertinoTabBar
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.dialog import CupertinoAlertDialog, CupertinoActionSheet
from kivycupertino.uix.button import CupertinoSystemButton, CupertinoSymbolButton, CupertinoButton
from kivycupertino.uix.switch import CupertinoSwitch
from kivycupertino.uix.indicator import CupertinoActivityIndicator, CupertinoProgressbar
from kivycupertino.uix.control import CupertinoSegmentedControls, CupertinoStepper
from kivycupertino.uix.slider import CupertinoSlider
from kivycupertino.uix.textinput import CupertinoSearchBar, CupertinoTextField, CupertinoTextView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class ShowcaseApp(CupertinoApp):
    @staticmethod
    def open_alert_dialog():
        alert_dialog = CupertinoAlertDialog()
        alert_dialog.title = 'Alert Dialog'
        alert_dialog.content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                               'Quisque tincidunt ut magna quis placerat'
        alert_dialog.add_action('Close', alert_dialog.dismiss)
        alert_dialog.open()

    @staticmethod
    def open_action_sheet():
        action_sheet = CupertinoActionSheet()
        action_sheet.add_action('Sheet', action_sheet.dismiss)
        action_sheet.add_action('[color=ff0000]Action[/color]', action_sheet.dismiss)
        action_sheet.open()

    def buttons(self):
        symbol_button = CupertinoSymbolButton()
        symbol_button.symbol = 'info'
        symbol_button.color = 0.05, 0.5, 0.95, 1
        symbol_button.size_hint = 0.15, 0.1
        symbol_button.pos_hint = {'center': (0.5, 0.8)}
        symbol_button.on_release = self.open_alert_dialog

        system_button = CupertinoSystemButton()
        system_button.text = 'Open Action Sheet'
        system_button.size_hint = 0.5, 0.1
        system_button.pos_hint = {'center': (0.5, 0.65)}
        system_button.on_release = self.open_action_sheet

        activity_indicator = CupertinoActivityIndicator()
        activity_indicator.size_hint = 0.1, 0.1
        activity_indicator.pos_hint = {'center': (0.5, 0.2)}

        button = CupertinoButton()
        button.text = 'Toggle Activity Indicator'
        button.size_hint = 0.8, 0.1
        button.pos_hint = {'center': (0.5, 0.5)}
        button.on_release = activity_indicator.toggle

        switch = CupertinoSwitch()
        switch.size_hint = 0.25, 0.1
        switch.pos_hint = {'center': (0.5, 0.35)}

        self.contents.add_widget(system_button)
        self.contents.add_widget(symbol_button)
        self.contents.add_widget(button)
        self.contents.add_widget(switch)
        self.contents.add_widget(activity_indicator)

    def update_progressbar(self, value):
        self.progressbar.value += value

    def controls(self):
        segmented_controls = CupertinoSegmentedControls()
        segmented_controls.size_hint = 0.7, 0.075
        segmented_controls.pos_hint = {'center': (0.5, 0.9)}
        segmented_controls.add_tab('Segmented')
        segmented_controls.add_tab('Controls')

        self.progressbar = CupertinoProgressbar()
        self.progressbar.size_hint = 0.95, 0.01
        self.progressbar.value = 10
        self.progressbar.pos_hint = {'center': (0.5, 0.65)}

        stepper = CupertinoStepper()
        stepper.size_hint = 0.2, 0.075
        stepper.pos_hint = {'right': 0.25, 'center_y': 0.55}
        stepper.bind(
            on_plus=lambda w: self.update_progressbar(10),
            on_minus=lambda w: self.update_progressbar(-10)
        )

        slider = CupertinoSlider()
        slider.size_hint = 0.8, 0.1
        slider.pos_hint = {'center': (0.5, 0.45)}

        self.contents.add_widget(segmented_controls)
        self.contents.add_widget(self.progressbar)
        self.contents.add_widget(stepper)
        self.contents.add_widget(slider)

    def text(self):
        ny_font = CupertinoLabel()
        ny_font.text = 'New York Font'
        ny_font.font_name = 'New York'
        ny_font.pos_hint = {'center': (0.5, 0.9)}

        sf_font = CupertinoLabel()
        sf_font.text = 'San Francisco Font'
        sf_font.font_name = 'San Francisco'
        sf_font.pos_hint = {'center': (0.5, 0.8)}

        search_bar = CupertinoSearchBar()
        search_bar.size_hint = 0.9, 0.075
        search_bar.pos_hint = {'center': (0.5, 0.65)}

        text_field = CupertinoTextField()
        text_field.hint_text = 'Text Field'
        text_field.size_hint = 0.9, 0.075
        text_field.pos_hint = {'center': (0.5, 0.5)}

        instructions = CupertinoLabel()
        instructions.text = 'Enter text below:'
        instructions.size_hint = 0.05, 0.1
        instructions.pos_hint = {'right': 0.25, 'center_y': 0.4}

        text_view = CupertinoTextView()
        text_view.size_hint = 0.95, 0.35
        text_view.pos_hint = {'center_x': 0.5, 'top': 0.35}

        self.contents.add_widget(ny_font)
        self.contents.add_widget(sf_font)
        self.contents.add_widget(search_bar)
        self.contents.add_widget(text_field)
        self.contents.add_widget(instructions)
        self.contents.add_widget(text_view)

    def change_screen(self, widget, screen):
        self.contents.clear_widgets()
        if screen == 'Buttons':
            self.buttons()
        elif screen == 'Controls':
            self.controls()
        elif screen == 'Text':
            self.text()

    def build(self):
        layout = BoxLayout()
        layout.orientation = 'vertical'

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.size_hint_y = 0.15

        title = CupertinoLabel()
        title.text = 'Showcase'
        title.bold = True
        title.pos_hint = {'center': (0.5, 0.5)}

        self.contents = FloatLayout()

        tab_bar = CupertinoTabBar()
        tab_bar.size_hint_y = 0.1
        tab_bar.bind(selected=self.change_screen)
        tab_bar.add_tab('Buttons', 'keypad_fill')
        tab_bar.add_tab('Controls', 'wrench_fill')
        tab_bar.add_tab('Text', 'abc')

        navigation_bar.add_widget(title)

        layout.add_widget(navigation_bar)
        layout.add_widget(self.contents)
        layout.add_widget(tab_bar)

        return layout


Window.clearcolor = 0.98, 0.98, 0.98, 1
Window.size = (300, 500)

if __name__ == '__main__':
    app = ShowcaseApp()
    app.run()
