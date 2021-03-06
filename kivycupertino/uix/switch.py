"""
Switches allow users to toggle settings off/on
"""

from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty, ColorProperty
from kivy.lang.builder import Builder

Builder.load_string("""
<CupertinoSwitch>:
    thumb: thumb
      
    canvas.before:
        Color:
            rgba: root.background_toggled if root.toggled else root.background_untoggled
        RoundedRectangle:
            radius: self.height/2.27,
            size: self.size
            pos: self.pos
    Widget:
        id: thumb
        size_hint_y: 0.9
        width: self.height
        pos_hint: {'center_y': 0.5}
        x: (root.x+root.width-self.width-1) if root.toggled else (root.x+1)
        
        canvas.before:
            Color:
                rgba: root.thumb_color
            Ellipse:
                size: self.size
                pos: self.pos
""")


class CupertinoSwitch(ButtonBehavior, FloatLayout):
    """
    iOS style Switch

    .. image:: ../_static/switch.gif
    """

    toggled = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.switch.CupertinoSwitch` is on
    
    :attr:`toggled` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    Color of thumb of :class:`~kivycupertino.uix.switch.CupertinoSwitch`
    
    :attr:`thumb_color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[1, 1, 1, 1]`
    """

    background_toggled = ColorProperty([0.3, 0.85, 0.4, 1])
    """
    Background color of :class:`~kivycupertino.uix.switch.CupertinoSwitch` when on
    
    :attr:`background_toggled` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.3, 0.85, 0.4, 1]`
    """

    background_untoggled = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of :class:`~kivycupertino.uix.switch.CupertinoSwitch` when off
    
    :attr:`background_untoggled` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0.95, 0.95, 0.95, 1]`
    """

    def on_press(self):
        """
        Callback when :class:`~kivycupertino.uix.switch.CupertinoSwitch` is pressed
        """

        self.toggled = not self.toggled
        self.size = (self.thumb.height, self.thumb.height)
