"""
Pages allow for a separation of different features

Page Controls
-------------

.. image:: ../_static/page_controls.gif

**Python**

.. code-block:: python

   screen_manager = CupertinoScreenManager()  # Must be CupertinoScreenManager
   page_controls = CupertinoPageControls()

   screen_manager.add_widget(page_controls)

**KV**

.. code-block::

   CupertinoScreenManager:  # Must be CupertinoScreenManager
       CupertinoPageControls:
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
    Dot to be added to :class:`~kivycupertino.uix.page.CupertinoPageControls` indicating
    a screen on :class:`~kivycupertino.uix.page.CupertinoScreenManager`
    """

    selected = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if the screen represented by
    :class:`~kivycupertino.uix.page._CupertinoScreen` is currently selected
    """

    color_selected = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.page._CupertinoScreen` when selected
    """

    color_unselected = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of
    :class:`~kivycupertino.uix.page._CupertinoScreen` when not selected
    """


class CupertinoPageControls(BoxLayout):
    """
    iOS style Page Controls
    """

    allow_tap = BooleanProperty(True)
    """
    A :class:`~kivy.properties.ColorProperty` defining if tapping
    :class:`~kivycupertino.uix.page.CupertinoPageControls` will switch to a screen
    """

    background_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.page.CupertinoPageControls`
    """

    color_selected = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of a dot on
    :class:`~kivycupertino.uix.page.CupertinoPageControls` when not selected
    """

    color_unselected = ColorProperty([0.2, 0.2, 0.2, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of a dot on
    :class:`~kivycupertino.uix.page.CupertinoPageControls` when not selected
    """

    def on_parent(self, instance, parent):
        """
        Callback when :class:`~kivycupertino.uix.page.CupertinoPageControls` is added to
        :class:`~kivycupertino.uix.page.CupertinoScreenManager`

        :param instance: Instance of class :class:`~kivycupertino.uix.page.CupertinoPageControls`
        :param parent: Instance of :class:`~kivycupertino.uix.page.CupertinoScreenManager`
        """

        assert isinstance(parent, CupertinoScreenManager), 'CupertinoPageControls must be added to an instance of CupertinoScreenManager'
        parent.bind(screen_names=self._add_screen, current=self._select_screen)

    def _add_screen(self, instance, name):
        """
        Callback when a new screen is added to the parent of
        :class:`~kivycupertino.uix.page.CupertinoPageControls`

        :param instance: Instance of class :class:`~kivycupertino.uix.page.CupertinoPageControls`
        :param name: Name of added screen
        """

        self.add_widget(_CupertinoScreen(color_selected=self.color_selected, color_unselected=self.color_unselected))

    def _select_screen(self, instance, name):
        """
        Callback when a screen of the parent of :class:`~kivycupertino.uix.page.CupertinoPageControls`
        is selected

        :param instance: Instance of class :class:`~kivycupertino.uix.page.CupertinoPageControls`
        :param name: Name of selected screen
        """

        for i in range(len(self.children)):
            self.children[i].selected = len(self.children)-1-i == instance.screen_names.index(name)

    def _change_screen(self, index):
        """
        Callback when a new screen on :class:`~kivycupertino.uix.page.CupertinoPageControls` is selected

        :param index: Index of screen
        """

        if self.allow_tap:
            self.parent.transition = NoTransition()
            self.parent.current = self.parent.screen_names[index]


class CupertinoScreenManager(ScreenManager):
    """
    A Screen Manager widget that also accepts an instance of
    :class:`~kivycupertino.uix.page.CupertinoPageControls`
    """

    def add_widget(self, widget):
        """
        Callback when a :class:`~kivy.uix.screenmanager.Screen` or a
        :class:`~kivycupertino.uix.page.CupertinoPageControls` is added to
        :class:`~kivycupertino.uix.page.CupertinoScreenManager`

        :param widget: Widget to be added to :class:`~kivycupertino.uix.page.CupertinoScreenManager`
        """

        if isinstance(widget, CupertinoPageControls):
            super(ScreenManager, self).add_widget(widget)
        else:
            super().add_widget(widget)
