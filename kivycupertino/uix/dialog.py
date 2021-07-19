"""
Dialogs help alert users to information
"""

from kivy.properties import NumericProperty, StringProperty, ColorProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivycupertino.uix.label import CupertinoLabel
from kivy.lang.builder import Builder
from re import sub

__all__ = [
    'CupertinoActionSheet',
    'CupertinoAlertDialog'
]

Builder.load_string("""
#: import root_path kivycupertino.__init__.root_path

<_CupertinoDialogButton>:
    color: root.text_color
    markup: True
    
    canvas.before:
        Color:
            rgba: root.color_down if self.state == 'down' else root.color_normal
        RoundedRectangle:
            radius: root.radii
            size: self.size
            pos: self.pos

<CupertinoActionSheet>:
    _actions: actions
    
    background: root_path+'transparent.png'
    background_color: 0, 0, 0, 0.5
    auto_dismiss: False
    size_hint_x: 0.95
    pos_hint: {'center_x': 0.5}
    
    FloatLayout:
        size: root.size
        pos: root.pos
        
        BoxLayout:
            id: actions
            orientation: 'vertical'
            spacing: 2
            size_hint_y: 0
            pos_hint: {'center_x': 0.5}
            y: cancel.y+cancel.height+10
            
            canvas.before:
                Color:
                    rgb: 0.9, 0.9, 0.9
                RoundedRectangle:
                    radius: root.curve,
                    size: self.size
                    pos: self.pos
        _CupertinoDialogButton:
            id: cancel
            radii: root.curve,
            text: 'Cancel'
            text_color: 0.05, 0.5, 1
            color_normal: root.color_normal
            color_down: root.color_down
            size_hint_y: 0.09
            pos_hint: {'center_x': 0.5, 'y': 0.02}
            on_release: root.dismiss()

<CupertinoAlertDialog>:
    _actions: actions
    
    background: root_path+'transparent.png'
    background_color: 0, 0, 0, 0.5
    auto_dismiss: False
    size_hint: 0.8, 0.3
    pos_hint: {'center': (0.5, 0.5)}
    
    canvas:
        Color:
            rgba: self.color
        RoundedRectangle:
            radius: self.curve,
            size: self.size
            pos: self.pos
            
    FloatLayout:
        size: root.size
        pos: root.pos
        
        CupertinoLabel:
            id: title
            text: root.title
            font_size: 15
            halign: 'center'
            bold: True
            text_size: self.width-20, None
            pos_hint: {'center_x': 0.5, 'top': 1.3}
        CupertinoLabel:
            id: content
            text: root.content
            font_size: 12
            halign: 'center'
            text_size: self.width-20, None
            pos_hint: {'center_x': 0.5}
            y: title.y-title.texture_size[1]-20
        BoxLayout:
            id: actions
            orientation: 'horizontal'
            spacing: 1
            padding: 0, 1, 0, 0
            size_hint_y: 0.25
            pos: root.pos
            
            canvas.before:
                Color:
                    rgb: 0.9, 0.9, 0.9
                RoundedRectangle:
                    radius: 0, 0, root.curve, root.curve
                    size: self.size
                    pos: self.pos
""")


class _CupertinoDialogButton(ButtonBehavior, CupertinoLabel):
    """
    Adaptive button to be used in Dialogs
    """

    text = StringProperty(' ')
    """
    Text of :class:`_CupertinoDialogButton`
    """

    color_normal = ColorProperty()
    """
    Background color of :class:`_CupertinoDialogButton` when not pressed
    """

    color_down = ColorProperty()
    """
    Background color of :class:`_CupertinoDialogButton` when pressed
    """

    text_color = ColorProperty([0.05, 0.5, 1, 1])
    """
    Text of :class:`_CupertinoDialogButton` when not pressed
    """

    radii = ListProperty([0, 0, 0, 0])
    """
    A :class:`~kivy.properties.ListProperty` defining the radii values of :class:`_CupertinoDialogButton`
    """


