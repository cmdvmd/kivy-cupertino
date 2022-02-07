"""
Modals help alert users to information
"""

from kivy.properties import NumericProperty, StringProperty, ColorProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivycupertino.uix.label import CupertinoLabel
from kivy.core.window import Window
from kivy.lang.builder import Builder

__all__ = [
    'CupertinoModalButton',
    'CupertinoDialog',
    'CupertinoActionSheet'
]

Builder.load_string("""
#: import root_path kivycupertino.root_path
#: import BoxLayout kivy.uix.boxlayout.BoxLayout

<Separator>:
    canvas.before:
        Color:
            rgb: 0.8, 0.8, 0.8
        Rectangle:
            size: self.size
            pos: self.pos

<CupertinoModalButton>:
    color: root.text_color
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_normal
        RoundedRectangle:
            radius: root._radii
            size: self.size
            pos: self.pos

<CupertinoModal>:
    background: root_path + 'transparent.png'
    overlay_color: 0, 0, 0, 0.45
    auto_dismiss: False

<CupertinoDialog>:
    _content: content
    _actions: actions
    _instantiated: isinstance(root._actions, BoxLayout) and bool(root._actions.children)
    
    BoxLayout:
        orientation: 'vertical'
           
        FloatLayout:
            id: content
            size_hint_y: None
            
            canvas.before:
                Color:
                    rgba: root.color
                RoundedRectangle:
                    radius: (root.curve, root.curve, 0, 0) if root._instantiated else (root.curve,) * 4 
                    size: self.size
                    pos: self.pos
        Separator:
            size_hint_y: None
            height: root.spacing if root._instantiated else 0
        BoxLayout:
            id: actions
            orientation: 'horizontal'
            size_hint_y: None
            pos: root.pos

<ActionSheetLabel>:
    halign: 'center'
    font_size: 11
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]

<CupertinoActionSheet>:
    _message_frame: message_frame
    _actions: actions
    _show_frame: (root.title).strip() or (root.message).strip()
    
    size_hint_x: 0.95
    
    FloatLayout:
        size: root.size
        pos: root.pos
        
        GridLayout:
            id: message_frame
            cols: 1
            padding: (30, 10, 30, 20) if len(self.children) > 2 else (30, 10)
            spacing: 10
            size_hint_y: None
            height: self.minimum_height if self.children else 0
            pos: frame_separator.x, frame_separator.y + frame_separator.height

            canvas.before:
                Color:
                    rgba: root.color_normal
                RoundedRectangle:
                    radius: root.curve, root.curve, 0, 0
                    size: self.size
                    pos: self.pos
        Separator:
            id: frame_separator
            size_hint_y: None
            height: root.spacing if root._show_frame else 0
            pos: actions.x, actions.y + actions.height
        BoxLayout:
            id: actions
            orientation: 'vertical'
            size_hint_y: None
            y: cancel.y + cancel.height + 10
            pos_hint: {'center_x': 0.5}
        CupertinoModalButton:
            id: cancel
            _radii: root.curve,
            text: 'Cancel'
            text_color: 0.05, 0.5, 1
            bold: True
            color_normal: root.color_normal
            color_down: root.color_down
            size_hint_y: None
            height: root.action_height
            y: 10
            pos_hint: {'center_x': 0.5}
            on_release: root.dismiss()
""")


class Separator(Widget):
    """
    A widget to separate instances of :class:`CupertinoModalButton` when added to an instance of :class:`CupertinoModal`
    """


