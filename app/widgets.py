from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.settings import SettingsWithTabbedPanel

from kivy.graphics import PopMatrix, PushMatrix, Rotate
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.app import App
import kivy
kivy.require('2.1.0')  # replace with your current kivy version !


class BackGround(Image):
    main_size = (1280, 1920)
    backgrounds = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        BackGround.backgrounds.append(self)
    
    def update_size():
        for b in BackGround.backgrounds:
            b.size = BackGround.main_size


class AlignedLabel(Label):
    def on_size(self, *args):
        self.text_size = self.size


class ChoiceButton(Button):
    def on_size(self, *args):
        self.text_size = self.size


class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class MenuBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            PushMatrix()
            self.rotation = Rotate(angle=22.57, origin=self.center)

        with self.canvas.after:
            PopMatrix()
    
class ButtonWithSound(Button):
    fx_sound = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_press(self):
        ButtonWithSound.fx_sound.play()
        return super().on_press()