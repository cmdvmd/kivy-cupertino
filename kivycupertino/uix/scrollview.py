"""
ScrollViews help show lots of information within a set screen size

ScrollView
----------

.. image:: ../_static/scrollview.gif

**Python**

.. code-block:: python

   scrollview = CupertinoScrollView()
   layout = GridLayout(cols=1, size_hint_y=None)
   layout.bind(minimum_height=layout.setter('height'))
   scrollview.add_widget(layout)

**KV**

.. code-block::

   CupertinoScrollView:
       GridLayout:
           cols: 1
           size_hint_y: None
           height: self.minimum_height
"""

from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.scrollview import ScrollView

__all__ = ["CupertinoScrollView"]

Builder.load_string(
    """
<CupertinoScrollView>:
    bar_margin: 2
    bar_width: 4
"""
)


class CupertinoScrollView(ScrollView):
    """
    iOS style ScrollView
    """

    bar_color = ColorProperty([0.65, 0.65, 0.65, 1])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of
    :class:`~kivycupertino.uix.scrollview.CupertinoScrollView` when scrolling
    """

    bar_inactive_color = ColorProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ColorProperty` defining the color of the bar of
    :class:`~kivycupertino.uix.scrollview.CupertinoScrollView` when not scrolling
    """
