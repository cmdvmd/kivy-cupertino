"""
Swiping allows users to interact with widgets by using hidden actions
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView
from kivycupertino.uix.behavior import CupertinoButtonBehavior
from kivy.properties import NumericProperty, OptionProperty, BooleanProperty, ColorProperty, StringProperty
from kivy.animation import Animation
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSwipe',
    'CupertinoSwipeAction'
]

Builder.load_string("""
<CupertinoSwipe>:
    _content: content
    
    CupertinoTableCell:
        id: content
        color: root.background_color
        size: root.size
        pos: root.pos
        on_x: root._move_actions()

<CupertinoSwipeAction>:
    color_down: self.color_normal
    orientation: 'vertical'
    padding: 5, 15
    
    canvas.before:
        Color:
            rgba: self.color
        Rectangle:
            size: self.size
            pos: self.pos
        
    CupertinoSymbol:
        id: symbol
        symbol: root.symbol
        color: root.text_color
        size_hint_y: 1.2
    CupertinoLabel:
        text: root.text
        color: root.text_color
        font_size: symbol.font_size * 0.6
""")


class CupertinoSwipe(StencilView):
    """
    A widget to add swiping functionality to existing Kivy Cupertino widgets

    .. image:: ../_static/swipe/demo.gif
    """

    background_color = ColorProperty([1, 1, 1, 1])
    """
    Background color of :class:`CupertinoSwipe`
    
    .. image:: ../_static/swipe/background_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipe(background_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwipe:
           background_color: 1, 0, 0, 1
    """

    complete_swipe_duration = NumericProperty(0.5)
    """
    How long after :class:`CupertinoSwipe` is released until swipe is moved to final position
    (completely expanded or completely collapsed)
    
    .. image:: ../_static/swipe/complete_swipe_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipe(complete_swipe_duration=1)
    
    **KV**
    
    .. code-block::
    
       CupertinoSwipe:
           complete_swipe_duration: 1
    """

    def __init__(self, **kwargs):
        """
        Callback to initialize variables of :class:`CupertinoSwipe`
        """

        super().__init__(**kwargs)
        self._left_distance = 0
        self._right_distance = 0
        self._last_movement = 0
        self._direction = 0
        self.bind(right=self._update_actions)

    def _get_content_pos(self):
        """
        Get the current position of the content being swiped

        :return: The position of the content relative to the widget
        """

        return self.to_local(self._content.x, self._content.y, True)[0]

    def _complete_swipe(self, *args):
        """
        Callback to reset :class:`CupertinoSwipe` after a swipe

        :param args: Arguments to reset :class:`CupertinoSwipe`
        """

        self._direction = 0

    def _update_actions(self, *args):
        """
        Callback to update size and side of the actions of :class:`CupertinoSwipe`

        :param args: Arguments when an action's attributes are changed
        """

        self._left_distance = 0
        self._right_distance = 0

        for child in self.children:
            if isinstance(child, CupertinoSwipeAction):
                if child.size_hint_x is not None:
                    child.width = self.width * child.size_hint_x
                child.x = self.right
                if child.side == 'left':
                    self._left_distance += child.width
                elif child.side == 'right':
                    self._right_distance -= child.width

    def _move_actions(self):
        """
        Callback to move all actions of :class:`CupertinoSwipe` when swiped
        """

        content_position = self._get_content_pos()
        moved_left = 0
        moved_right = 0

        for child in self.children[::-1]:
            if isinstance(child, CupertinoSwipeAction):
                if child.side == 'left' and self._direction != -1:
                    action_position = (self._left_distance - moved_left) * (content_position / self._left_distance)
                    child.right = self.to_parent(action_position, 0, True)[0]
                    moved_left += child.width
                elif child.side == 'right' and self._direction != 1:
                    action_position = -(self._right_distance + moved_right) * (content_position / self._right_distance)
                    child.x = self.right - action_position
                    moved_right += child.width

    def on_touch_down(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is pressed

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        if self.collide_point(*touch.pos):
            touch.grab(self)
            self._last_movement = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is released

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        if touch.grab_current is self:
            touch.ungrab(self)
            position = self._get_content_pos()

            if position > self._left_distance - position and self._direction == 1:
                self.expand('left')
            elif position < self._right_distance - position and self._direction == -1:
                self.expand('right')
            else:
                self.collapse()
        return super().on_touch_up(touch)

    def on_touch_move(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is dragged

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        if touch.grab_current is self:
            Animation.cancel_all(self._content)
            distance = touch.x - self._last_movement
            position = self._get_content_pos()
            if (distance > 0 and position < self._left_distance) or (distance < 0 and position > self._right_distance):
                if self._direction == 0 and not self.is_collapsed():
                    self._direction = position / abs(position)
                self._content.x += distance * (
                    0.2 if position != 0 and position / abs(position) != self._direction else 1)
                self._last_movement = touch.x
        return super().on_touch_move(touch)

    def add_widget(self, widget, index=0, canvas=None):
        """
        Callback to add a widget to :class:`CupertinoSwipe`

        :param widget: Widget to be added to :class:`CupertinoSwipe`
        :param index: Index :param widget: should be added to :class:`CupertinoSwipe`
        :param canvas: Canvas :param widget: should be added to
        """

        if len(self.children) < 1:
            super().add_widget(widget, index, canvas)
        elif isinstance(widget, CupertinoSwipeAction):
            super().add_widget(widget, index, canvas)
            widget.bind(side=self._update_actions, size_hint_x=self._update_actions)
            self.bind(height=widget.setter('height'), y=widget.setter('y'))
            self._update_actions()
        else:
            self._content.add_widget(widget, index, canvas)

    def is_collapsed(self):
        """
        Check if :class:`CupertinoSwipe` is collapsed

        :return: If :class:`CupertinoSwipe` is collapsed
        """

        return self._get_content_pos() == 0

    def collapse(self):
        """
        Callback to reset :class:`CupertinoSwipe` so no actions are visible

        .. image:: ../_static/swipe/collapse.gif
        """

        animation = Animation(x=self.to_parent(0, 0, True)[0], duration=self.complete_swipe_duration, t='out_circ')
        animation.bind(on_complete=self._complete_swipe)
        animation.start(self._content)

    def expand(self, side):
        """
        Callback to completely open a specified side :class:`CupertinoSwipe`

        .. image:: ../_static/swipe/expand.gif

        :param side: The side of :class:`CupertinoSwipe` to expand (``'left'`` or ``'right'``)
        """

        if side in ['left', 'right']:
            x = self.to_parent(self._left_distance if side == 'left' else self._right_distance, 0, True)[0]
            animation = Animation(x=x, duration=self.complete_swipe_duration, t='out_circ')
            animation.start(self._content)
        else:
            raise ValueError(f"Unknown side '{side}'")


class CupertinoSwipeAction(CupertinoButtonBehavior, BoxLayout, StencilView):
    """
    An iOS style action to add to :class:`CupertinoSwipe`

    .. image:: ../_static/swipe_action/demo.png
    """

    side = OptionProperty('left', options=['left', 'right'])
    """
    Side of :class:`CupertinoSwipe` that :class:`CupertinoSwipeAction` should be shown on
    
    .. image:: ../_static/swipe_action/side.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(side='right')
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           side: 'right'
    """

    symbol = StringProperty(' ')
    """
    Text of :class:`CupertinoSwipeAction`
    
    .. image:: ../_static/swipe_action/symbol.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(symbol='trash_fill')
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           symbol: 'trash_fill'
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoSwipeAction`
    
    .. image:: ../_static/swipe_action/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(text='Delete')
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           text: 'Delete'
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoSwipeAction` is disabled
    
    .. image:: ../_static/swipe_action/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(disabled=True)
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           disabled: True
    """

    color_normal = ColorProperty([1, 0, 0, 1])
    """
    Color of :class:`CupertinoSwipeAction` when not pressed or disabled
    
    .. image:: ../_static/swipe_action/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(color_normal=(1, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           color_normal: 1, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0.3, 0.4, 1])
    """
    Color of :class:`CupertinoSwipeAction` when disabled
    
    .. image:: ../_static/swipe_action/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(disabled=True, color_disabled=(0.5, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([1, 1, 1, 1])
    """
    Color of text of :class:`CupertinoSwipeAction`
    
    .. image:: ../_static/swipe_action/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwipeAction(text_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwipeAction:
           text_color: 1, 0, 0, 1
    """
