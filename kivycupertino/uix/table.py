"""
Tables help organize data and information for users to view and interact with
"""

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivycupertino.uix.behavior import CupertinoButtonBehavior
from kivy.properties import ColorProperty, NumericProperty, BooleanProperty, StringProperty
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoTableCell',
    'CupertinoClickableTableCell',
    'CupertinoTableGroup'
]

Builder.load_string("""
<CupertinoTableCell>:
    canvas.before:
        Color:
            rgba: self.color
        Rectangle:
            size: self.size
            pos: 0, 0
        Color:
            rgb: 0.9, 0.9, 0.9
        Rectangle:
            size: dp(self.width * self._upper_border), dp(1)
            pos: self.width * (1 - self._upper_border), 0
        Rectangle:
            size: dp(self.width * self._lower_border), dp(1)
            pos: self.width * (1 - self._lower_border), self.height

<CupertinoClickableTableCell>:    
    CupertinoSymbol:
        symbol: 'chevron_right'
        color: 0.75, 0.75, 0.8, 1
        size_hint: None, 0.4
        width: self.height
        pos_hint: {'right': 0.97, 'center_y': 0.5}

<CupertinoTableGroup>:
    orientation: 'vertical'
    
    CupertinoLabel:
        text: (' ' * 4) + root.text
        font_size: '12sp'
        text_size: self.size
        halign: 'left'
        color: root.text_color
        size_hint_y: 0.95
""")


class CupertinoTableCell(RelativeLayout):
    """
    iOS style Cell for Table View. :class:`CupertinoTableCell` is a
    :class:`~kivy.uix.relativelayout.RelativeLayout` and can accept any number of widgets

    .. image:: ../_static/table_cell/demo.png
    """

    color = ColorProperty([1, 1, 1, 1])
    """
    Background color of :class:`CupertinoTableCell`
    
    .. image:: ../_static/table_cell/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTableCell(color=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoNavigationBar:
           CupertinoTableCell: 1, 0, 0, 1
    """

    _upper_border = NumericProperty(1)
    """
    Percentage of upper border to be drawn in interval [0, 1]
    """

    _lower_border = NumericProperty(1)
    """
    Percentage of lower border to be drawn in interval [0, 1]
    """


class CupertinoClickableTableCell(CupertinoButtonBehavior, CupertinoTableCell):
    """
    iOS style clickable Cell for Table View. :class:`CupertinoClickableTableCell` is a
    :class:`~kivy.uix.relativelayout.RelativeLayout` and can accept any number of widgets

    .. image:: ../_static/clickable_table_cell/demo.gif
    """

    disabled = BooleanProperty(False)
    """
    If :class:`CupertinoClickableTableCell` is disabled
    
    .. image:: ../_static/clickable_table_cell/disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableTableCell(disabled=True)
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableTableCell:
           disabled: True
    """

    transition_duration = NumericProperty(0.075)
    """
    Duration of the transition of the color of :class:`CupertinoButton` when its state changes
    
    .. image:: ../_static/clickable_table_cell/transition_duration.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableTableCell(transition_duration=0.5)
       
    **KV**
    
    .. code-block::

       CupertinoClickableTableCell:
           transition_duration: 0.5
    """

    color_normal = ColorProperty([1, 1, 1, 1])
    """
    Background color of :class:`CupertinoClickableTableCell` when not pressed or disabled
    
    .. image:: ../_static/clickable_table_cell/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableTableCell(color_normal=(1, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableTableCell:
           color_normal: 1, 0, 0, 1
    """

    color_down = ColorProperty([0.9, 0.9, 0.9, 0.9])
    """
    Background color of :class:`CupertinoClickableTableCell` when pressed
    
    .. image:: ../_static/clickable_table_cell/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoClickableTableCell(color_down=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::

       CupertinoClickableTableCell:
           color_down: 0.5, 0, 0, 1
    """

    color_disabled = ColorProperty([0.8, 0.8, 0.8, 1])
    """
    Background color of :class:`CupertinoClickableTableCell` when disabled
    
    .. image:: ../_static/clickable_table_cell/color_disabled.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoTableCell(disabled=True, color_disabled=(0.5, 0, 0, 1))
   
    **KV**
   
    .. code-block::
    
       CupertinoClickableTableCell:
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
    Background color of :class:`CupertinoClickableTableCell` when disabled
    
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
    Background color of :class:`CupertinoClickableTableCell` when disabled
    
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
        Add an instance of :class:`CupertinoTableCell` to :class:`CupertinoTableGroup`

        :param widget: Instance of :class:`CupertinoTableCell` to be added to :class:`CupertinoTableGroup`
        :param index: Index at which :class:`CupertinoTableCell` will be inserted into :attr:`children` of :class:`CupertinoTableGroup`
        :param canvas: Canvas at which :class:`CupertinoTableCell` will be inserted into :class:`CupertinoTableGroup`
        """

        super().add_widget(widget, index, canvas)
        smallest = len(self.children) - 1
        largest = 0
        for index, child in enumerate(self.children):
            if isinstance(child, CupertinoTableCell):
                child._upper_border = 0.95
                child._lower_border = 0.95

                if index < smallest:
                    smallest = index
                if index > largest:
                    largest = index
        self.children[smallest]._upper_border = 1
        self.children[largest]._lower_border = 1