class CupertinoModalButton(ButtonBehavior, CupertinoLabel):
    """
    Adaptive button to be used in Dialogs

    .. image:: ../_static/modal_button/demo.gif
    """

    text = StringProperty(' ')
    """
    Text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/text.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(text='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           text: 'Hello World'
    """

    font_size = NumericProperty(14)
    """
    Size of text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/font_size.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(font_size=20)
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           font_size: 20
    """

    color_normal = ColorProperty([1, 1, 1, 0.9])
    """
    Background color of :class:`CupertinoModalButton` when not pressed
    
    .. image:: ../_static/modal_button/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(color_normal=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([0.9, 0.9, 0.9, 1])
    """
    Background color of :class:`CupertinoModalButton` when pressed
    
    .. image:: ../_static/modal_button/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_down: 0.5, 0, 0, 1
    """

    text_color = ColorProperty([0.05, 0.5, 1, 1])
    """
    Color of the text of :class:`CupertinoModalButton`
    
    .. image:: ../_static/modal_button/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoModalButton(text_color=(1, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoModalButton:
           color_down: 1, 0, 0, 1
    """

    _radii = ListProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ListProperty` defining the radii values of the corners of :class:`CupertinoModalButton`
    """


class CupertinoModal(ModalView):
    """
    Base class for iOS style modals with separate content and actions
    """

    def remove_widget(self, widget):
        """
        Remove :attr:`children` from instance of :class:`CupertinoModal`

        :param widget: :class:`Widget` to be removed from :class:`CupertinoModal`
        """

        if isinstance(widget, CupertinoModalButton):
            try:
                index = self._actions.children.index(widget)
                if index != len(self._actions.children) - 1:
                    self._actions.remove_widget(self._actions.children[index + 1])
                self._actions.remove_widget(widget)
                self._configure_shape()
            except ValueError:
                return
        else:
            self._content.remove_widget(widget)


class CupertinoDialog(CupertinoModal):
    """
    iOS style dialog that dynamically adapts to the amount of actions (:class:`CupertinoModalButton`) it has

    .. image:: ../_static/dialog/demo.gif
    """

    color = ColorProperty([1, 1, 1, 0.9])
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

    action_height = NumericProperty(40)
    """
    Height of :class:`CupertinoModalButton` when added to :class:`CupertinoDialog`
    
    .. image:: ../_static/dialog/action_height.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoDialog(action_height=75)
   
    **KV**
    
    .. code-block::
    
       CupertinoDialog:
           action_height: 75
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
        super().__init__(**kwargs)
        self._content.height = (Window.height * self.size_hint_y) if self.size_hint_y is not None else self.height
        self.size_hint_y = None
        self._configure_shape()

    def _configure_shape(self):
        """
        Update size of :class:`CupertinoDialog` and the orientation of its actions
        """

        if self._actions.children:
            longest_text = len(self._actions.children[0].text)
            for child in self._actions.children:
                if isinstance(child, CupertinoModalButton):
                    longest_text = max(longest_text, len(child.text))
                    child._radii = 0, 0, 0, 0

            orientation = 'vertical' if len(self._actions.children) > 3 or longest_text > 10 else 'horizontal'
            self._actions.orientation = orientation
            for child in self._actions.children:
                if isinstance(child, Separator):
                    if orientation == 'vertical':
                        child.size_hint = 1, None
                        child.height = self.spacing
                    else:
                        child.size_hint = None, 1
                        child.width = self.spacing

            if orientation == 'vertical':
                self._actions.height = ((len(self._actions.children) + 1) / 2) * self.action_height
                self._actions.children[0]._radii[-2:] = (self.curve,) * 2
            elif orientation == 'horizontal':
                self._actions.height = self.action_height
                self._actions.children[-1]._radii[3] = self.curve
                self._actions.children[0]._radii[2] = self.curve

            self.height = self._content.height + self._actions.height

    def on_size_hint_y(self, instance, value):
        """
        Set value of :attr:`size_hint_y` without affecting :attr:`_og_size_hint_y`

        :param instance: Instance of :class:`CupertinoDialog`
        :param value: Value :attr:`size_hint_y` should be set to
        """

        if self.children and value is not None:
            self._content.height = Window.height * value
            self.size_hint_y = None
            self._configure_shape()

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add a widget to :class:`CupertinoDialog`, adding instances of :class:`CupertinoModalButton`
        to actions at bottom of the dialog

        :param widget: Instance of :class:`kivy.uix.Widget` to add to :class:`CupertinoDialog`
        :param index: Index of :attr:`children` to add :param widget: to
        :param canvas: Canvas to add :param widget: to
        """

        if len(self.children) >= 1:
            if isinstance(widget, CupertinoModalButton):
                self._actions.add_widget(widget, index)
                if len(self._actions.children) > 1:
                    self._actions.add_widget(Separator(size_hint=(None, None), size=(0, 0)), index + 1)
                self._configure_shape()
            else:
                self._content.add_widget(widget, index)
        else:
            super().add_widget(widget, index, canvas)


class ActionSheetLabel(CupertinoLabel):
    """
    Label for message frame of :class:`CupertinoActionSheet` that wraps text
    """


class CupertinoActionSheet(CupertinoModal):
    """
    iOS style Action Sheet

    .. image:: ../_static/action_sheet/demo.gif
    """

    title = StringProperty(' ')
    """
    Title shown in message frame of :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/title.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(title='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           title: 'Hello World'
    """

    message = StringProperty(' ')
    """
    Message shown in message frame of :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/message.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(message='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           message: 'Hello World'
    """

    text_color = ColorProperty([0.6, 0.6, 0.6, 1])
    """
    Color of :attr:`title` and :attr:`message` shown in message frame of :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/text_color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(text_color=[1, 0, 0, 1])
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           text_color: 1, 0, 0, 1
    """

    color_normal = ColorProperty([1, 1, 1, 0.9])
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

    color_down = ColorProperty([0.9, 0.9, 0.9, 1])
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

    action_height = NumericProperty(45)
    """
    Height of :class:`CupertinoModalButton` when added to :class:`CupertinoActionSheet`
    
    .. image:: ../_static/action_sheet/action_height.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(action_height=75)
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           action_height: 75
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

    def __init__(self, **kwargs):
        """
        Initialize variables of :class:`CupertinoActionSheet`

        :param kwargs: Keyword arguments for :class:`CupertinoActionSheet`
        """

        super().__init__(**kwargs)

        self._title_label = ActionSheetLabel(bold=True, color=self.text_color)
        self._message_label = ActionSheetLabel(color=self.text_color)

    def _configure_shape(self):
        """
        Configure shape of dialog based on present :attr:`children`
        """

        if self._actions.children:
            self._actions.height = ((len(self._actions.children) + 1) / 2) * self.action_height

            for b in self._actions.children:
                b._radii = 0, 0, 0, 0
            self._actions.children[0]._radii[2:] = self.curve, self.curve
            self._actions.children[-1]._radii[:2] = (0, 0) if self._show_frame else (self.curve, self.curve)

    def on_text_color(self, instance, value):
        """
        Callback when :attr:`text_color` is changed

        :param instance: Instance of :class:`CupertinoActionSheet`
        :param value: New value of :attr:`text_color`
        """

        self._title_label.color = value
        self._message_label.color = value

    def on_title(self, instance, value):
        """
        Callback when :attr:`title` is changed

        :param instance: Instance of :class:`CupertinoActionSheet`
        :param value: New value of :attr:`title`
        """

        self._title_label.text = value
        if self._title_label.parent is None:
            self._message_frame.add_widget(self._title_label, 1)
        elif not value.strip():
            self._title_label.parent.remove_widget(self._title_label)
        self._configure_shape()

    def on_message(self, instance, value):
        """
        Callback when :attr:`message` is changed

        :param instance: Instance of :class:`CupertinoActionSheet`
        :param value: New value of :attr:`message`
        """

        self._message_label.text = value
        if self._message_label.parent is None:
            self._message_frame.add_widget(self._message_label)
        elif not value.strip():
            self._message_label.parent.remove_widget(self._message_label)
        self._configure_shape()

    def add_widget(self, widget, index=0, canvas=None):
        """
        Add an instance of :class:`CupertinoModalButton` to :class:`CupertinoActionSheet`
        """

        if len(self.children) >= 1:
            assert isinstance(widget,
                              CupertinoModalButton), 'CupertinoActionSheet accepts only CupertinoModalButton widget'

            self._actions.add_widget(widget, index)
            if len(self._actions.children) > 1:
                self._actions.add_widget(Separator(size_hint_y=None, height=self.spacing), index + 1)
            self._configure_shape()
        else:
            super().add_widget(widget, index, canvas)
