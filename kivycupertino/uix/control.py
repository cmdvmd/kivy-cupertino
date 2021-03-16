"""
Controls allow users to control information on their screen
"""

from kivycupertino.uix.button import CupertinoSystemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ColorProperty
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSegmentedControls',
    'CupertinoStepper'
]

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

    selected = StringProperty()
    """
    A :class:`~kivy.properties.StringProperty` defining the selected tab of
    :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    """

    background_color = ColorProperty([0.95, 0.95, 0.95, 0.9])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    """

    color_selected = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of selected tab of
    :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty defining the color of text of tabs of
    :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
    """

    def on_selected(self, widget, text):
        """
        Callback when a new tab is selected

        :param widget: The instance of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
        :param text: The text of the selected tab
        """

        self.selected = text
        tab = None
        for child in self.children:
            if child.text == text:
                tab = child
            child.canvas.before.clear()
        with tab.canvas.before:
            Color(rgba=self.color_selected)
            RoundedRectangle(radius=(10,), size=tab.size, pos=tab.pos)

    def add_tab(self, text):
        """
        Add a tab to :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`

        :param text: Text of tab
        """

        for child in self.children:
            assert child.text != text, f'A tab named "{text}" already exists'

        tab = CupertinoSystemButton(
            text=text,
            markup=False,
            color_normal=self.text_color,
            color_down=self.text_color,
            on_release=lambda button: setattr(self, 'selected', button.text)
        )

        self.add_widget(tab)
        if len(self.children) == 1:
            Clock.schedule_once(lambda dt: setattr(self, 'selected', tab.text), 0.5)


class CupertinoStepper(BoxLayout):
    """
    iOS style Stepper

    .. image:: ../_static/stepper.gif
    """

    color_normal = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of button of
    :class:`~kivycupertino.uix.control.CupertinoStepper` when not pressed
    """

    color_down = ColorProperty([0.8, 0.8, 0.8, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of button of
    :class:`~kivycupertino.uix.control.CupertinoStepper` when pressed
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of text of button of
    :class:`~kivycupertino.uix.control.CupertinoStepper`
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
