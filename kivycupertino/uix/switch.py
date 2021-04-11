"""
Switches allow users to toggle settings off/on

Usage:
------

.. image:: ../../_static/switch.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.switch import CupertinoSwitch
    from kivy.uix.floatlayout import FloatLayout

    class TestApp(CupertinoApp):

        def update(self, bar):
            bar.value += 1

        def build(self):
            layout = FloatLayout()

            switch = CupertinoSwitch(size_hint=[0.25, 0.1], pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(switch)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()

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
            rgba: root.background_toggled if root.toggled else root.background_untoggled
        RoundedRectangle:
            radius: self.height/2.27,
            size: self.size
            pos: self.pos
    Widget:
        width: root.width/2
        height: root.height-(root.padding*2)
        y: root.y+(root.height/2)-(self.height/2)
        x: root.x + ((root.width-self.width-root.padding) if root.toggled else root.padding)
        
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
    :class:`~kivycupertino.uix.switch.CupertinoSwitch` at 2:1
    """

    toggled = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.switch.CupertinoSwitch` is on
    """

    thumb_color = ColorProperty([1, 1, 1, 1])
    """
    A :class:`~kivy.properties.ColorProperty` that degines the color of thumb of
    :class:`~kivycupertino.uix.switch.CupertinoSwitch`
    """

    background_toggled = ColorProperty([0.3, 0.85, 0.4, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.switch.CupertinoSwitch` when on
    """

    background_untoggled = ColorProperty([0.95, 0.95, 0.95, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the background color of
    :class:`~kivycupertino.uix.switch.CupertinoSwitch` when off
    """

    padding = NumericProperty(2)
    """
    A :class:`~kivy.properties.ColorProperty` defining the padding around the thumb of
    :class:`~kivycupertino.uix.switch.CupertinoSwitch`
    """
