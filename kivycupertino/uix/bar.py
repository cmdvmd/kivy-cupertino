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
    'CupertinoToolbar',
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

<CupertinoToolbar>:
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
            pos: self.x, self.y+self.height

<_CupertinoTab>:
    orientation: 'vertical'
    
    CupertinoSymbol:
        id: symbol
        symbol: root.symbol
        color: root.color_selected if root.selected else root.color_unselected
    CupertinoLabel:
        text: root.text
        font_size: symbol.font_size*0.55
        color: root.color_selected if root.selected else root.color_unselected
        size_hint_y: 0.7

<CupertinoTabBar>:
    items: items

    color: root.background_color
    
    BoxLayout:
        id: items
        orientation: 'horizontal'
        padding: 3
        size: root.size
        pos: root.pos
""")


class CupertinoNavigationBar(FloatLayout):
    """
    iOS style Navigation Bar. :class:`CupertinoNavigationBar`
    is a :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

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


class CupertinoToolbar(FloatLayout):
    """
    iOS style Toolbar. :class:`CupertinoToolbar`
    is a :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

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


class _CupertinoTab(ButtonBehavior, BoxLayout):
    """
    iOS style tab for :class:`CupertinoTabBar`
    """

    text = StringProperty()
    """
    Text of :class:`_CupertinoTab`
    """

    symbol = StringProperty()
    """
    Symbol of :class:`_CupertinoTab`
    """

    selected = BooleanProperty(False)
    """
    If :class:`_CupertinoTab` is selected
    """

    color_unselected = ColorProperty()
    """
    Color of :class:`_CupertinoTab` when not selected
    """

    color_selected = ColorProperty()
    """
    Color of :class:`_CupertinoTab` when selected
    """


class CupertinoTabBar(CupertinoToolbar):
    """
    iOS style tab bar

    .. image:: ../_static/tab_bar/demo.gif
    """

    selected = StringProperty(' ')
    """
    Selected tab of :class:`CupertinoTabBar`
    
    .. image:: ../_static/tab_bar/selected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTabBar(selected='Recents')
   
    **KV**
   
    .. code-block::
    
       CupertinoTabBar:
           selected: 'Recents'
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

    color_selected = ColorProperty([0.2, 0.45, 1, 1])
    """
    Color of the selected tab of :class:`CupertinoTabBar`
    
    .. image:: ../_static/tab_bar/color_selected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTabBar(color_selected=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTabBar:
           color_selected: 1, 0, 0, 1
    """

    color_unselected = ColorProperty([0.7, 0.7, 0.75, 1])
    """
    Color of unselected tabs of :class:`CupertinoTabBar`
    
    .. image:: ../_static/tab_bar/color_unselected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTabBar(color_unselected=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTabBar:
           color_unselected: 0.5, 0, 0, 1
    """

    def on_selected(self, instance, tab_text):
        """
        Callback when a new tab of :class:`CupertinoTabBar` is selected

        :param instance: The instance of :class:`CupertinoTabBar`
        :param tab_text: Text of the selected tag
        """

        for tab in self.items.children:
            tab.selected = tab.text == tab_text

    def add_tab(self, text, symbol):
        """
        Add a tab to :class:`CupertinoTabBar`

        :param text: Text of tab
        :param symbol: :ref:`Symbol <symbol>` of tab

        .. note::
           Tabs can be only added to :class:`CupertinoTabBar` with Python,
           not KV

        .. code-block:: python

           tab_bar = CupertinoTabBar()
           tab_bar.add_tab('Stars', 'star_fill')
           tab_bar.add_tab('People', 'person_alt_circle')
           tab_bar.add_tab('Recents', 'clock_fill')
        """

        tab = _CupertinoTab(
            text=text,
            symbol=symbol,
            color_selected=self.color_selected,
            color_unselected=self.color_unselected,
            on_release=lambda button: setattr(self, 'selected', button.text)
        )

        self.items.add_widget(tab)

        if len(self.items.children) == 1:
            self.selected = text
