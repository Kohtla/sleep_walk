import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from app.init_story import init_story
from kivy.config import Config, ConfigParser

from app.components import RootWidget, ButtonWithSound, BackGround, MenuBoxLayout, AlignedLabel, ChoiceButton

# TODO: move somewhere in gui class
Config.set("graphics", "resizable", 0)

kivy.require('2.1.0')  # replace with your current kivy version !


class GUI(App):
    layout = RootWidget()
    game = None
    settings = None
    music = None

    # TODO: move somewhere
    username = ''

    kx = 1
    ky = 1
    last_func = None

    def mouse_dispatch(self, window, pos):
        for widget in window.children[0].walk():
            if isinstance(widget, Button):
                if widget.collide_point(*pos):
                    widget.font_size = "17sp"
                else:
                    widget.font_size = "15sp"

    def __init__(self, game, settings, **kwargs):
        self.settings = settings
        self.game = game
        super().__init__(**kwargs)
        self.music = SoundLoader.load("audio/game_music.mp3")
        ButtonWithSound.fx_sound = SoundLoader.load("audio/try_fx_sound.ogg")
        self.music.loop = True
        Window.left = 50
        Window.top = 50
        Window.bind(mouse_pos=self.mouse_dispatch)
        self.main_menu()

    def build(self):
        self.settings_cls = SettingsWithTabbedPanel
        self.use_kivy_settings = False
        w, h = map(int, self.config.get("graphics", "resolution").split('x'))
        Window.size = (w, h)
        if self.config.get("graphics", "fullscreen") == "yes":
            Window.fullscreen = True
        else:
            Window.fullscreen = False
        self.music.play()
        return self.layout

    def get_application_config(self, defaultpath='config/config.ini'):
        return super().get_application_config(defaultpath)

    def build_config(self, config):
        config.read("config/config.ini")
        self.music.volume = float(config.get("audio", "music_volume"))/100
        ButtonWithSound.fx_sound.volume = float(
            config.get("audio", "fx_volume"))/100
        super().build_config(config)

    def build_settings(self, settings):
        settings.add_json_panel("Settings", self.config,
                                "settings/settings.json")
        return super().build_settings(settings)

    def on_config_change(self, config, section, key, value):
        if section == "graphics":
            if key == "fullscreen":
                if value == "yes":
                    self.layout.get_root_window().fullscreen = True
                else:
                    self.layout.get_root_window().fullscreen = False
            if key == "vsync":
                # TODO: enable VSync somehow
                pass
            if key == "resolution":
                self.layout.get_root_window().size = tuple(map(int, value.split('x')))
                BackGround.main_size = tuple(map(int, value.split('x')))
                BackGround.update_size()
        if section == "audio":
            if key == "music_volume":
                self.music.volume = int(value) / 100
            if key == "fx_volume":
                ButtonWithSound.fx_sound.volume = int(value) / 100
        if section == "lang":
            # TODO: set current localization
            pass
        return super().on_config_change(config, section, key, value)

    def display_settings(self, settings):
        try:
            p = self.settings_popup
        except AttributeError:
            self.settings_popup = Popup(content=settings,
                                        title='Settings',
                                        size_hint=(0.8, 0.8))
            p = self.settings_popup
        if p.content is not settings:
            p.content = settings
        p.open()

    def close_settings(self, *args):
        try:
            p = self.settings_popup
            self.last_func()
            p.dismiss()
        except AttributeError:
            pass  # Settings popup doesn't exist

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

    def _continue(self, instance):
        self.game.start(self.game.get_latest_person())
        self.show_level()

    def _init_story(self, instance):
        init_story()

    def main_menu(self, instance=None):
        self.layout.clear_widgets()

        self.last_func = self.main_menu

        conf = ConfigParser()
        conf.read(self.get_application_config())
        self.layout.size = (conf.get("graphics", "resolution").split(
            'x')[0], conf.get("graphics", "resolution").split('x')[1])
        self.kx = self.layout.size[0]/1280
        self.ky = self.layout.size[1]/720
        box = MenuBoxLayout(orientation='vertical',
                            size=(200, 200),
                            size_hint=(None, None),
                            pos=(self.kx*700, self.ky*100),
                            spacing=5)
        bg = BackGround(source='img/menu.png',
                        size_hint=(None, None),
                        size=self.layout.size)

        self.layout.add_widget(bg)

        btn_ng = ButtonWithSound(text='NEW GAME',
                                 height=80,
                                 background_color=(0, 0, 0, 0),
                                 color=(256, 256, 256, 1))
        btn_ng.bind(on_press=self.create_person_menu)
        box.add_widget(btn_ng)

        btn_c = ButtonWithSound(text='CONTINUE',
                                height=80,
                                background_color=(0, 0, 0, 0),
                                color=(256, 256, 256, 1),
                                halign='left')
        btn_c.bind(on_press=self._continue)
        box.add_widget(btn_c)

        btn_lg = ButtonWithSound(text='LOAD GAME',
                                 height=80,
                                 background_color=(0, 0, 0, 0),
                                 color=(256, 256, 256, 1))
        btn_lg.bind(on_press=self.load_person_menu)
        box.add_widget(btn_lg)

        btn_s = ButtonWithSound(text='SETTINGS',
                                height=80,
                                background_color=(0, 0, 0, 0),
                                color=(256, 256, 256, 1))
        btn_s.bind(on_press=self.open_settings)
        box.add_widget(btn_s)

        btn_e = ButtonWithSound(text='EXIT',
                                height=80,
                                background_color=(0, 0, 0, 0),
                                color=(256, 256, 256, 1))
        btn_e.bind(on_press=self.stop)
        box.add_widget(btn_e)

        btn_is = ButtonWithSound(text='Init story',
                                 size=(160, 40),
                                 size_hint=(None, None))
        btn_is.bind(on_press=self._init_story)

        self.layout.add_widget(box)
        self.layout.add_widget(btn_is)

    def pause_menu(self, instance=None):
        self.last_func = self.pause_menu

        self.layout.clear_widgets()

        box = BoxLayout(orientation='vertical',
                        size=(200, 200),
                        size_hint=(None, None),
                        spacing=5,
                        pos=(self.layout.center_x-100, self.layout.center_y-100))

        box.add_widget(Label(text='PAUSE'))

        btn_r = ButtonWithSound(text='RESUME',
                                height=95)
        btn_r.bind(on_press=self.show_level)
        box.add_widget(btn_r)

        btn_m = ButtonWithSound(text='MAIN MENU',
                                height=95)
        btn_m.bind(on_press=self.main_menu)
        box.add_widget(btn_m)

        btn_s = ButtonWithSound(text="SETTINGS",
                                height=95)
        btn_s.bind(on_press=self.open_settings)
        box.add_widget(btn_s)

        btn_e = ButtonWithSound(text='EXIT',
                                height=95)
        btn_e.bind(on_press=self.stop)
        box.add_widget(btn_e)

        self.layout.add_widget(box)

    def _username_changed(self, instance, value):
        self.username = value

    def _create_person(self, instance):
        if self.username == '':
            close_btn = ButtonWithSound(text='OK')
            popup = Popup(title='Person\'s name cannot be empty!',
                          size=(300, 100),
                          content=close_btn,
                          size_hint=(None, None),
                          auto_dismiss=True)
            close_btn.bind(on_press=popup.dismiss)
            popup.open()
            return
        self.game.create_person(self.username)
        self.show_level()

    def create_person_menu(self, instance):
        self.last_func = self.create_person_menu
        self.layout.clear_widgets()

        box = BoxLayout(orientation='vertical',
                        size=(200, 200),
                        size_hint=(None, None),
                        pos=(self.layout.center_x-100,
                             self.layout.center_y-100),
                        spacing=5)

        box.add_widget(Label(text='CREATE PERSON'))

        textinput = TextInput(text='',)
        textinput.bind(text=self._username_changed)
        box.add_widget(textinput)

        buttons_orientation = BoxLayout(orientation='horizontal',
                                        size=(200, 50),
                                        size_hint=(None, None),
                                        spacing=5)
        box.add_widget(buttons_orientation)

        btn_m = ButtonWithSound(text='RETURN',
                                size=(100, 50))
        btn_m.bind(on_press=self.main_menu)
        buttons_orientation.add_widget(btn_m)

        btn_go = ButtonWithSound(text='CREATE',
                                 size=(100, 50))
        btn_go.bind(on_press=self._create_person)
        buttons_orientation.add_widget(btn_go)
        self.layout.add_widget(box)

    def _load_game(self, instance):
        self.game.start(instance.person)
        self.show_level()

    def load_person_menu(self, instance):
        self.last_func = self.load_person_menu
        self.layout.clear_widgets()
        box = BoxLayout(orientation='vertical',
                        size=(200, 200),
                        size_hint=(None, None))
        box.add_widget(Label(text='Load person menu'))

        for person in self.game.list_persons():
            btn = ButtonWithSound(text=person.name)
            btn.person = person
            btn.bind(on_press=self._load_game)
            box.add_widget(btn)

        btn_m = ButtonWithSound(text='RETURN')
        btn_m.bind(on_press=self.main_menu)
        box.add_widget(btn_m)
        self.layout.add_widget(box)

    def _set_lang(self, id):
        print(id)

    def show_titles(self):
        self.layout.clear_widgets()
        box = BoxLayout(orientation='vertical',
                        size=(200, 200),
                        size_hint=(None, None))
        box.add_widget(Label(text='THE END'))

        btn_m = ButtonWithSound(text='MAIN MENU')
        btn_m.bind(on_press=self.main_menu)
        box.add_widget(btn_m)
        self.layout.add_widget(box)

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
        self.layout.add_widget(AlignedLabel(text='It is level %s for %s' %
                                            (self.game.level.name,
                                             self.game.person.name),
                                            pos=(self.kx*20, self.ky*680),
                                            halign='left'))
        self.layout.add_widget(AlignedLabel(text='%s: %s' % (self.game.line.character, self.game.line.text),
                                            pos=(self.kx*180, self.ky*190),
                                            halign='left'
                                            ))

        choices = self.game.get_choices()

        if choices:
            box_height = 40 * len(choices)
            box = BoxLayout(orientation='vertical',
                            size=(600, box_height),
                            size_hint=(None, None),
                            pos=(self.kx*180, self.ky*(190 - box_height)),
                            spacing=2)
            for choice in choices:
                btn = ChoiceButton(text=choice.text,
                                   background_color=(1, 1, 1, 1),
                                   halign='left',
                                   valign='center')
                btn.choice = choice
                btn.bind(on_press=self._make_choice)
                box.add_widget(btn)
            self.layout.add_widget(box)
        else:
            btn = ButtonWithSound(text='NEXT',
                                  size=(160, 160),
                                  size_hint=(None, None),
                                  pos=(1000*self.kx, 50*self.ky))
            btn.bind(on_press=self._next_line)
            self.layout.add_widget(btn)

        btn_p = ButtonWithSound(text='PAUSE',
                                size=(160, 40),
                                size_hint=(None, None))
        btn_p.bind(on_press=self.pause_menu)
        self.layout.add_widget(btn_p)
