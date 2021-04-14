from kivy.uix.screenmanager import Screen
from kivycupertino.uix.dialog import CupertinoAlertDialog, CupertinoActionSheet


class DialogShowcaseScreen(Screen):

    def open_alert_dialog(self):
        alert_dialog = CupertinoAlertDialog()
        alert_dialog.title = 'Alert Dialog'
        alert_dialog.content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                               'Quisque tincidunt ut magna quis placerat'
        alert_dialog.add_action('Close', alert_dialog.dismiss)
        alert_dialog.open()

    def open_action_sheet(self):
        action_sheet = CupertinoActionSheet()
        action_sheet.add_action('Sheet', action_sheet.dismiss)
        action_sheet.add_action('[color=ff0000]Action[/color]', action_sheet.dismiss)
        action_sheet.open()
