from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import StringProperty, ColorProperty


class SystemButton(ButtonBehavior, Label):
    text = StringProperty('')
    color = ColorProperty([0.1, 0.5, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
