from turtle import color
import kivy
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from app.init_story import init_story
from kivy.config import Config, ConfigParser
from datetime import datetime

from app.components import BulletButton, RootWidget, ButtonWithSound, BackGround, MenuBoxLayout, AlignedLabel, ChoiceButton, Bullet
from app.screens import MainMenuScreen

# TODO: move somewhere in gui class
Config.set("graphics", "resizable", 0)

kivy.require('2.1.0')  # replace with your current kivy version !


class GUI(App):
    layout = RootWidget()
    state = None
    # TODO: move settings to the separate class
    settings = None
    music = None

    # TODO: move somewhere
    username = ''

    kx = 1
    ky = 1
    last_func = None

    girls_paths = ['img/girl1.png', 'img/girl2.jpg']
    girls_positions = [(0, 5), (40, 20)]

    def mouse_dispatch(self, window, pos):
        for widget in window.children[0].walk():
            if isinstance(widget, ButtonWithSound):
                if widget.collide_point(*pos):
                    widget.color = (1, 0, 0, 1)
                else:
                    widget.color = widget.base_color

    def __init__(self, state, settings, **kwargs):
        self.settings = settings
        self.state = state
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
        self.kx = w/1280
        self.ky = h/720
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
        size = tuple(map(int, config.get("graphics", "resolution").split('x')))
        self.kx = size[0]/1280
        self.ky = size[1]/720
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
                xy = tuple(map(int, value.split('x')))
                self.layout.get_root_window().size = xy
                BackGround.main_size = tuple(map(int, value.split('x')))
                BackGround.update_size()
                self.kx = xy[0]/1280
                self.ky = xy[1]/720
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
        Animation.cancel_all(self.girl_image)
        self.girls_paths = ['img/girl1.png', 'img/girl2.jpg']
        self.girls_positions = [(0, 5), (40, 20)]
        try:
            p = self.settings_popup
            self.last_func()
            p.dismiss()
        except AttributeError:
            pass  # Settings popup doesn't exist

    def callback(self, instance):
        print('The button <%s> is being pressed' % instance.text)

    def _continue(self, instance):
        self.state.start(self.state.get_latest_person())
        self.show_level()

    def _init_story(self, instance):
        init_story()

    # This function changes the source of the image and creates next animation recursively
    def _next_girl_image(self, widget):
        girl_path = self.girls_paths.pop()
        self.girls_paths.insert(0, girl_path)
        widget.source = girl_path
        next_position = self.girls_positions.pop()
        self.girls_positions.insert(0, next_position)
        anim = Animation(d=2,
                         t='in_cubic',
                         opacity=1)
        anim += Animation(d=8,
                          t='in_out_cubic',
                          x=next_position[0]*self.kx,
                          y=next_position[1]*self.ky)
        anim += Animation(d=2,
                          t='in_cubic',
                          opacity=0)
        anim.on_complete = self._next_girl_image

        anim.start(widget)

    def redraw_background(self):
        self.layout.clear_widgets()
        color_img = Image(source="img/colors.png",
                          size_hint=(None, None),
                          size=self.layout.size)
        self.layout.add_widget(color_img)
        self.girl_image = Image(source='img/girl1.png',
                                pos=(40*self.kx, 20*self.ky))

        self.layout.add_widget(self.girl_image)

        anim = Animation(d=8,
                         t='in_out_cubic',
                         x=0*self.kx,
                         y=5*self.ky)
        anim += Animation(d=2,
                          t='in_cubic',
                          opacity=0)
        anim.on_complete = self._next_girl_image
        Animation.cancel_all(self.girl_image)
        anim.start(self.girl_image)

        bg = BackGround(source='img/menu.png',
                        size_hint=(None, None),
                        size=self.layout.size)

        self.layout.add_widget(bg)

    def main_menu(self, instance=None):

        self.last_func = self.main_menu
        # TODO: what that config is doing here, need to replace
        conf = ConfigParser()
        conf.read(self.get_application_config())
        self.layout.size = (conf.get("graphics", "resolution").split(
            'x')[0], conf.get("graphics", "resolution").split('x')[1])
        self.kx = self.layout.size[0]/1280
        self.ky = self.layout.size[1]/720
        self.redraw_background()

        # here we init new main menu object and draw it here
        menu_screen = MainMenuScreen(self)
        box = menu_screen.draw()

        btn_is = ButtonWithSound(text='Init story',
                                 size=(160, 40),
                                 size_hint=(None, None))
        btn_is.bind(on_press=self._init_story)

        self.layout.add_widget(box)
        self.layout.add_widget(btn_is)

    def pause_menu(self, instance=None):
        self.last_func = self.pause_menu

        self.redraw_background()

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
        self.state.create_person(self.username)
        self.show_level()

    def create_person_menu(self, instance):
        self.last_func = self.create_person_menu
        self.redraw_background()

        box = BoxLayout(orientation='vertical',
                        size=(600, 200),
                        size_hint=(None, None),
                        pos=(self.layout.center_x-300,
                             self.layout.center_y-200),
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
        textinput.bind(text=self._username_changed)
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
        btn_m.bind(on_press=self.main_menu)
        buttons_orientation.add_widget(btn_m)

        btn_go = ButtonWithSound(text='ACCEPT',
                                 size=(300, 80),
                                 font_size='60px',
                                 background_color=(0, 0, 0, 0),
                                 bold=True,
                                 color=(52/255, 123/255, 169/255, 1))
        btn_go.bind(on_press=self._create_person)
        buttons_orientation.add_widget(btn_go)
        self.layout.add_widget(box)

    def _load_game(self, instance):
        self.state.start(instance.person)
        self.show_level()

    def load_person_menu(self, instance):
        self.last_func = self.load_person_menu
        self.redraw_background()
        box = BoxLayout(orientation='vertical',
                        size=(700, 450),
                        size_hint=(None, None),
                        pos=(self.layout.center_x-300, self.layout.center_y-350))
        box.add_widget(Label(text='Load person menu', font_size='20px',
                             color=(0, 0, 0, 1),
                             height=30, size_hint=(1, 0.1), text_size=(700, 30), halign='left'))

        scroll_view = ScrollView(size_hint=(1, None),
                                 height=400)
        scroll_viewport = GridLayout(cols=2,
                                     size_hint=(1, None),
                                     height=len(self.state.list_persons())*60)
        scroll_view.add_widget(scroll_viewport)
        box.add_widget(scroll_view)

        for person in self.state.list_persons():
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
            btn.bind(on_press=self._load_game)
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
        self.state.next_line()
        if self.state.the_end:
            self.show_titles()
        else:
            self.show_level()

    def _make_choice(self, instance):
        self.state.make_choice(instance.choice)
        self.show_level()

    def show_level(self, instance=None):
        self.redraw_background()
        self.layout.add_widget(AlignedLabel(text='It is level %s for %s' %
                                            (self.state.level.name,
                                             self.state.person.name),
                                            pos=(self.kx*20, self.ky*680),
                                            halign='left'))
        self.layout.add_widget(AlignedLabel(text='%s: %s' % (self.state.line.character, self.state.line.text),
                                            pos=(self.kx*180, self.ky*190),
                                            halign='left'
                                            ))

        choices = self.state.get_choices()

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
