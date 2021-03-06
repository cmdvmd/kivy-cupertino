"""
Labels display text to users
"""

from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty, ColorProperty


class CupertinoLabel(Label):
    """
    iOS style Label

    .. image:: ../_static/label.png
    """

    text = StringProperty('')
    """
    Text of :class:`~kivycupertino.uix.label.CupertinoLabel`
    
    :attr:`text` is a :class:`~kivy.properties.StringProperty` and defaults to `""`
    """

    font_name = StringProperty('San Francisco')
    """
    Font of :class:`~kivycupertino.uix.label.CupertinoLabel`
    
    :attr:`font_name` is a :class:`~kivy.properties.StringProperty` and defaults to `San Francisco`.
    To comply with iOS standard, use `San Francisco` or `New York`
    """

    bold = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.label.CupertinoLabel` is bold
    
    :attr:`bold` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    italic = BooleanProperty(False)
    """
    If :class:`~kivycupertino.uix.label.CupertinoLabel` is italic
    
    :attr:`italic` is a :class:`~kivy.properties.BooleanProperty` and defaults to `False`
    """

    color = ColorProperty([0, 0, 0, 1])
    """
    Text color of :class:`~kivycupertino.uix.label.CupertinoLabel`
    
    :attr:`color` is a :class:`~kivy.properties.ColorProperty` and defaults to `[0, 0, 0, 1]`
    """
