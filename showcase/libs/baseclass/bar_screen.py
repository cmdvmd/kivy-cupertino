from kivy.uix.screenmanager import Screen

class BarShowcaseScreen(Screen):
    loaded = False

    def on_pre_enter(self):
        if not self.loaded:
            self.ids.tab_bar.add_tab('Stars', 'star_fill')
            self.ids.tab_bar.add_tab('People', 'person_circle')
            self.ids.tab_bar.add_tab('Recents', 'clock_fill')
            self.loaded = True