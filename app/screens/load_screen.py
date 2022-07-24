from app.components import ButtonWithSound
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from datetime import datetime


class LoadScreen:
    def __init__(self, gui) -> None:
        self.gui = gui

    def draw(self) -> BoxLayout:
        box = BoxLayout(orientation='vertical',
                        size=(700, 450),
                        size_hint=(None, None),
                        pos=(self.gui.layout.center_x-300, self.gui.layout.center_y-350))
        box.add_widget(Label(text='Load person menu', font_size='20px',
                             color=(0, 0, 0, 1),
                             height=30, size_hint=(1, 0.1), text_size=(700, 30), halign='left'))

        scroll_view = ScrollView(size_hint=(1, None),
                                 height=400)
        scroll_viewport = GridLayout(cols=2,
                                     size_hint=(1, None),
                                     height=len(self.gui.state.list_persons())*60)
        scroll_view.add_widget(scroll_viewport)
        box.add_widget(scroll_view)

        for person in self.gui.state.list_persons():
            btn = ButtonWithSound(text=person.name,
                                  size_hint=(0.7, None),
                                  height=58,
                                  font_size='48px',
                                  halign='left',
                                  text_size=(490, 58),
                                  background_color=(0, 0, 0, 0),
                                  color=(0, 0, 0, 1),
                                  bold=True)
            btn.person = person
            btn.bind(on_press=self.gui._load_game)
            last_time = Label(text=datetime.strftime(person.date_updated, '%d/%m/%Y'),
                              size_hint=(0.3, None),
                              font_size='36px',
                              height=58,
                              color=(0, 0, 0, 1))
            scroll_viewport.add_widget(btn)
            scroll_viewport.add_widget(last_time)

        btn_m = ButtonWithSound(text='RETURN',
                                font_size='20px',
                                height=50,
                                size_hint=(1, 0.1),
                                text_size=(700, 25),
                                halign='left',
                                background_color=(0, 0, 0, 0),
                                color=(0, 0, 0, 1))
        btn_m.bind(on_press=self.gui.main_menu)
        box.add_widget(btn_m)
        return box
