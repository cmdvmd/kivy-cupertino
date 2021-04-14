from kivy.uix.screenmanager import Screen

class ControlShowcaseScreen(Screen):
    
    loaded = False

    def on_pre_enter(self):
        if not self.loaded:
            self.ids.segmented_controls.add_segment("Segmented")
            self.ids.segmented_controls.add_segment("Controls")
            self.loaded = True