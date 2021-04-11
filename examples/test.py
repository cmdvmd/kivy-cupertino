import sys


sys.path.append("..")
from kivycupertino.app import CupertinoApp
from kivycupertino.uix.label import CupertinoLabel
from kivy.uix.screenmanager import SlideTransition, Screen
from kivycupertino.uix.page import CupertinoScreenManager, CupertinoPageControls
from kivy.core.window import Window


class TestApp(CupertinoApp):

    def switch_screen(self, widget, touch):
        if touch.ox-touch.x > 75:
            widget.transition = SlideTransition(direction='left')
            widget.current = widget.next()
            touch.ox = touch.x
        elif touch.x-touch.ox > 75:
            widget.transition = SlideTransition(direction='right')
            widget.current = widget.previous()
            touch.ox = touch.x

    def build(self):
        w = CupertinoScreenManager(on_touch_move=self.switch_screen)
        c = CupertinoPageControls(size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'y': 0.05})
        w.add_widget(c)
        for i in range(5):
            s = Screen(name=str(i))
            s.add_widget(CupertinoLabel(text=f'Screen {i+1}', pos_hint={'center': (0.5, 0.5)}))
            w.add_widget(s)
        return w



    Window.clearcolor = 0.98, 0.98, 0.98, 1


Window.size = (300, 500)

if __name__ == '__main__':
    app = TestApp()
    app.run()
