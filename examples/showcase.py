"""
Showcase
========

A program to show all widgets in Kivy Cupertino
"""

__author__ = 'Eduardo Mendes'  # dunossauro on GitHub <https://github.com/dunossauro>
__maintainer__ = 'cmdvmd'

from kivycupertino.app import CupertinoApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.bar import CupertinoNavigationBar
from kivycupertino.uix.button import CupertinoSystemButton, CupertinoIconButton, CupertinoButton
from kivycupertino.uix.switch import CupertinoSwitch
from kivycupertino.uix.indicator import CupertinoProgressbar
from kivycupertino.uix.control import CupertinoSegmentedControls, CupertinoStepper
from kivycupertino.uix.dialog import CupertinoAlertDialog, CupertinoActionSheet
from kivycupertino.uix.textfield import CupertinoTextField, CupertinoTextView


class ShowcaseApp(CupertinoApp):
    def increment_progress(self, amount):
        self.progress_bar.value += amount

    @staticmethod
    def open_alert_dialog():
        alert_dialog = CupertinoAlertDialog()
        alert_dialog.title = 'Alert Dialog'
        alert_dialog.content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in pulvinar lorem'
        alert_dialog.add_action('Close', alert_dialog.dismiss)
        alert_dialog.open()

    @staticmethod
    def open_action_sheet():
        action_sheet = CupertinoActionSheet()
        action_sheet.add_action('Save', action_sheet.dismiss)
        action_sheet.add_action('[color=ff0000]Delete[/color]', action_sheet.dismiss)
        action_sheet.open()

    def build(self):
        box = BoxLayout()
        box.orientation = 'vertical'

        navigation_bar = CupertinoNavigationBar()
        navigation_bar.height = 60

        title = CupertinoLabel()
        title.text = 'Showcase'
        title.bold = True
        title.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        scrollview = ScrollView()
        scrollview.size_hint_y = None
        scrollview.height = Window.height-navigation_bar.height

        layout = GridLayout()
        layout.cols = 1
        layout.spacing = 15
        layout.padding = 15
        layout.size_hint_y = None
        layout.bind(
            minimum_height=layout.setter('height')
        )

        system_button = CupertinoSystemButton()
        system_button.text = 'Send'
        system_button.size_hint_y = None
        system_button.height = 20

        icon_button = CupertinoIconButton()
        icon_button.icon = 'info'
        icon_button.size_hint_y = None
        icon_button.size = 32, 32

        button = CupertinoButton()
        button.text = 'Hello World'
        button.size_hint_y = None
        button.height = 50

        segmented_controls = CupertinoSegmentedControls()
        segmented_controls.size_hint_y = None
        segmented_controls.height = 30
        segmented_controls.add_tab('Segmented')
        segmented_controls.add_tab('Controls')

        switch = CupertinoSwitch()
        switch.size_hint = None, None
        switch.size = 100, 50

        self.progress_bar = CupertinoProgressbar()
        self.progress_bar.value = 10
        self.progress_bar.size_hint_y = None
        self.progress_bar.height = 5

        stepper = CupertinoStepper()
        stepper.size_hint = None, None
        stepper.size = 100, 30
        stepper.bind(
            on_plus=lambda widget: self.increment_progress(10),
            on_minus=lambda widget: self.increment_progress(-10)
        )

        ny_label = CupertinoLabel()
        ny_label.font_name = 'New York'
        ny_label.text = 'New York Font Label'
        ny_label.size_hint_y = None
        ny_label.height = 20

        sf_label = CupertinoLabel()
        sf_label.font_name = 'San Francisco'
        sf_label.text = 'San Francisco Font Label'
        sf_label.size_hint_y = None
        sf_label.height = 20

        alert_dialog_button = CupertinoButton()
        alert_dialog_button.text = 'Open Alert Dialog'
        alert_dialog_button.size_hint_y = None
        alert_dialog_button.height = 50
        alert_dialog_button.on_release = self.open_alert_dialog

        action_sheet_button = CupertinoButton()
        action_sheet_button.text = 'Open Action Sheet'
        action_sheet_button.size_hint_y = None
        action_sheet_button.height = 50
        action_sheet_button.on_release = self.open_action_sheet

        text_field = CupertinoTextField()
        text_field.hint_text = 'Text Field'
        text_field.size_hint_y = None
        text_field.height = 30

        instructions = CupertinoLabel()
        instructions.text = 'Enter Text Below:'
        instructions.size_hint = None, None
        instructions.size = 120, 20

        text_view = CupertinoTextView()
        text_view.size_hint_y = None
        text_view.height = 100

        navigation_bar.add_widget(title)

        layout.add_widget(system_button)
        layout.add_widget(icon_button)
        layout.add_widget(button)
        layout.add_widget(segmented_controls)
        layout.add_widget(switch)
        layout.add_widget(self.progress_bar)
        layout.add_widget(stepper)
        layout.add_widget(ny_label)
        layout.add_widget(sf_label)
        layout.add_widget(alert_dialog_button)
        layout.add_widget(action_sheet_button)
        layout.add_widget(text_field)
        layout.add_widget(instructions)
        layout.add_widget(text_view)

        scrollview.add_widget(layout)

        box.add_widget(navigation_bar)
        box.add_widget(scrollview)

        return box


Window.clearcolor = 0.98, 0.98, 0.98, 1
Window.size = (300, 500)

app = ShowcaseApp()
app.run()
