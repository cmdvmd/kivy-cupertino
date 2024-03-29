"""
A program to register Kivy Cupertino widgets for use in Kv language
"""

from kivy.factory import Factory

r = Factory.register

r('CupertinoNavigationBar', module='kivycupertino.uix.bar')
r('CupertinoToolbar', module='kivycupertino.uix.bar')
r('CupertinoTab', module='kivycupertino.uix.bar')
r('CupertinoTabBar', module='kivycupertino.uix.bar')

r('LongPressBehavior', module='kivycupertino.uix.behavior')
r('SelectableBehavior', module='kivycupertino.uix.behavior')

r('CupertinoButton', module='kivycupertino.uix.button')
r('CupertinoSystemButton', module='kivycupertino.uix.button')
r('CupertinoSymbolButton', module='kivycupertino.uix.button')

r('CupertinoSegment', module='kivycupertino.uix.control')
r('CupertinoSegmentedControls', module='kivycupertino.uix.control')
r('CupertinoStepper', module='kivycupertino.uix.control')

r('CupertinoActionSheet', module='kivycupertino.uix.modal')
r('CupertinoDialog', module='kivycupertino.uix.modal')
r('CupertinoModalButton', module='kivycupertino.uix.modal')

r('CupertinoActivityIndicator', module='kivycupertino.uix.indicator')
r('CupertinoProgressBar', module='kivycupertino.uix.indicator')

r('CupertinoLabel', module='kivycupertino.uix.label')

r('CupertinoScreenManager', module='kivycupertino.uix.page')
r('CupertinoPageControls', module='kivycupertino.uix.page')

r('CupertinoScrollView', module='kivycupertino.uix.scrollview')

r('CupertinoSlider', module='kivycupertino.uix.slider')

r('CupertinoSwipe', module='kivycupertino.uix.swipe')
r('CupertinoSwipeAction', module='kivycupertino.uix.swipe')

r('CupertinoSwitch', module='kivycupertino.uix.switch')

r('CupertinoSymbol', module='kivycupertino.uix.symbol')

r('CupertinoTableCell', module='kivycupertino.uix.table')
r('CupertinoClickableTableCell', module='kivycupertino.uix.table')
r('CupertinoTableGroup', module='kivycupertino.uix.table')

r('CupertinoTextField', module='kivycupertino.uix.textinput')
r('CupertinoTextView', module='kivycupertino.uix.textinput')
r('CupertinoSearchBar', module='kivycupertino.uix.textinput')
