"""
Controls allow users to control information on their screen
"""

from kivycupertino.uix.button import CupertinoSystemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ColorProperty
from kivy.graphics import Color, RoundedRectangle
from kivy.lang.builder import Builder

Builder.load_string("""
<CupertinoSegmentedControls>:
    orientation: 'horizontal'
    spacing: 3
    padding: 3
    
    canvas.before:
        Color:
            rgba: root.background_color
        RoundedRectangle:
            radius: 10,
            size: self.size
            pos: self.pos

<CupertinoStepper>:
    orientation: 'horizontal'
    spacing: 2
    
    CupertinoSystemButton:
        text: '-'
        font_size: 25
        color_normal: root.text_color
        color_down: root.text_color
        on_release: root.dispatch('on_minus')
        
        canvas.before:
            Color:
                rgba: root.color_down if self.state == 'down' else root.color_normal
            RoundedRectangle:
                radius: root.height/4, 0, 0, root.height/4
                size: self.size
                pos: self.pos
    CupertinoSystemButton:
        text: '+'
        font_size: 25
        color_normal: root.text_color
        color_down: root.text_color
        on_release: root.dispatch('on_plus')
        
        canvas.before:
            Color:
                rgba: root.color_down if self.state == 'down' else root.color_normal
            RoundedRectangle:
                radius: 0, root.height/4, root.height/4, 0
                size: self.size
                pos: self.pos
""")


class CupertinoSegmentedControls(BoxLayout):
    """
    iOS style Segmented Controls

    .. image:: ../_static/segmented_controls.gif
    """

    background_color = ColorProperty([0.95, 0.95, 0.95, 0.9])
    """
    Background color of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    
    :attr:`background_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.95, 0.95, 0.95, 0.9]`
    """

    color_selected = ColorProperty([1, 1, 1, 1])
    """
    Background color of selected tab of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    
    :attr:`color_selected` is a :class:`~kivy.properties.ColorProperty` and defaults to `[1, 1, 1, 1]`
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    Color of text of tabs of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    
    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 1]`
    """

    def __select(self, tab, action=None):
        """
        Changes color of selected tab

        :param tab: The selected tab
        :param action: The callback to be performed
        """

        for child in self.children:
            child.canvas.before.clear()

        with tab.canvas.before:
            Color(rgba=self.color_selected)
            RoundedRectangle(radius=(10,), size=tab.size, pos=tab.pos)

        if action is not None:
            action(self)

    def add_tab(self, text, action):
        """
        Add a tab to :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`

        :param text: Text of tab
        :param action: Callback to be performed, bound to ``on_release`` of tab
        """

        tab = CupertinoSystemButton(
            text=text,
            markup=False,
            color_normal=self.text_color,
            color_down=self.text_color,
            on_release=lambda b: self.__select(b, action)
        )
        self.add_widget(tab)
        self.__select(tab)


class CupertinoStepper(BoxLayout):
    """
    iOS style Stepper

    .. image:: ../_static/stepper.gif
    """

    color_normal = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of button of :class:`~kivycupertino.uix.control.CupertinoStepper` when not pressed
    
    :attr:`color_normal` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.95, 0.95, 0.95, 1]`
    """

    color_down = ColorProperty([0.8, 0.8, 0.8, 1])
    """
    Background color of button of :class:`~kivycupertino.uix.control.CupertinoStepper` when pressed
    
    :attr:`color_down` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.8, 0.8, 0.8, 1]`
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    Color of text of button of :class:`~kivycupertino.uix.control.CupertinoStepper`
    
    :attr:`text_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 1]`
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`~kivycupertino.uix.control.CupertinoStepper` and register events
        :param kwargs: Keyword arguments of :class:`~kivycupertino.uix.control.CupertinoStepper`
        """

        super().__init__(**kwargs)
        self.register_event_type('on_minus')
        self.register_event_type('on_plus')

    def on_minus(self):
        """
        Callback when minus button is pressed
        """

    def on_plus(self):
        """
        Callback when plus button is pressed
        """
