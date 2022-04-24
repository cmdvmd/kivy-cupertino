"""
Gestures allow users to interact with widgets on screen

.. note::
   Behaviors can only be used as superclasses for instances of :class:`Widget`
"""

from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock

__all__ = [
    'LongPressBehavior',
    'SelectableBehavior'
]


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
