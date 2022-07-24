from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from app.components import ButtonWithSound


class CreatePersonScreen:
    def __init__(self, gui) -> None:
        self.gui = gui

    def draw(self) -> BoxLayout:
        box = BoxLayout(orientation='vertical',
                        size=(600, 200),
                        size_hint=(None, None),
                        pos=(self.gui.layout.center_x-300,
                             self.gui.layout.center_y-200),
                        spacing=10)

        box.add_widget(Label(text='ENTER YOUR NAME HERE',
                             font_size='20px',
                             color=(0, 0, 0, 1),
                             size_hint=(1, None),
                             height=20,
                             text_size=(600, 20),
                             halign='left'))

        textinput = TextInput(text='',
                              halign='center',
                              size_hint=(1, None),
                              height=123,
                              multiline=False,
                              font_size='60px',
                              padding_y=25)
        textinput.bind(text=self.gui._username_changed)
        box.add_widget(textinput)

        buttons_orientation = BoxLayout(orientation='horizontal',
                                        size=(600, 80),
                                        size_hint=(None, None),
                                        spacing=5)
        box.add_widget(buttons_orientation)

        btn_m = ButtonWithSound(text='RETURN',
                                size=(300, 80),
                                font_size='60px',
                                background_color=(0, 0, 0, 0),
                                bold=True,
                                color=(117/255, 117/255, 117/255, 1))
        btn_m.bind(on_press=self.gui.main_menu)
        buttons_orientation.add_widget(btn_m)

        btn_go = ButtonWithSound(text='ACCEPT',
                                 size=(300, 80),
                                 font_size='60px',
                                 background_color=(0, 0, 0, 0),
                                 bold=True,
                                 color=(52/255, 123/255, 169/255, 1))
        btn_go.bind(on_press=self.gui._create_person)
        buttons_orientation.add_widget(btn_go)
        return box
