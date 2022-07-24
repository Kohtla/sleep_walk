from app.components import ButtonWithSound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class PauseScreen:
    def __init__(self, gui) -> None:
        self.gui = gui

    def draw(self) -> BoxLayout:
        box = BoxLayout(orientation='vertical',
                        size=(200, 200),
                        size_hint=(None, None),
                        spacing=5,
                        pos=(self.gui.layout.center_x-100, self.gui.layout.center_y-100))

        box.add_widget(Label(text='PAUSE'))

        btn_r = ButtonWithSound(text='RESUME',
                                height=95)
        btn_r.bind(on_press=self.gui.show_level)
        box.add_widget(btn_r)

        btn_m = ButtonWithSound(text='MAIN MENU',
                                height=95)
        btn_m.bind(on_press=self.gui.main_menu)
        box.add_widget(btn_m)

        btn_s = ButtonWithSound(text="SETTINGS",
                                height=95)
        btn_s.bind(on_press=self.gui.open_settings)
        box.add_widget(btn_s)

        btn_e = ButtonWithSound(text='EXIT',
                                height=95)
        btn_e.bind(on_press=self.gui.stop)
        box.add_widget(btn_e)

        return box
