"""
Gestures allow users to interact with widgets on screen
"""

from kivy.properties import NumericProperty, BooleanProperty
from kivy.clock import Clock
from kivy.logger import Logger
from plyer import vibrator

__all__ = [
    'LongPressBehavior'
]


class LongPressBehavior:
    """
    Behavior to detect a long press on a widget

    .. image:: ../_static/long_press/demo.gif

    .. note::
       :class:`LongPressBehavior` can only be used as a superclass for an instance of :class:`Widget`

       .. code-block:: python

          class ExampleWidget(LongPressBehavior, CupertinoButton):
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

    haptic_touch = BooleanProperty(False)
    """
    If Haptic Touch is enabled to provide haptic (vibrational) feedback when a long press is detected
    
    .. note::
       Vibration is only available on Android and iOS. When compiling for Android, ensure to include
       the ``VIBRATE`` permission in ``buildozer.spec``
   
    **Python**
    
    .. code-block:: python
    
       ExampleWidget(haptic_touch=True)
   
    **KV**
    
    .. code-block::
    
       ExampleWidget:
           haptic_touch: True
    """

    vibration_duration = NumericProperty(0.1)
    """
    How long to vibrate if :attr:`haptic_touch` is enabled
    
    **Python**
    
    .. code-block:: python
    
       ExampleWidget(vibration_duration=1)
   
    **KV**
    
    .. code-block::
    
       ExampleWidget:
           vibration_duration: 1
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_long_press')

    def on_touch_down(self, touch):
        if self.collide_point(touch.ox, touch.oy):
            touch.ud['callback'] = Clock.schedule_once(
                lambda dt: self.dispatch('on_long_press', touch),
                self.long_press_duration
            )
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if 'callback' in touch.ud:
            touch.ud['callback'].cancel()
        return super().on_touch_up(touch)

    def on_long_press(self, touch):
        """
        Event when a widget is long pressed

        :param touch: The touch on this widget
        """

        if self.haptic_touch:
            try:
                assert vibrator.exists()
                vibrator.vibrate(time=self.vibration_duration)
            except (NotImplementedError, AssertionError):
                Logger.warning('Vibrator: Vibration is not supported on this device')
