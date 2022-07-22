from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.graphics import PopMatrix, PushMatrix, Rotate, Color, Ellipse, Rectangle


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
    base_color = (0, 0, 0, 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_color = kwargs.get('color', (0, 0, 0, 1))

    def on_press(self):
        ButtonWithSound.fx_sound.play()
        return super().on_press()


class Bullet(Widget):
    color = (0, 0, 0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.x)
        with self.canvas.before:
            Color(*self.color)
            Ellipse(size=self.size)


class BulletButton(BoxLayout):

    def __init__(self, **kwargs):
        btn = ButtonWithSound(**kwargs)
        bul = Bullet(size=kwargs.get("bullet_size", (50, 50)))
        super().__init__(pos=kwargs.get("pos", (0, 0)),
                         width=kwargs.get("width") +
                         kwargs.get("bullet_size", (50, 50))[0],
                         height=kwargs.get("height"),
                         orientation='horizontal')
        self.add_widget(btn)
        print(self.pos)
        self.add_widget(bul)
