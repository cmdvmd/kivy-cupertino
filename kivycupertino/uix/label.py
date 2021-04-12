"""
Labels display text to users

Label
-----

.. image:: ../_static/label.png

**Python**

.. code-block:: python

   label = CupertinoLabel(text='Hello World')

**KV**

.. code-block::

   CupertinoLabel:
       text: 'Hello World'
"""

from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty, ColorProperty

__all__ = [
    'CupertinoLabel'
]


class CupertinoLabel(Label):
    """
    iOS style Label
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
