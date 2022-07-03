from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

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
            self.rotation = Rotate(angle=0, origin=self.center)

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
    radius = 20
    color = (0, 0, 0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.center)
        with self.canvas:
            Color(*self.color)
            Ellipse(size=(self.radius*2, self.radius*2),
                    pos=(self.center_x, self.center_y))


class BulletButton(BoxLayout):

    def __init__(self, **kwargs):
        btn = ButtonWithSound(**kwargs)
        bul = Bullet()
        super().__init__(pos=kwargs.get("pos", (0, 0)),
                         width=kwargs.get("width")+5 +
                         kwargs.get("radius", 10)*2,
                         height=kwargs.get("height"),
                         orientation='horizontal',
                         spacing=5)
        self.add_widget(btn)
        self.add_widget(bul)
