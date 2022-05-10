import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class GUI(App):
    layout = BoxLayout()
    game = None

    def __init__(self, game, **kwargs):
        self.game = game
        super().__init__(**kwargs)
        self.main_menu(None)

    def build(self):
        return self.layout
    
    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)
    
    def _continue(self, instance):
        self.game.start(self.game.get_latest_person())
        self.show_level()

    def main_menu(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='SLEEP WALK v 0.2'))

        btn_ng = Button(text='NEW GAME')
        btn_ng.bind(on_press=self.create_person_menu)
        self.layout.add_widget(btn_ng)

        btn_c = Button(text='CONTINUE')
        btn_c.bind(on_press=self._continue)
        self.layout.add_widget(btn_c)

        btn_lg = Button(text='LOAD GAME')
        btn_lg.bind(on_press=self.load_person_menu)
        self.layout.add_widget(btn_lg)

        btn_e = Button(text='EXIT')
        btn_e.bind(on_press=self.stop)
        self.layout.add_widget(btn_e)

    def pause_menu(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='PAUSE'))

        btn_r = Button(text='RESUME')
        btn_r.bind(on_press=self.callback)
        self.layout.add_widget(btn_r)

        btn_m = Button(text='MAIN MENU')
        btn_m.bind(on_press=self.callback)
        self.layout.add_widget(btn_m)

        btn_e = Button(text='EXIT')
        btn_e.bind(on_press=self.callback)
        self.layout.add_widget(btn_e)

    def _username_changed(self, instance, value):
        self.username = value

    def _create_person(self, instance):
        self.game.create_person(self.username)
        self.show_level()

    def create_person_menu(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='CREATE PERSON'))

        textinput = TextInput(text='',)
        textinput.bind(text=self._username_changed)
        self.layout.add_widget(textinput)

        btn_m = Button(text='RETURN')
        btn_m.bind(on_press=self.main_menu)
        self.layout.add_widget(btn_m)

        btn_go = Button(text='CREATE')
        btn_go.bind(on_press=self._create_person)
        self.layout.add_widget(btn_go)

    def _load_game(self, instance):
        self.game.start(instance.person)
        self.show_level()

    def load_person_menu(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='Load person menu'))

        for person in self.game.list_persons():
            btn  = Button(text=person.name)
            btn.person = person
            btn.bind(on_press=self._load_game)
            self.layout.add_widget(btn)

        btn_m = Button(text='RETURN')
        btn_m.bind(on_press=self.main_menu)
        self.layout.add_widget(btn_m)

    def show_titles(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='THE END'))

        btn_m = Button(text='MAIN MENU')
        btn_m.bind(on_press=self.callback)
        self.layout.add_widget(btn_m)

    def show_level(self):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text=self.game.person.name))
