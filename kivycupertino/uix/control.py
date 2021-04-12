"""
Controls allow users to control information on their screen

Segmented Controls
------------------

.. image:: ../_static/segmented_controls.gif

.. code-block:: python

   segmented_controls = CupertinoSegmentedControls()
   segmented_controls.add_tab('Segmented')
   segmented_controls.add_tab('Controls')


Stepper
-------

.. image:: ../_static/stepper.gif

.. code-block:: python

   stepper = CupertinoStepper()
"""

from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, BooleanProperty, ColorProperty
from kivy.clock import Clock
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSegmentedControls',
    'CupertinoStepper'
]

Builder.load_string("""
<_CupertinoSegment>:   
    canvas.before:
        Color:
            rgba: self.color_selected if self.selected else (0, 0, 0, 0)
        RoundedRectangle:
            radius: 10,
            size: self.size
            pos: self.pos

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


class _CupertinoSegment(ButtonBehavior, CupertinoLabel):
    """
    iOS style segment for :class:`~kivycupertino.uix.controls.CupertinoSegmented Controls`
    """

    text = StringProperty()
    """
    A :class:`~kivy.properties.StringProperty` defining the text
    :class:`~kivycupertino.uix.control._CupertinoSegment`
    """

    selected = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.control._CupertinoSegment` is selected
    """

    text_color = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the text of
    :class:`~kivycupertino.uix.control._CupertinoSegment`
    """

    color_selected = ColorProperty()
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.control._CupertinoSegment` when selected
    """


class CupertinoSegmentedControls(BoxLayout):
    """
    iOS style Segmented Controls
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

    def on_selected(self, instance, text):
        """
        Callback when a new tab is selected

        :param instance: Instance of :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`
        :param text: Text of the selected tab
        """

        self.selected = text
        for tab in instance.children:
            tab.selected = tab.text == text

    def add_segment(self, text):
        """
        Add a tab to :class:`~kivycupertino.uix.control.CupertinoSegmentedControls`

        :param text: Text of tab
        """

        for child in self.children:
            assert child.text != text, f'A tab named "{text}" already exists'

        tab = _CupertinoSegment(
            text=text,
            text_color=self.text_color,
            on_release=lambda button: setattr(self, 'selected', button.text)
        )

        self.add_widget(tab)
        if len(self.children) == 1:
            Clock.schedule_once(lambda dt: setattr(self, 'selected', tab.text), 0)


class CupertinoStepper(BoxLayout):
    """
    iOS style Stepper
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