class CupertinoActionSheet(ModalView):
    """
    iOS style Action Sheet

    .. image:: ../_static/action_sheet/demo.gif
    """

    color_normal = ColorProperty([1, 1, 1, 0.95])
    """
    Background color of the actions of :class:`CupertinoActionSheet` when not pressed
    
    .. image:: ../_static/action_sheet/color_normal.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(color_normal=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           color_normal: 0.5, 0, 0, 1
    """

    color_down = ColorProperty([1, 1, 1, 0.5])
    """
    Background color of the actions of :class:`CupertinoActionSheet` when pressed
    
    .. image:: ../_static/action_sheet/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoActionSheet(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoActionSheet:
           color_down: 0.5, 0, 0, 1
    """

    curve = NumericProperty(12)
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

    def add_action(self, text, action):
        """
        Add an action to :class:`dialog.CupertinoActionSheet`

        :param text: Text of action. :attr:`markup` is enabled
        :param action: Callback to be performed, bound to attr:`on_release` of action

        .. note::
           Actions can only be added to :class:`CupertinoActionSheet`
           in Python, not KV

        .. code-block:: python

           action_sheet = CupertinoActionSheet()
           action_sheet.add_action('[color=ff0000]Action[/color]', callback)
           action_sheet.add_action('Sheet', callback)
        """

        button = _CupertinoDialogButton(
            text=text,
            color_normal=self.color_normal,
            color_down=self.color_down,
            on_release=action
        )
        self._actions.size_hint_y += 0.1
        self._actions.add_widget(button)

        for b in self._actions.children:
            b.radii = 0, 0, 0, 0
        self._actions.children[0].radii[2:] = self.curve, self.curve
        self._actions.children[-1].radii[:2] = self.curve, self.curve


class CupertinoAlertDialog(ModalView):
    """
    iOS style Alert Dialog

    .. image:: ../_static/alert_dialog/demo.gif
    """

    title = StringProperty(' ')
    """
    Text of title of :class:`CupertinoAlertDialog`
    
    .. image:: ../_static/alert_dialog/title.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoAlertDialog(title='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoAlertDialog:
           title: 'Hello World'
    """

    content = StringProperty(' ')
    """
    Text of content of :class:`CupertinoAlertDialog`
    
    .. image:: ../_static/alert_dialog/content.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoAlertDialog(content='Hello World')
   
    **KV**
    
    .. code-block::
    
       CupertinoAlertDialog:
           content: 'Hello World'
    """

    color = ColorProperty([1, 1, 1, 0.95])
    """
    Background color of :class:`CupertinoAlertDialog`
    
    .. image:: ../_static/alert_dialog/color.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoAlertDialog(color=(1, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoAlertDialog:
           color: 1, 0, 0, 1
    """

    color_down = ColorProperty([0.9, 0.9, 0.9, 1])
    """
    Background color of action of :class:`CupertinoAlertDialog` when pressed
    
    .. image:: ../_static/alert_dialog/color_down.gif
    
    **Python**
    
    .. code-block:: python
    
       CupertinoAlertDialog(color_down=(0.5, 0, 0, 1))
   
    **KV**
    
    .. code-block::
    
       CupertinoAlertDialog:
           color_down: 0.5, 0, 0, 1
    """

    curve = NumericProperty(15)
    """
    Curve of  :class:`CupertinoAlertDialog`
    
    .. image:: ../_static/alert_dialog/curve.png
    
    **Python**
    
    .. code-block:: python
    
       CupertinoAlertDialog(curve=20)
   
    **KV**
    
    .. code-block::
    
       CupertinoAlertDialog:
           curve: 20
    """

    def add_action(self, text, action):
        """
        Add an action to :class:`CupertinoAlertDialog`

        :param text: Text of action. ``markup`` is enabled
        :param action: Callback to be performed, bound to ``on_release`` of action
        """

        self._actions.add_widget(_CupertinoDialogButton(
            text=text,
            color_normal=self.color,
            color_down=self.color_down,
            on_release=action
        ))

        if len(self._actions.children) > 2 or len(sub(r'\[.*?]', '', text)) > 10:
            self._actions.orientation = 'vertical'

        if self._actions.orientation == 'vertical':
            self.size_hint_y += 0.05
            self._actions.size_hint_y += 0.05

            self._actions.children[0].radii[-2:] = [self.curve, self.curve]
            for button in self._actions.children[1:]:
                button.radii = [0, 0, 0, 0]
        else:
            self._actions.children[-1].radii[-2:] = (0, self.curve)
            self._actions.children[0].radii[2] = self.curve
