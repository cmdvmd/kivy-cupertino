"""
Swiping allows users to interact with widgets by using hidden actions
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stencilview import StencilView
from kivycupertino.uix.behavior import CupertinoButtonBehavior
from kivy.properties import OptionProperty, BooleanProperty, ColorProperty, StringProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSwipe',
    'CupertinoSwipeAction'
]

Builder.load_string("""
<CupertinoSwipe>:
    _content: content
    
    RelativeLayout:
        id: content
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
    """

    def __init__(self, **kwargs):
        """
        Callback to initialize variables of :class:`CupertinoSwipe`
        """

        super().__init__(**kwargs)
        self._left_max = 0
        self._right_max = 0
        self._last_movement = 0
        self.bind(right=self._update_actions)

    def _get_content_pos(self):
        return self.to_local(self._content.x, self._content.y, True)[0]

    def _update_actions(self, *args):
        """
        Callback to update size and side of the actions of :class:`CupertinoSwipe`

        :param args: Arguments when an action's attributes are changed
        """

        self._left_max = 0
        self._right_max = 0

        for child in self.children:
            if isinstance(child, CupertinoSwipeAction):
                if child.size_hint_x is not None:
                    child.width = self.width * child.size_hint_x
                child.x = self.right
                if child.side == 'left':
                    self._left_max += child.width
                elif child.side == 'right':
                    self._right_max += child.width

    def _move_actions(self):
        """
        Callback to move all actions of :class:`CupertinoSwipe` when swiped
        """

        content_position = self._get_content_pos()
        moved_left = 0
        moved_right = 0

        for child in self.children[::-1]:
            if isinstance(child, CupertinoSwipeAction):
                if child.side == 'left':
                    action_position = (self._left_max - moved_left) * (content_position / self._left_max)
                    child.right = self.to_parent(action_position, 0, True)[0]
                    moved_left += child.width
                elif child.side == 'right':
                    action_position = (self._right_max - moved_right) * (-content_position / self._right_max)
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

    def on_touch_move(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is dragged

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        if touch.grab_current is self:
            distance = touch.x - self._last_movement
            position = self._get_content_pos()
            if (distance > 0 and position < self._left_max) or (distance < 0 and -position < self._right_max):
                self._content.x += distance
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


class CupertinoSwipeAction(CupertinoButtonBehavior, BoxLayout, StencilView):
    """
    An iOS style action to add to :class:`CupertinoSwipe`
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
    
       CupertinoSwipeAction(color_disabled=(0.5, 0, 0, 1))
       
    **KV**
    
    .. code-block::

       CupertinoSwipeAction:
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
