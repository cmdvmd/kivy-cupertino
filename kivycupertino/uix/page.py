"""
Pages allow for a separation of different features
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string("""
<_CupertinoScreen>:
    on_press: self.parent._change_screen(self.parent.children[::-1].index(self))
    
    canvas.before:
        Color:
            rgba: self.color_selected if self.selected else self.color_unselected
        Ellipse:
            size: self.height, self.height
            pos: self.x+self.width/2-self.height/2, self.y

<CupertinoPageControls>:
    padding: self.height/3
    spacing: self.height/3
    
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            size: self.size
            pos: self.pos
""")


class _CupertinoScreen(ButtonBehavior, Widget):
    """
    Dot to be added to :class:`CupertinoPageControls` indicating
    a screen on :class:`CupertinoScreenManager`
    """

    selected = BooleanProperty(False)
    """
    If the screen represented by :class:`_CupertinoScreen` is currently selected
    """

    color_selected = ColorProperty()
    """
    Color of :class:`_CupertinoScreen` when selected
    """

    color_unselected = ColorProperty()
    """
    Color of :class:`_CupertinoScreen` when not selected
    """


class CupertinoPageControls(BoxLayout):
    """
    iOS style Page Controls. Will automatically update the number of pages and current page
    when added to an instance of :class:`CupertinoScreenManager`
    
    .. image:: ../_static/page_controls/demo.gif
    """

    tap = BooleanProperty(False)
    """
    If tapping :class:`CupertinoPageControls` will switch to a screen
    
    .. image:: ../_static/page_controls/tap.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoPageControls(tap=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoPageControls:
           tap: True
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    Background color of :class:`CupertinoPageControls`
    
    .. image:: ../_static/page_controls/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoPageControls(background_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoPageControls:
           background_color: 1, 0, 0, 1
    """

    color_selected = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of a dot on :class:`CupertinoPageControls`
    when not selected
    
    .. image:: ../_static/page_controls/color_selected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoPageControls(color_selected=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoPageControls:
           color_selected: 1, 0, 0, 1
    """

    color_unselected = ColorProperty([0.2, 0.2, 0.2, 1])
    """
    Color of a dot on :class:`CupertinoPageControls` when not selected
    
    .. image:: ../_static/page_controls/color_unselected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoPageControls(color_unselected=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoPageControls:
           color_unselected: 0.5, 0, 0, 1
    """

    def on_parent(self, instance, parent):
        """
        Callback when :class:`CupertinoPageControls` is added to :class:`CupertinoScreenManager`

        :param instance: Instance of class :class:`CupertinoPageControls`
        :param parent: Instance of :class:`CupertinoScreenManager`
        """

        assert isinstance(parent, CupertinoScreenManager), 'CupertinoPageControls must be added to an ' \
                                                           'instance of CupertinoScreenManager'
        parent.bind(screen_names=self._add_screen, current=self._select_screen)

    def _add_screen(self, instance, name):
        """
        Callback when a new screen is added to the parent of :class:`CupertinoPageControls`

        :param instance: Instance of class :class:`CupertinoPageControls`
        :param name: Name of added screen
        """

        self.add_widget(_CupertinoScreen(color_selected=self.color_selected, color_unselected=self.color_unselected))

    def _select_screen(self, instance, name):
        """
        Callback when a screen of the parent of :class:`CupertinoPageControls`
        is selected

        :param instance: Instance of class :class:`CupertinoPageControls`
        :param name: Name of selected screen
        """

        for i in range(len(self.children)):
            self.children[i].selected = len(self.children)-1-i == instance.screen_names.index(name)

    def _change_screen(self, index):
        """
        Callback when a new screen on :class:`CupertinoPageControls` is selected

        :param index: Index of screen
        """

        if self.tap:
            self.parent.transition = NoTransition()
            self.parent.current = self.parent.screen_names[index]


class CupertinoScreenManager(ScreenManager):
    """
    A Screen Manager widget that also accepts an instance of
    :class:`CupertinoPageControls`
    """

    def add_widget(self, widget):
        """
        Callback when a :class:`Screen` or a :class:`CupertinoPageControls` is added to
        :class:`CupertinoScreenManager`

        :param widget: Widget to be added to :class:`CupertinoScreenManager`
        """

        if isinstance(widget, CupertinoPageControls):
            super(ScreenManager, self).add_widget(widget)
        else:
            super().add_widget(widget)
