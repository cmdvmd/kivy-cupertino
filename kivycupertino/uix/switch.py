"""
Switches allow users to toggle settings off/on
"""

from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, ColorProperty, NumericProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoSwitch'
]

Builder.load_string("""
<CupertinoSwitch>: 
    on_press: self.toggled = not self.toggled
        
    canvas.before:
        Color:
            rgba: root.color_toggled if root.toggled else root.color_untoggled
        RoundedRectangle:
            radius: self.height/2,
            size: self.size
            pos: self.pos
    Widget:
        width: root.width/2
        height: root.height-(4)
        y: root.y+(root.height/2)-(self.height/2)
        x: root.x + ((root.width-self.width-4) if root.toggled else 4)
        
        canvas.before:
            Color:
                rgba: root.thumb_color
            Ellipse:
                size: self.size
                pos: self.pos
""")


class CupertinoSwitch(ButtonBehavior, Widget):
    """
    iOS style Switch. To comply with iOS standard, keep the width to height ratio of
    :class:`CupertinoSwitch` at 2:1

    .. image:: ../_static/switch/demo.gif
    """

    toggled = BooleanProperty(False)
    """
    If :class:`CupertinoSwitch` is on
    
    .. image:: ../_static/switch/toggled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(toggled=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           toggled: True
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    Color of thumb of :class:`CupertinoSwitch`
    
    .. image:: ../_static/switch/thumb_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(thumb_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           thumb_color: 1, 0, 0, 1
    """

    color_toggled = ColorProperty([0.3, 0.85, 0.4, 1])
    """
    Background color of :class:`CupertinoSwitch` when on
    
    .. image:: ../_static/switch/color_toggled.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(color_toggled=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           color_toggled: 1, 0, 0, 1
    """

    color_untoggled = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    Background color of :class:`CupertinoSwitch` when off
    
    .. image:: ../_static/switch/color_untoggled.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoSwitch(color_untoggled=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoSwitch:
           color_untoggled: 0.5, 0, 0, 1
    """
