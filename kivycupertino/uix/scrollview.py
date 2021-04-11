"""
ScrollViews help show lots of information within a set screen size

Usage:
------

.. image:: ../../_static/scrollview.gif

.. code-block:: python

    from kivycupertino.app import CupertinoApp
    from kivy.uix.gridlayout import GridLayout
    from kivycupertino.uix.label import CupertinoLabel
    from kivycupertino.uix.scrollview import CupertinoScrollView

    class TestApp(CupertinoApp):

        def build(self):
            scrollview = CupertinoScrollView()
            layout = GridLayout(cols=1, size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))

            for i in range(10):
                layout.add_widget(CupertinoLabel(text=f'Item {i+1}', size_hint_y=None))

            scrollview.add_widget(layout)

            return scrollview

    if __name__ == '__main__':
        app = TestApp()
        app.run()
..

Api:
-----
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
