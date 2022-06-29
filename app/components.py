
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

from kivy.graphics import PopMatrix, PushMatrix, Rotate


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
            self.rotation = Rotate(angle=20, origin=self.center)

        with self.canvas.after:
            PopMatrix()


class ButtonWithSound(Button):
    fx_sound = None
    base_color = (0,0,0,1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_color = kwargs.get('color', (0,0,0,1))

    def on_press(self):
        ButtonWithSound.fx_sound.play()
        return super().on_press()
