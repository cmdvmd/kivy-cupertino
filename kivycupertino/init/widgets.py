"""
A program to register Kivy Cupertino widgets for use in kv lang
"""

from kivy.factory import Factory

r = Factory.register

r('CupertinoNavigationBar', module='kivycupertino.uix.bar')
r('CupertinoTabBar', module='kivycupertino.uix.bar')
r('CupertinoButton', module='kivycupertino.uix.button')
r('CupertinoBackButton', module='kivycupertino.uix.button')
r('CupertinoNextButton', module='kivycupertino.uix.button')
r('CupertinoSystemButton', module='kivycupertino.uix.button')
r('CupertinoSymbolButton', module='kivycupertino.uix.button')
r('CupertinoSegmentedControls', module='kivycupertino.uix.control')
r('CupertinoStepper', module='kivycupertino.uix.control')
r('CupertinoActivityIndicator', module='kivycupertino.uix.indicator')
r('CupertinoProgressBar', module='kivycupertino.uix.indicator')
r('CupertinoLabel', module='kivycupertino.uix.label')
r('CupertinoScreenManager', module='kivycupertino.uix.page')
r('CupertinoPageControls', module='kivycupertino.uix.page')
r('CupertinoScrollView', module='kivycupertino.uix.scrollview')
r('CupertinoSlider', module='kivycupertino.uix.slider')
r('CupertinoSwitch', module='kivycupertino.uix.switch')
r('CupertinoSymbol', module='kivycupertino.uix.symbol')
r('CupertinoSearchBar', module='kivycupertino.uix.textinput')
r('CupertinoTextField', module='kivycupertino.uix.textinput')
r('CupertinoTextView', module='kivycupertino.uix.textinput')
