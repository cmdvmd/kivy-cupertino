"""
Showcase
========

.. codeauthor:: cmdvmd <vcmd43@gmail.com>

A program to display all widgets in Kivy Cupertino
"""

from kivycupertino.app import CupertinoApp
from kivycupertino.uix.bar import CupertinoNavigationBar, CupertinoTabBar, CupertinoTab
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.modal import CupertinoModalButton, CupertinoDialog, CupertinoActionSheet
from kivycupertino.uix.button import CupertinoSystemButton, CupertinoSymbolButton, CupertinoButton
from kivycupertino.uix.switch import CupertinoSwitch
from kivycupertino.uix.indicator import CupertinoActivityIndicator, CupertinoProgressbar
from kivycupertino.uix.control import CupertinoSegment, CupertinoSegmentedControls, CupertinoStepper
from kivycupertino.uix.slider import CupertinoSlider
from kivycupertino.uix.textinput import CupertinoSearchBar, CupertinoTextField, CupertinoTextView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class ShowcaseApp(CupertinoApp):
    @staticmethod
    def open_dialog():
        dialog = CupertinoDialog()
        dialog.size_hint = 0.8, 0.2

        dialog_title = CupertinoLabel()
        dialog_title.text = 'Alert Dialog'
        dialog_title.font_size = 15
        dialog_title.bold = True
        dialog_title.pos_hint = {'center_x': 0.5, 'top': 1.3}

        dialog_content = CupertinoLabel()
        dialog_content.text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque tincidunt ut magna quis placerat'
        dialog_content.font_size = 12
        dialog_content.halign = 'center'
        dialog_content.pos_hint = {'center_x': 0.5, 'top': 0.9}
        dialog_content.bind(
            width=lambda *args: dialog_content.setter('text_size')(dialog_content, (dialog_content.width - 20, None))
        )

        close_button = CupertinoModalButton()
        close_button.text = 'Close'
        close_button.on_release = dialog.dismiss

        dialog.add_widget(dialog_title)
        dialog.add_widget(dialog_content)
        dialog.add_widget(close_button)

        dialog.open()

    @staticmethod
    def open_action_sheet():
        action_sheet = CupertinoActionSheet()
        action_sheet.title = 'Action Sheet'
        action_sheet.message = 'This is an iOS style action sheet'

        action_button = CupertinoModalButton()
        action_button.text = 'Action'
        action_button.text_color = 1, 0, 0, 1

        sheet_button = CupertinoModalButton()
        sheet_button.text = 'Sheet'

        cancel_button = CupertinoModalButton()
        cancel_button.text = 'Cancel'
        cancel_button.cancel = True
        cancel_button.color_normal = 1, 1, 1, 1
        cancel_button.on_release = action_sheet.dismiss

        action_sheet.add_widget(action_button)
        action_sheet.add_widget(sheet_button)
        action_sheet.add_widget(cancel_button)

        action_sheet.open()

    def buttons(self):
        symbol_button = CupertinoSymbolButton()
        symbol_button.symbol = 'info_circle'
        symbol_button.color_normal = 0.05, 0.5, 0.95, 1
        symbol_button.color_down = 0, 0.15, 0.8, 1
        symbol_button.size_hint_y = 0.1
        symbol_button.pos_hint = {'center': (0.5, 0.8)}
        symbol_button.on_release = self.open_dialog

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
        button.on_release = lambda: setattr(activity_indicator, 'playing', not activity_indicator.playing)

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

        segmented_tab = CupertinoSegment()
        segmented_tab.text = 'Segmented'

        controls_tab = CupertinoSegment()
        controls_tab.text = 'Controls'

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
        slider.size_hint = 0.8, 0.075
        slider.pos_hint = {'center': (0.5, 0.45)}

        segmented_controls.add_widget(segmented_tab)
        segmented_controls.add_widget(controls_tab)

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
        instructions.text = 'Text View:'
        instructions.size_hint = 0.05, 0.1
        instructions.pos_hint = {'right': 0.175, 'center_y': 0.4}

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

        button_tab = CupertinoTab()
        button_tab.text = 'Buttons'
        button_tab.symbol = 'circle_grid_3x3_fill'

        controls_tab = CupertinoTab()
        controls_tab.text = 'Controls'
        controls_tab.symbol = 'wrench_fill'

        text_tab = CupertinoTab()
        text_tab.text = 'Text'
        text_tab.symbol = 'textformat_abc'

        navigation_bar.add_widget(title)

        tab_bar.add_widget(button_tab)
        tab_bar.add_widget(controls_tab)
        tab_bar.add_widget(text_tab)

        layout.add_widget(navigation_bar)
        layout.add_widget(self.contents)
        layout.add_widget(tab_bar)

        return layout


if __name__ == '__main__':
    Window.clearcolor = 0.98, 0.98, 0.98, 1
    Window.size = (300, 550)

    app = ShowcaseApp()
    app.run()
