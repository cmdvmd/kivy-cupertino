"""
Labels display text to users

Usage:
------

.. image:: ../../_static/label.png

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivycupertino.uix.label import CupertinoLabel
    from kivy.uix.floatlayout import FloatLayout

    class TestApp(CupertinoApp):

        def build(self):
            layout = FloatLayout()

            label = CupertinoLabel(text='label', font_name='San Francisco', pos_hint={'center': (0.5, 0.5)})

            layout.add_widget(label)

            return layout

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

Api:
----

"""

from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty, ColorProperty

__all__ = [
    'CupertinoLabel'
]


class CupertinoLabel(Label):
    """
    iOS style Label

    .. image:: ../../_static/label.png
    """

    text = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of
    :class:`~kivycupertino.uix.label.CupertinoLabel`
    """

    font_name = StringProperty('San Francisco')
    """
    A :class:`~kivy.properties.StringProperty` defining the font of
    :class:`~kivycupertino.uix.label.CupertinoLabel`. To comply with iOS standard, use
    `San Francisco` or `New York`
    """

    bold = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.label.CupertinoLabel` is bold
    """

    italic = BooleanProperty(False)
    """
    A :class:`~kivy.properties.BooleanProperty` defining if
    :class:`~kivycupertino.uix.label.CupertinoLabel` is italic
    """

    color = ColorProperty([0, 0, 0, 1])
    """
    A :class:`~kivy.properties.ColorProperty` that deinfes the text color of
    :class:`~kivycupertino.uix.label.CupertinoLabel`
    """
