"""
Bars are generally positioned at the top or bottom of a screen and
contain widgets and/or information for easy access by users
"""

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivycupertino.uix.behavior import SelectableBehavior
from kivy.properties import ColorProperty, StringProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoNavigationBar',
    'CupertinoToolbar',
    'CupertinoTab',
    'CupertinoTabBar'
]

Builder.load_string("""
<CupertinoNavigationBar>:
    canvas.before:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: 0, 0
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Rectangle:
            size: self.width, dp(1)
            pos: 0, 0

<CupertinoToolbar>:
    canvas.before:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: 0, 0
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Rectangle:
            size: self.width, dp(1)
            pos: 0, self.height

<CupertinoTab>:
    orientation: 'vertical'
    
    CupertinoSymbol:
        id: symbol
        symbol: root.symbol
        color: root.color_selected if root.selected else root.color_unselected
    CupertinoLabel:
        text: root.text
        font_size: symbol.font_size * 0.55
        color: root.color_selected if root.selected else root.color_unselected
        size_hint_y: 0.7

<CupertinoTabBar>:
    _tabs: tabs

    color: root.background_color
    
    BoxLayout:
        id: tabs
        orientation: 'horizontal'
        padding: dp(3)
        size: root.size
        pos: 0, 0
""")


class CupertinoNavigationBar(RelativeLayout):
    """
    iOS style Navigation Bar. :class:`CupertinoNavigationBar` is a
    :class:`~kivy.uix.relativelayout.RelativeLayout` and can accept any number of widgets

    .. image:: ../_static/navigation_bar/demo.png
    """

    color = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of :class:`CupertinoNavigationBar`
    
    .. image:: ../_static/navigation_bar/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoNavigationBar(color=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoNavigationBar:
           color: 0.5, 0, 0, 1
    """


class CupertinoToolbar(RelativeLayout):
    """
    iOS style Toolbar. :class:`CupertinoToolbar`
    is a :class:`~kivy.uix.relativelayout.RelativeLayout` and can accept any number of widgets

    .. image:: ../_static/toolbar/demo.png
    """

    color = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of :class:`CupertinoToolbar`
    
    .. image:: ../_static/toolbar/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoToolbar(color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoToolbar:
           color: 0.5, 0, 0, 1
    """


class CupertinoTab(SelectableBehavior, BoxLayout):
    """
    iOS style tab to be used with :class:`CupertinoTabBar`

    .. image:: ../_static/tab/demo.png
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoTab`
    
    .. image:: ../_static/tab/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTab(text='Tab')
   
    **KV**
   
    .. code-block::
    
       CupertinoTab:
           text: 'Tab'
    """

    symbol = StringProperty(' ')
    """
    Symbol of :class:`CupertinoTab`
    
    .. image:: ../_static/tab/symbol.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTab(symbol='hammer_fill')
   
    **KV**
   
    .. code-block::
    
       CupertinoTab:
           symbol: 'hammer_fill'
    """

    color_selected = ColorProperty([0.2, 0.45, 1, 1])
    """
    Color of the selected tab of :class:`CupertinoTab`
    
    .. image:: ../_static/tab/color_selected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTabBar(color_selected=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTab:
           color_selected: 1, 0, 0, 1
    """

    color_unselected = ColorProperty([0.7, 0.7, 0.75, 1])
    """
    Color of :class:`CupertinoTabBar` when not selected
    
    .. image:: ../_static/tab/color_unselected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTab(color_unselected=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTab:
           color_unselected: 0.5, 0, 0, 1
    """


class CupertinoTabBar(CupertinoToolbar):
    """
    iOS style tab bar

    .. image:: ../_static/tab_bar/demo.gif
    """

    background_color = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of :class:`CupertinoTabBar` when selected
    
    .. image:: ../_static/tab_bar/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTabBar(background_color=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTabBar:
           background_color: 0.5, 0, 0, 1
    """

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add an instance of :class:`CupertinoTab` to :class:`CupertinoTabBar`
        """

        if len(self.children) >= 1:
            assert isinstance(widget, CupertinoTab), 'CupertinoTabBar accepts only CupertinoTab widget'
            self._tabs.add_widget(widget)
            if widget.selected or len(self._tabs.children) == 1:
                widget.refresh()
        else:
            super().add_widget(widget, index, canvas)
    
    def get_selected_tab(self):
        """
        Get the currently selected tab of :class:`CupertinoTabBar`
        
        :return: The selected :class:`CupertinoTab`
        """
        
        for tab in self._tabs.children:
            if tab.selected:
                return tab
