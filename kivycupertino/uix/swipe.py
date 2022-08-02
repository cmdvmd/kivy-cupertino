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
    on_touch_up: if args[1].grab_current is self: args[1].ungrab(self)
    on_width: [action.setter('width')(action, self.width / 5.5) for action in self._left_actions + self._right_actions]
    
    RelativeLayout:
        id: content
        size: root.size
        pos: root.pos

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
        self._last_movement = 0
        self._left_actions = []
        self._right_actions = []
        self.bind(width=self._update_actions, x=self._update_actions)

    def _update_actions(self, *args):
        """
        Callback to update position of the actions of :class:`CupertinoSwipeAction`

        :param args: Arguments when updating the position of actions
        """

        self._right_actions.clear()
        self._left_actions.clear()

        for child in self.children[::-1]:
            if isinstance(child, CupertinoSwipeAction):
                if child.side == 'left':
                    self._left_actions.append(child)
                    child.right = self.x
                elif child.side == 'right':
                    self._right_actions.append(child)
                    child.x = self.x + self.width

    def on_touch_down(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is pressed

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        if self.collide_point(*touch.pos):
            touch.grab(self)
            self._last_movement = touch.x
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        """
        Callback when :class:`CupertinoSwipe` is dragged

        :param touch: Touch on :class:`CupertinoSwipe`
        """

        distance = touch.x - self._last_movement
        max_left = sum(action.width for action in self._left_actions)
        max_right = sum(action.width for action in self._right_actions)

        if touch.grab_current is self and ((distance > 0 and self.to_local(*self._content.pos, True)[0] < max_left) or (
                distance < 0 and -self.to_local(*self._content.pos, True)[0] < max_right)):
            self._content.x += distance
            self._last_movement = touch.x

            for index, action in enumerate(self._left_actions):
                action.x += distance * ((max_left - (action.width * index)) / max_left)
            for index, action in enumerate(self._right_actions):
                action.x += distance * ((max_right - (action.width * index)) / max_right)

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
            widget.bind(side=self._update_actions)
            super().add_widget(widget, index, canvas)
            self._update_actions()
            self.bind(height=widget.setter('height'), y=widget.setter('y'))
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
