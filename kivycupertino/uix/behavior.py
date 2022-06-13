"""
Behaviors allow for expanded functionality for existing widgets

.. note::
   Behaviors can only be used as superclasses for instances of :class:`Widget`
"""

from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import NumericProperty, BooleanProperty, ColorProperty
from kivy.animation import Animation
from kivy.clock import Clock

__all__ = [
    'CupertinoButtonBehavior',
    'LongPressBehavior',
    'SelectableBehavior'
]


class CupertinoButtonBehavior(ButtonBehavior):
    """
    Base class for buttons that can only be used with an instance of :class:`kivy.uix.widget.Widget`
    """

    disabled = BooleanProperty()
    """
    If widget with :class:`CupertinoButtonBehavior` is disabled
    
    .. image:: ../_static/button/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(disabled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of widget with :class:`CupertinoButtonBehavior` when its
    state changes
    
    .. image:: ../_static/button/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(transition_duration=0.5)
       
    **KV**
    
    .. code-block::

       CupertinoButton:
           transition_duration: 0.5
    """

    color_normal = ColorProperty()
    """
    Color of widget with :class:`CupertinoButtonBehavior` when not pressed or disabled
    
    .. image:: ../_static/button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(color_normal=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty()
    """
    Color of widget with :class:`CupertinoButtonBehavior` when pressed
    
    .. image:: ../_static/button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(color_down=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           color_down: 1, 0, 0, 1
    """

    color_disabled = ColorProperty()
    """
    Color of widget with :class:`CupertinoButtonBehavior` when disabled
    
    .. image:: ../_static/button/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoButton(disabled=True, color_disabled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoButton:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """

    color = ColorProperty()
    """
    Current color of a widget with :class:`CupertinoButtonBehavior`
    """

    def __init__(self, **kwargs):
        """
        Initialize behavior of :class:`CupertinoButtonBehavior`

        :param kwargs: Keyword arguments of :class:`CupertinoButtonBehavior`
        """

        super().__init__(**kwargs)
        self.color = self.color_normal
        self.bind(
            disabled=lambda *args: self._animate_color(),
            state=lambda *args: self._animate_color(),
            color_normal=lambda *args: self._set_color(),
            color_down=lambda *args: self._set_color(),
            color_disabled=lambda *args: self._set_color()
        )

    def _get_color(self):
        if self.state == 'down':
            return self.color_down
        elif self.disabled:
            return self.color_disabled
        else:
            return self.color_normal

    def _animate_color(self):
        """
        Callback when the state of :class:`CupertinoSymbolButton` changes
        """

        animation = Animation(color=self._get_color(), duration=self.transition_duration)
        animation.start(self)

    def _set_color(self):
        self.color = self._get_color()


class LongPressBehavior:
    """
    Behavior to detect a long press on a widget

    .. image:: ../_static/long_press/demo.gif
    """

    long_press_duration = NumericProperty(1)
    """
    Time that constitutes a long press
    
    .. image:: ../_static/long_press/long_press_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       ExampleWidget(long_press_duration=2)
   
    **KV**
    
    .. code-block::
    
       ExampleWidget:
           long_press_duration: 2
    """

    def __init__(self, **kwargs):
        """
        Initialize behaviors of :class:`LongPressBehavior`

        :param kwargs: Keyword arguments for :class:`LongPressBehavior`
        """

        super().__init__(**kwargs)
        self.register_event_type('on_long_press')

    def on_touch_down(self, touch):
        """
        Callback when a widget is clicked

        :param touch: Touch on the widget
        """

        if self.collide_point(*touch.opos):
            touch.ud['callback'] = Clock.schedule_once(
                lambda dt: self.dispatch('on_long_press', touch),
                self.long_press_duration
            )
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """
        Callback when a widget is released

        :param touch: Touch on the widget
        """

        if 'callback' in touch.ud:
            touch.ud['callback'].cancel()
        return super().on_touch_up(touch)

    def on_long_press(self, touch):
        """
        Event when a widget is long pressed

        :param touch: The touch on this widget
        """


class SelectableBehavior:
    """
    Behavior to detect a selection of a specific widget among all other widgets in :attr:`parent`

    .. image:: ../_static/segmented_controls/demo.gif
    """

    selected = BooleanProperty(False)
    """
    If a widget is selected in its :attr:`parent`
    
    .. image:: ../_static/segmented_controls/selected.png
    
    **Python**
    
    .. code-block:: python
    
       ExampleWidget(selected=True)
   
    **KV**
    
    .. code-block::
    
       ExampleWidget:
           selected: True
    """

    def __init__(self, **kwargs):
        """
        Initialize behaviors of :class:`SelectableBehavior`

        :param kwargs: Keyword arguments for :class:`SelectableBehavior`
        """

        super().__init__(**kwargs)
        self.register_event_type('on_chosen')

    def on_touch_up(self, touch):
        """
        Callback when a widget is released

        :param touch: Touch on the widget
        """

        if self.collide_point(*touch.opos) and self.collide_point(*touch.pos):
            self.selected = True
        return super().on_touch_up(touch)

    def on_selected(self, instance, value):
        """
        Callback when :attr:`selected` of a widget with :class:`SelectableBehavior` is changed

        :param instance: Instance of widget with :class:`SelectableBehavior`
        :param value: Value of :attr:`selected`
        """

        if self.parent is not None and value:
            self.dispatch('on_chosen')
            for child in self.parent.children:
                if child is not self and isinstance(child, SelectableBehavior):
                    child.selected = False

    def refresh(self):
        """
        Set :attr:`selected` of this instance of :class:`SelectableBehavior` to ``True`` while setting all other
        instances in :attr:`parent` to ``False``

        .. note::
           This function is mainly to be used when adding widgets to a parent. Otherwise, setting :attr:`selected`
           to ``True`` will achieve this
        """

        self.selected = False
        self.selected = True

    def on_chosen(self):
        """
        Event when a widget is selected
        """
