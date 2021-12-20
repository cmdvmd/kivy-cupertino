"""
Dialogs help alert users to information
"""

from kivy.properties import NumericProperty, StringProperty, ColorProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivycupertino.uix.label import CupertinoLabel
from kivy.lang.builder import Builder
from kivy.core.window import Window

__all__ = [
    'CupertinoDialogButton',
    'CupertinoActionSheet',
    'CupertinoDialog'
]

Builder.load_string("""
#: import root_path kivycupertino.root_path

<_Separator>:
    canvas.before:
        Color:
            rgb: 0.8, 0.8, 0.8
        Rectangle:
            size: self.size
            pos: self.pos

<CupertinoDialogButton>:
    color: root.text_color
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_normal
        RoundedRectangle:
            radius: root._radii
            size: self.size
            pos: self.pos

<CupertinoDialog>:
    _content: content
    _actions: actions
    
    background: root_path + 'transparent.png'
    auto_dismiss: False
    pos_hint: {'center': (0.5, 0.5)}
    
    BoxLayout:
        orientation: 'vertical'
        
        FloatLayout:
            id: content
            
            canvas.before:
                Color:
                    rgba: root.color
                RoundedRectangle:
                    radius: root.curve, root.curve, 0, 0
                    size: self.size
                    pos: self.pos
        _Separator:
            size_hint_y: None
            height: root.spacing
        BoxLayout:
            id: actions
            orientation: 'horizontal'
            pos: root.pos

<CupertinoActionSheet>:
    _actions: actions
    
    background: root_path + 'transparent.png'
    auto_dismiss: False
    size_hint_x: 0.95
    pos_hint: {'center_x': 0.5}
    
    FloatLayout:
        size: root.size
        pos: root.pos
        
        BoxLayout:
            id: actions
            orientation: 'vertical'
            y: cancel.y + cancel.height + 10
            pos_hint: {'center_x': 0.5}
        
        CupertinoDialogButton:
            id: cancel
            _radii: root.curve,
            text: 'Cancel'
            text_color: 0.05, 0.5, 1
            bold: True
            color_normal: root.color_normal
            color_down: root.color_down
            size_hint_y: 0.08
            y: 10
            pos_hint: {'center_x': 0.5}
            on_release: root.dismiss()
""")


class _Separator(Widget):
    pass


