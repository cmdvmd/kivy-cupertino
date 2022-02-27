"""
Labels display text to users
"""

from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ColorProperty

__all__ = [
    'CupertinoLabel'
]


class CupertinoLabel(Label):
    """
    iOS style Label

    .. image:: ../_static/label/demo.png
    """

    text = StringProperty(' ')
    """
    A :class:`~kivy.properties.StringProperty` defining the text of :class:`CupertinoLabel`
    
    .. image:: ../_static/label/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(text='Hello World')
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           text: 'Hello World'
    """

    font_name = StringProperty('San Francisco')
    """
    Font of :class:`CupertinoLabel`. To comply with iOS standard, use `San Francisco` or `New York`
    
    .. image:: ../_static/label/font_name.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(font_name='New York')
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           font_name: 'New York'
    """

    font_size = NumericProperty('15sp')
    """
    Size of the font of :class:`CupertinoLabel`
    
    .. image:: ../_static/label/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(font_size='20sp')
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           font_size: '20sp'
    """

    bold = BooleanProperty(False)
    """
    If :attr:`text` :class:`CupertinoLabel` is bold
    
    .. image:: ../_static/label/bold.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(bold=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           bold: True
    """

    italic = BooleanProperty(False)
    """
    If :attr:`text` of :class:`CupertinoLabel` is italic
    
    .. image:: ../_static/label/italic.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(italic=True)
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           italic: True
    """

    color = ColorProperty([0, 0, 0, 1])
    """
    Color of :attr:`text` :class:`CupertinoLabel`
    
    .. image:: ../_static/label/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoLabel(color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoLabel:
           color: 1, 0, 0, 1
    """
