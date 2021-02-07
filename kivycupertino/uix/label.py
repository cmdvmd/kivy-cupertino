from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ColorProperty


class CupertinoLabel(Label):
    text = StringProperty('')
    font_name = StringProperty('San Francisco')
    bold = BooleanProperty(False)
    italic = BooleanProperty(False)
    color = ColorProperty([0, 0, 0, 1])
