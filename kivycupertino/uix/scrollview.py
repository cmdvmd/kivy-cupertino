"""
ScrollViews help show lots of information within a set screen size
"""

from kivy.uix.scrollview import ScrollView
from kivy.properties import ColorProperty
from kivy.lang import Builder

__all__ = [
    'CupertinoScrollView'
]

Builder.load_string("""
<CupertinoScrollView>:
    bar_margin: 2
    bar_width: 4
""")


class CupertinoScrollView(ScrollView):
    """
    iOS style ScrollView

    .. image:: ../_static/scrollview/demo.gif
    """

    bar_color = ColorProperty([0.65, 0.65, 0.65, 1])
    """
    Color of the bar of :class:`CupertinoScrollView` when scrolling
    
    .. image:: ../_static/scrollview/bar_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoScrollview(bar_color=(1, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoScrollview:
           bar_color: 1, 0, 0, 1
    """

    bar_inactive_color = ColorProperty([0, 0, 0, 0])
    """
    Color of the bar of :class:`CupertinoScrollView` when not scrolling
    
    .. image:: ../_static/scrollview/bar_inactive_color.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoScrollview(bar_inactive_color=(0.5, 0, 0, 1))
    
    **KV**
    
    .. code-block::
    
       CupertinoScrollview:
           bar_inactive_color: 0.5, 0, 0, 1
    """
