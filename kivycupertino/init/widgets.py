"""
A program to register Kivy Cupertino widgets for use in kv lang
"""

from kivy.factory import Factory

Factory.register('CupertinoNavigationBar', module='kivycupertino.uix.bar')
Factory.register('CupertinoTabBar', module='kivycupertino.uix.bar')
Factory.register('CupertinoButton', module='kivycupertino.uix.button')
Factory.register('CupertinoSystemButton', module='kivycupertino.uix.button')
Factory.register('CupertinoSymbolButton', module='kivycupertino.uix.button')
Factory.register('CupertinoSegmentedControls', module='kivycupertino.uix.control')
Factory.register('CupertinoStepper', module='kivycupertino.uix.control')
Factory.register('CupertinoProgressBar', module='kivycupertino.uix.indicator')
Factory.register('CupertinoAlertDialog', module='kivycupertino.uix.indicator')
Factory.register('CupertinoLabel', module='kivycupertino.uix.label')
Factory.register('CupertinoScrollView', module='kivycupertino.uix.scrollview')
Factory.register('CupertinoSlider', module='kivycupertino.uix.slider')
Factory.register('CupertinoSwitch', module='kivycupertino.uix.switch')
Factory.register('CupertinoSymbol', module='kivycupertino.uix.symbol')
Factory.register('CupertinoTextField', module='kivycupertino.uix.textfield')
Factory.register('CupertinoTextView', module='kivycupertino.uix.textfield')
