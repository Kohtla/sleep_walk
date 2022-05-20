from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang.builder import Builder

from kivy.core.window import Window
from kivy.app import App
import kivy

from app.init_story import init_story
kivy.require('2.1.0')  # replace with your current kivy version !

class BackGround(Image):
    pass


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class GUI(App):
    layout = RootWidget()
    game = None
    settings = None

    def __init__(self, game, settings, **kwargs):
        self.settings = settings
        self.game = game
        super().__init__(**kwargs)
        self.main_menu()

    def build(self):
        return self.layout

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

    def _continue(self, instance):
        self.game.start(self.game.get_latest_person())
        self.show_level()

    def _init_story(self, instance):
        init_story()

    def main_menu(self, instance=None):
        self.layout.clear_widgets()

        box = BoxLayout(orientation='vertical')
        bg = BackGround(source='img/menu.png', size_hint=(None, None), size=(Window.width, Window.height))
        
        self.layout.add_widget(bg)

        box.add_widget(Label(text='SLEEP WALK v 0.2'))

        btn_ng = Button(text='NEW GAME')
        btn_ng.bind(on_press=self.create_person_menu)
        box.add_widget(btn_ng)

        btn_c = Button(text='CONTINUE')
        btn_c.bind(on_press=self._continue)
        box.add_widget(btn_c)

        btn_lg = Button(text='LOAD GAME')
        btn_lg.bind(on_press=self.load_person_menu)
        box.add_widget(btn_lg)

        btn_e = Button(text='EXIT')
        btn_e.bind(on_press=self.stop)
        box.add_widget(btn_e)

        btn_is = Button(text='Init story')
        btn_is.bind(on_press=self._init_story)
        box.add_widget(btn_is)

        self.layout.add_widget(box)

    def pause_menu(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='PAUSE'))

        btn_r = Button(text='RESUME')
        btn_r.bind(on_press=self.show_level)
        self.layout.add_widget(btn_r)

        btn_m = Button(text='MAIN MENU')
        btn_m.bind(on_press=self.main_menu)
        self.layout.add_widget(btn_m)

        btn_e = Button(text='EXIT')
        btn_e.bind(on_press=self.stop)
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
            btn = Button(text=person.name)
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
        btn_m.bind(on_press=self.main_menu)
        self.layout.add_widget(btn_m)

    def _next_line(self, instance):
        self.game.next_line()
        if self.game.the_end:
            self.show_titles()
        else:
            self.show_level()

    def _make_choice(self, instance):
        self.game.make_choice(instance.choice)
        self.show_level()

    def show_level(self, instance=None):
        self.layout.clear_widgets()
        self.layout.add_widget(Label(text='It is level %s for %s' %
                                     (self.game.level.name, self.game.person.name)))
        self.layout.add_widget(Label(text='%s: %s' % (
            self.game.line.character, self.game.line.text)))

        choices = self.game.get_choices()

        if choices:
            for choice in choices:
                btn = Button(text=choice.text)
                btn.choice = choice
                btn.bind(on_press=self._make_choice)
                self.layout.add_widget(btn)
        else:
            btn = Button(text='NEXT')
            btn.bind(on_press=self._next_line)
            self.layout.add_widget(btn)

        btn_p = Button(text='PAUSE')
        btn_p.bind(on_press=self.pause_menu)
        self.layout.add_widget(btn_p)
