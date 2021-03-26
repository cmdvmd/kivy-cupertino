"""
Bars are generally positioned at the top or bottom of a screen and
contain widgets and/or information for easy access by users
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ColorProperty, BooleanProperty, StringProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoNavigationBar',
    'CupertinoTabBar'
]

Builder.load_string("""
<CupertinoNavigationBar>:
    canvas.before:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Rectangle:
            size: self.width, 1
            pos: self.pos

<_CupertinoTab>:
    orientation: 'vertical'
    
    CupertinoSymbol:
        symbol: root.symbol
        color: root.color_selected if root.selected else root.color_unselected
    CupertinoLabel:
        text: root.text
        font_size: 12
        color: root.color_selected if root.selected else root.color_unselected
        size_hint_y: 0.7

<CupertinoTabBar>:
    padding: 3
    
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Rectangle:
            size: self.width, 1
            pos: self.x, self.y+self.height
""")


class CupertinoNavigationBar(FloatLayout):
    """
    iOS style Navigation Bar. :class:`~kivycupertino.uix.bar.CupertinoNavigationBar`
    is a :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

    .. image:: ../_static/navigation_bar.png
    """

    color = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.bar.CupertinoNavigationBar`
    """


class _CupertinoTab(ButtonBehavior, BoxLayout):
    """
    iOS style tab for :class:`~kivycupertino.uix.bar.CupertinoTabBar`
    """

    text = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of
    :class:`~kivycupertino.uix.bar._CupertinoTab`
    """

    symbol = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the symbol of
    :class:`~kivycupertino.uix.bar._CupertinoTab`
    """

    selected = BooleanProperty(False)
    """
    A :class:`~kivy.properties.Boolean` defining if
    :class:`~kivycupertino.uix.bar._CupertinoTab` is selected
    """

    color_unselected = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.bar._CupertinoTab` when not selected
    """

    color_selected = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.bar._CupertinoTab` when selected
    """


class CupertinoTabBar(BoxLayout):
    """
    iOS style tab bar

    .. image:: ../_static/tab_bar.gif
    """

    selected = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the selected tab of
    :class:`~kivycupertino.uix.bar.CupertinoTabBar`
    """

    background_color = ColorProperty([0.95, 0.95, 0.95, 0.75])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.bar.CupertinoTabBar` when selected
    """

    color_selected = ColorProperty([0.2, 0.45, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the selected tab of
    :class:`~kivycupertino.uix.bar.CupertinoTabBar` when selected
    """

    color_unselected = ColorProperty([0.7, 0.7, 0.75, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of unselected tabs of
    :class:`~kivycupertino.uix.bar.CupertinoTabBar`
    """

    def on_selected(self, widget, tab_text):
        """
        Callback when a new tab of :class:`kivycupertino.uix.bar.CupertinoTabBar` is selected

        :param widget: The instance of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
        :param tab_text: Text of the selected tag
        """

        for tab in self.children:
            tab.selected = tab.text == tab_text

    def add_tab(self, text, symbol):
        """
        Add a tab to :class:`~kivycupertino.uix.control.CupertinoTabBar`

        :param text: Text of tab
        :param symbol: :ref:`Symbol <symbol>` of tab
        """

        tab = _CupertinoTab(
            text=text,
            symbol=symbol,
            color_selected=self.color_selected,
            color_unselected=self.color_unselected,
            on_release=lambda button: setattr(self, 'selected', button.text)
        )

        self.add_widget(tab)

        if len(self.children) == 1:
            self.selected = text
