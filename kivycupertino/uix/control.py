"""
Controls allow users to control information on their screen
"""

from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty, ColorProperty, NumericProperty, BooleanProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSegment',
    'CupertinoSegmentedControls',
    'CupertinoStepper'
]

Builder.load_string("""
<CupertinoSegment>:
    font_size: self.parent.height / 2 if self.parent is not None else '15sp'

<CupertinoSegmentedControls>:
    _segments: segments
    _selected_segment: selected_segment
    
    on_touch_down: args[1].ud[self] = self.collide_point(*args[1].pos)
    on_touch_up: self._select(args[1])
    on_touch_move: self._select(args[1])
    
    canvas.before:
        Color:
            rgba: self.background_color
        RoundedRectangle:
            radius: dp(10),
            size: self.size
            pos: 0, 0
    
    Widget:
        id: selected_segment
        size_hint: None, None
        size: 0, 0
        pos: segments.pos
        
        canvas.before:
            Color:
                rgba: root.color_selected
            RoundedRectangle:
                radius: dp(10),
                size: self.size
                pos: self.pos
    BoxLayout:
        id: segments
        orientation: 'horizontal'
        spacing: dp(3)
        padding: dp(3)
        size: root.size
        pos: 0, 0

<CupertinoStepper>:
    orientation: 'horizontal'
    spacing: dp(2)
    
    CupertinoModalButton:
        text: '-'
        font_size: sp(min(self.size) * 0.7)
        disabled: root.minus_disabled
        text_color: root.text_color
        color_normal: root.color_normal
        color_down: root.color_down
        color_disabled: root.color_disabled
        on_release: root.dispatch('on_minus')
        _radii: dp(root.height / 4), 0, 0, dp(root.height / 4)
    CupertinoModalButton:
        text: '+'
        font_size: sp(min(self.size) * 0.7)
        disabled: root.add_disabled
        text_color: root.text_color
        color_normal: root.color_normal
        color_down: root.color_down
        color_disabled: root.color_disabled
        on_release: root.dispatch('on_plus')
        _radii: 0, dp(root.height / 4), dp(root.height / 4), 0
""")


class CupertinoSegment(CupertinoLabel):
    color = ColorProperty([0, 0, 0, 1])
    """
    Color of text of :class:`CupertinoSegment`
    
    .. image:: ../_static/segment/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegment(color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSegment:
           text_color: 1, 0, 0, 1
    """


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
    
    .. image:: ../_static/segmented_controls/background_color.png
    
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
    
    .. image:: ../_static/segmented_controls/color_selected.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSegmentedControls(color_selected=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSegmentedControls:
           color_selected: 1, 0, 0, 1
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

    def _select(self, touch):
        """
        Callback when new segment of :class:`CupertinoSegmentedControls` is selected

        :param touch: :class:`kivy.input.providers.mouse.MouseMotionEvent` on :class:`CupertinoSegmentedControls`
        """

        for segment in self._segments.children:
            if self in touch.ud and touch.ud[self] and segment.x <= self._segments.to_widget(*touch.pos)[0] <= segment.x + segment.width:
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

    def add_widget(self, widget, index=0, canvas=None):
        """
        .. note::
           The :attr:`text` of every :class:`CupertinoSegment` added must be unique

        Add an instance of :class:`CupertinoSegment` to :class:`CupertinoSegmentedControls`
        """

        if len(self.children) >= 2:
            assert isinstance(widget,
                              CupertinoSegment), 'CupertinoSegmentedControls accepts only CupertinoSegment widget'
            for child in self._segments.children:
                assert child.text != widget.text, f'A tab named "{widget.text}" already exists'

            self._segments.add_widget(widget)
            if len(self._segments.children) == 1:
                self.selected = widget.text
        else:
            super().add_widget(widget, index, canvas)


class CupertinoStepper(BoxLayout):
    """
    iOS style Stepper

    .. image:: ../_static/stepper/demo.gif
    """

    color_normal = ColorProperty([0.9, 0.9, 0.9, 0.75])
    """
    Background color of button of :class:`CupertinoStepper` when not valid
    
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
    Background color of button of :class:`CupertinoStepper` when valid
    
    .. image:: ../_static/stepper/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(color_down=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           color_down: 0.5, 0, 0, 1
    """

    color_disabled = ColorProperty([0.8, 0.8, 0.8, 1])
    """
    Background color of button of :class:`CupertinoStepper` when disabled
    
    .. image:: ../_static/stepper/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(add_disabled=True, color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           add_disabled: True
           color_disabled: 0.5, 0, 0, 1
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

    minus_disabled = BooleanProperty(False)
    """
    If minus button of :class:`CupertinoStepper` is disabled
    
    .. image:: ../_static/stepper/minus_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(minus_disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           minus_disabled: True
    """

    add_disabled = BooleanProperty(False)
    """
    If add button of :class:`CupertinoStepper` is disabled
    
    .. image:: ../_static/stepper/add_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoStepper(add_disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoStepper:
           add_disabled: True
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
        Callback when minus button is valid
        """

    def on_plus(self):
        """
        Callback when plus button is valid
        """
