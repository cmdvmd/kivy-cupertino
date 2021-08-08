"""
Tables help organize data and information for users to view and interact with
"""

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty, StringProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoCell',
    'CupertinoClickableCell',
    'CupertinoTableGroup'
]

Builder.load_string("""
<CupertinoCell>:
    canvas.before:
        Color:
            rgba: self.color
        Rectangle:
            size: self.size
            pos: self.pos
        Color:
            rgb: 0.9, 0.9, 0.9
        Rectangle:
            size: self.width*self._upper_border, 1
            pos: (self.x+self.width)-(self.width*self._upper_border), self.y
        Rectangle:
            size: self.width*self._lower_border, 1
            pos: (self.x+self.width)-(self.width*self._lower_border), self.y+self.height

<CupertinoClickableCell>:
    color: self.color_down if self.state == 'down' else self.color_disabled if self.disabled else self.color_normal
    CupertinoLabel:
        text: '›'
        font_size: 25
        color: 0.75, 0.75, 0.8, 1
        size_hint_x: 0.01
        pos_hint: {'right': 0.95, 'center_y': 0.5}

<CupertinoTableGroup>:
    orientation: 'vertical'
    
    CupertinoLabel:
        id: label
        text: (' '*4)+root.text
        font_size: 12
        text_size: self.size
        halign: 'left'
        color: root.text_color
        size_hint_y: 0.95
""")


class CupertinoCell(FloatLayout):
    """
    iOS style Cell for Table View. :class:`CupertinoCell` is a
    :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

    .. image:: ../_static/cell/demo.png
    """

    color = ColorProperty([1, 1, 1, 1])
    """
    Background color of :class:`CupertinoCell`
    
    .. image:: ../_static/cell/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoCell(color=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoNavigationBar:
           CupertinoCell: 1, 0, 0, 1
    """

    _upper_border = NumericProperty(1)
    """
    Percentage of upper border to be drawn in interval [0, 1]
    """

    _lower_border = NumericProperty(1)
    """
    Percentage of lower border to be drawn in interval [0, 1]
    """


class CupertinoClickableCell(ButtonBehavior, CupertinoCell):
    """
    iOS style clickable Cell for Table View. :class:`CupertinoClickableCell` is a
    :class:`~kivy.uix.floatlayout.FloatLayout` and can accept any number of widgets

    .. image:: ../_static/clickable_cell/demo.gif
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoClickableCell` is disabled
    
    .. image:: ../_static/clickable_cell/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableCell(disabled=True)
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableCell:
           disabled: True
    """

    color_normal = ColorProperty([1, 1, 1, 1])
    """
    Background color of :class:`CupertinoClickableCell` when not pressed or disabled
    
    .. image:: ../_static/clickable_cell/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableCell(color_normal=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableCell:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0, 0, 0, 0.1])
    """
    Background color of :class:`CupertinoClickableCell` when pressed
    
    .. image:: ../_static/clickable_cell/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableCell(color_down=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::

       CupertinoClickableCell:
           color_down: 0.5, 0, 0, 1
    """

    color_disabled = ColorProperty([0, 0, 0, 0.3])
    """
    Background color of :class:`CupertinoClickableCell` when disabled
    
    .. image:: ../_static/clickable_cell/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoCell(disabled=True, color_disabled=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableCell:
           disabled: True
           color_disabled: 0.5, 0, 0, 1
    """


class CupertinoTableGroup(BoxLayout):
    """
    iOS style table group

    .. image:: ../_static/table_group/demo.png
    """

    text = StringProperty(' ')
    """
    Background color of :class:`CupertinoClickableCell` when disabled
    
    .. image:: ../_static/table_group/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTableGroup(text='Example Group')
   
    **KV**
   
    .. code-block::
    
       CupertinoTableGroup:
           text: 'Example Group'
    """

    text_color = ColorProperty([0.6, 0.6, 0.6, 1])
    """
    Background color of :class:`CupertinoClickableCell` when disabled
    
    .. image:: ../_static/table_group/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTableGroup(text_color=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoTableGroup:
           text_color: 1, 0, 0, 1
    """

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add an instance of :class:`CupertinoCell` to :class:`CupertinoTableGroup`

        :param widget: Instance of :class:`CupertinoCell` to be added to :class:`CupertinoTableGroup`
        :param index: Index at which :class:`CupertinoCell` will be inserted into attr:`children` of :class:`CupertinoTableGroup`
        :param canvas: Canvas at which :class:`CupertinoCell` will be inserted into :class:`CupertinoTableGroup`
        """

        super().add_widget(widget, index, canvas)
        smallest = len(self.children) - 1
        largest = 0
        for index, child in enumerate(self.children):
            if isinstance(child, CupertinoCell):
                child._upper_border = 0.95
                child._lower_border = 0.95

                if index < smallest:
                    smallest = index
                if index > largest:
                    largest = index
        self.children[smallest]._upper_border = 1
        self.children[largest]._lower_border = 1
