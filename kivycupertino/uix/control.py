"""
Controls allow users to control information on their screen
"""

from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ColorProperty, NumericProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSegmentedControls',
    'CupertinoStepper'
]

Builder.load_string("""
<CupertinoSegmentedControls>:
    _segments: segments
    _selected_segment: selected_segment
    
    on_touch_down: args[1].ud['pressed'] = self.collide_point(*args[1].pos)
    
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            radius: 10,
            size: self.size
            pos: self.pos
    
    Widget:
        id: selected_segment
        size_hint: None, None
        size: segments.size
        pos: segments.pos
        
        canvas.before:
            Color:
                rgba: root.color_selected
            RoundedRectangle:
                radius: 10,
                size: self.size
                pos: self.pos    
    BoxLayout:
        id: segments
        orientation: 'horizontal'
        spacing: 3
        padding: 3
        size: root.size
        pos: root.pos

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


class CupertinoSegmentedControls(RelativeLayout):
    """
    iOS style Segmented Controls

    .. image:: ../_static/segmented_controls/demo.gif
    """

    selected = StringProperty(' ')
    """
    Selected tab of :class:`CupertinoSegmentedControls`
    
    .. image:: ../_static/segmented_controls/selected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(selected='Second')
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           selected: 'Second'
    """

    background_color = ColorProperty([0.9, 0.9, 0.9, 0.75])
    """
    Background color of :class:`CupertinoSegmentedControls`
    
    .. image:: ../_static/segmented_controls/background_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(background_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           background_color: 0.5, 0, 0, 1
    """

    color_selected = ColorProperty([1, 1, 1, 1])
    """
    Background color of selected tab of :class:`CupertinoSegmentedControls`
    
    .. image:: ../_static/segmented_controls/color_selected.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(color_selected=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           color_selected: 1, 0, 0, 1
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    Color of text of tabs of :class:`CupertinoSegmentedControls`
    
    .. image:: ../_static/segmented_controls/text_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(text_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           text_color: 1, 0, 0, 1
    """

    transition_duration = NumericProperty(0.1)
    """
    Duration of change of selected segment of :class:`CupertinoSegmentedControls`
    
    .. image:: ../_static/segmented_controls/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(transition_duration=0.5)
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           transition_duration: 0.5
    """

    def on_touch_up(self, touch):
        for segment in self._segments.children:
            if segment.collide_point(*touch.pos) and touch.ud['pressed']:
                self.selected = segment.text
                break

    def on_selected(self, instance, text):
        """
        Callback when a new tab is selected

        :param instance: Instance of :class:`CupertinoSegmentedControls`
        :param text: Text of the selected tab
        """

        for segment in self._segments.children:
            if segment.text == text:
                animation = Animation(
                    size=segment.size,
                    pos=segment.pos,
                    duration=self.transition_duration
                )
                animation.start(self._selected_segment)
                break

    def add_segment(self, text):
        """
        Add a tab to :class:`CupertinoSegmentedControls`

        :param text: Text of tab

        .. note::
           Segments can be only added to :class:`CupertinoSegmentedControls` with Python,
           not KV

        .. code-block:: python

           segmented_controls = CupertinoSegmentedControls()
           segmented_controls.add_segment('First')
           segmented_controls.add_segment('Second')
        """

        for child in self._segments.children:
            assert child.text != text, f'A tab named "{text}" already exists'

        segment = CupertinoLabel(text=text, color=self.text_color)
        self._segments.add_widget(segment)

        if len(self._segments.children) == 1:
            self.selected = text


class CupertinoStepper(BoxLayout):
    """
    iOS style Stepper

    .. image:: ../_static/stepper/demo.gif
    """

    color_normal = ColorProperty([0.9, 0.9, 0.9, 0.75])
    """
    Background color of button of :class:`CupertinoStepper` when not pressed
    
    .. image:: ../_static/stepper/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(color_normal=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([0.7, 0.7, 0.7, 1])
    """
    Background color of button of :class:`CupertinoStepper` when pressed
    
    .. image:: ../_static/stepper/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(color_down=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           color_down: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([0, 0, 0, 1])
    """
    Color of text of button of :class:`CupertinoStepper`
    
    .. image:: ../_static/stepper/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(text_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           text_color: 1, 0, 0, 1
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`CupertinoStepper` and register events

        :param kwargs: Keyword arguments of :class:`CupertinoStepper`
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
