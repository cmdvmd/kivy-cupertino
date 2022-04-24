"""
Controls allow users to control information on their screen
"""

from kivycupertino.uix.label import CupertinoLabel
from kivycupertino.uix.behavior import SelectableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty
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
    
    on_touch_down: if self.collide_point(*args[1].pos): args[1].grab(self)
    on_touch_up:
        self._select(self.get_selected_segment(), self.transition_duration)
        if args[1].grab_current is self: args[1].ungrab(self)

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


class CupertinoSegment(SelectableBehavior, CupertinoLabel):
    """
    iOS style segment to be used with :class:`CupertinoSegmentedControls`
    """

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

    def __init__(self, **kwargs):
        """
        Initialize behaviors of :class:`CupertinoSegmentedControls`

        :param kwargs: Keyword arguments for :class:`CupertinoSegmentedControls`
        """

        super().__init__(**kwargs)
        def resize(*args): self._select(self.get_selected_segment(), 0)
        self.bind(size=resize, pos=resize)

    def _select(self, segment, duration):
        """
        Show selection animation to select a segment of :class:`CupertinoSegmentedControls`

        :param segment: Segment of :class:`CupertinoSegmentedControls` to be selected
        """

        segment.selected = True
        animation = Animation(
            size=segment.size,
            pos=segment.pos,
            duration=duration
        )
        animation.start(self._selected_segment)

    def on_touch_move(self, touch):
        """
        Detect a movement on a segment of :class:`CupertinoSegmentedControls`

        :param touch: Touch on :class:`CupertinoSegmentedControls`
        """

        for segment in self._segments.children:
            if touch.grab_current is self and segment.x <= self.to_local(*touch.pos)[0] <= segment.x + segment.width:
                self._select(segment, self.transition_duration)
                break

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add an instance of :class:`CupertinoSegment` to :class:`CupertinoSegmentedControls`
        """

        if len(self.children) >= 2:
            assert isinstance(widget,
                              CupertinoSegment), 'CupertinoSegmentedControls accepts only CupertinoSegment widget'
            self._segments.add_widget(widget, index)
            if widget.selected or len(self._segments.children) == 1:
                widget.refresh()
        else:
            super().add_widget(widget, index, canvas)

    def get_selected_segment(self):
        """
        Get the currently selected segment of :class:`CupertinoSegmentedControls`

        :return: The selected :class:`CupertinoSegment`
        """

        for segment in self._segments.children:
            if segment.selected:
                return segment


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