class CupertinoDialogButton(ButtonBehavior, CupertinoLabel):
    """
    Adaptive button to be used in Dialogs
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoDialogButton`
    
    .. image:: ../_static/dialog_button/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialogButton(text='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoDialogButton:
           text: 'Hello World'
    """

    font_size = NumericProperty(14)
    """
    Size of text of :class:`CupertinoDialogButton`
    
    .. image:: ../_static/dialog_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialogButton(font_size=20)
   
    **KV**
    
    .. code-block::
    
       CupertinoDialogButton:
           font_size: 20
    """

    color_normal = ColorProperty([1, 1, 1, 0.85])
    """
    Background color of :class:`CupertinoDialogButton` when not pressed
    
    .. image:: ../_static/dialog_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialogButton(color_normal=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoDialogButton:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([1, 1, 1, 0.75])
    """
    Background color of :class:`CupertinoDialogButton` when pressed
    
    .. image:: ../_static/dialog_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialogButton(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoDialogButton:
           color_down: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([0.05, 0.5, 1, 1])
    """
    Color of the text of :class:`CupertinoDialogButton`
    
    .. image:: ../_static/dialog_button/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialogButton(text_color=(1, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoDialogButton:
           color_down: 1, 0, 0, 1
    """

    _radii = ListProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ListProperty` defining the radii values of the corners of :class:`CupertinoDialogButton`
    """


class CupertinoDialog(ModalView):
    """
    iOS style dialog

    .. image:: ../_static/dialog/demo.gif
    """

    color = ColorProperty([1, 1, 1, 0.85])
    """
    Background color of :class:`CupertinoDialog`
    
    .. image:: ../_static/dialog/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialog(color=(1, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoDialog:
           color: 1, 0, 0, 1
    """

    spacing = NumericProperty(1)
    """
    Spacing between :attr:`children` of  :class:`CupertinoDialog`
    
    .. image:: ../_static/dialog/spacing.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialog(spacing=5)
   
    **KV**
    
    .. code-block::
    
       CupertinoDialog:
           spacing: 5
    """

    curve = NumericProperty(10)
    """
    Curve of  :class:`CupertinoDialog`
    
    .. image:: ../_static/dialog/curve.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialog(curve=20)
   
    **KV**
    
    .. code-block::
    
       CupertinoDialog:
           curve: 20
    """

    def __init__(self, **kwargs):
        """
        Initialize :class:`CupertinoDialog`
        """

        super().__init__(**kwargs)

        self._og_size_hint_y = self.size_hint_y
        self.bind(size_hint_y=lambda instance, value: self.__setattr__('_og_size_hint_y', value))

    def _configure_shape(self):
        """
        Configure :attr:`orientation` and placement of actions in the layout
        """

        longest_text = len(self._actions.children[0].text)
        for child in self._actions.children:
            if isinstance(child, CupertinoDialogButton):
                longest_text = max(longest_text, len(child.text))
                child._radii = 0, 0, 0, 0

        orientation = 'vertical' if len(self._actions.children) > 3 or longest_text > 10 else 'horizontal'
        self._actions.orientation = orientation
        for child in self._actions.children:
            if isinstance(child, _Separator):
                if orientation == 'vertical':
                    child.size_hint = (1, None)
                    child.height = self.spacing
                else:
                    child.size_hint = (None, 1)
                    child.width = self.spacing

        if orientation == 'vertical':
            actions_height = Window.height * self._og_size_hint_y * 0.35 * ((len(self._actions.children) + 1) / 2)
            super().__setattr__('size_hint_y', ((Window.height * self._og_size_hint_y * 0.65) + actions_height) / Window.height)
            self._actions.size_hint_y = actions_height / (Window.height * self.size_hint_y)
            self._actions.children[0]._radii[-2:] = self.curve, self.curve
        else:
            self.size_hint_y = self._og_size_hint_y
            self._actions.size_hint_y = 0.35
            self._actions.children[-1]._radii[-2:] = 0, self.curve
            self._actions.children[0]._radii[2] = self.curve

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add :attr:`children` to :class:`CupertinoDialog`

        .. note::
           Instances of :class:`CupertinoDialogButton` will be rendered at the
           bottom of the dialog rather than in the content area
        """

        if len(self.children) >= 1:
            if isinstance(widget, CupertinoDialogButton):
                self._actions.add_widget(widget, index)
                if len(self._actions.children) > 1:
                    self._actions.add_widget(_Separator(size_hint=(None, None), size=(0, 0)), index + 1)
                self._configure_shape()
            else:
                self._content.add_widget(widget, index)
        else:
            super().add_widget(widget, index, canvas)

    def remove_widget(self, widget):
        """
        Remove :attr:`children` from their respective layouts
        """

        if isinstance(widget, CupertinoDialogButton):
            try:
                index = self._actions.children.index(widget)
                if index != len(self._actions.children) - 1:
                    self._actions.remove_widget(self.children[index + 1])
                self._actions.remove_widget(widget)
                self._configure_shape()
            except ValueError:
                return
        else:
            self._content.remove_widget(widget)


class CupertinoActionSheet(ModalView):
    """
    iOS style Action Sheet

    .. image:: ../_static/action_sheet/demo.gif
    """

    color_normal = ColorProperty([1, 1, 1, 0.95])
    """
    Background color of :class:`CupertinoActionSheet` 'Cancel' button when not pressed
    
    .. image:: ../_static/action_sheet/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(color_normal=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([1, 1, 1, 0.8])
    """
    Background color of :class:`CupertinoActionSheet` 'Cancel' button when pressed
    
    .. image:: ../_static/action_sheet/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           color_down: 0.5, 0, 0, 1
    """

    spacing = NumericProperty(1)
    """
    Spacing between :attr:`children` of  :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/spacing.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(spacing=5)
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           spacing: 5
    """

    curve = NumericProperty(10)
    """
    Curve of  :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/curve.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(curve=20)
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           curve: 20
    """

    def _configure_shape(self):
        """
        Configure shape of dialog based on present :attr:`children`
        """

        self._actions.size_hint_y = 0.08 * ((len(self._actions.children) + 1) / 2)

        for b in self._actions.children:
            b._radii = 0, 0, 0, 0
        self._actions.children[0]._radii[2:] = self.curve, self.curve
        self._actions.children[-1]._radii[:2] = self.curve, self.curve

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add an instance of :class:`CupertinoDialogButton` to :class:`CupertinoActionSheet`
        """

        if len(self.children) >= 1:
            assert isinstance(widget,
                              CupertinoDialogButton), 'CupertinoActionSheet accepts only CupertinoDialogButton widget'

            self._actions.add_widget(widget)
            if len(self._actions.children) > 1:
                self._actions.add_widget(_Separator(size_hint_y=None, height=self.spacing), index + 1)
            self._configure_shape()
        else:
            super().add_widget(widget, index, canvas)

    def remove_widget(self, widget):
        """
        Remove :attr:`children` from :class:`CupertinoActionSheet`
        """

        try:
            index = self._actions.children.index(widget)
            if index != len(self._actions.children) - 1:
                self._actions.remove_widget(self.children[index + 1])
            self._actions.remove_widget(widget)
            self._configure_shape()
        except ValueError:
            return
