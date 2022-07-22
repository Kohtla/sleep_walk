from app.components import MenuBoxLayout, ButtonWithSound, RunningLine


class MainMenuScreen:

    def __init__(self, gui):
        self.gui = gui

    def draw(self):
        # TODO: there is a method to find posibility to continue game easier fix that
        pers = [p for p in self.gui.state.list_persons()]
        box = MenuBoxLayout(orientation='vertical',
                            size=(600, 520),
                            size_hint=(None, None),
                            pos=(self.gui.kx*280, self.gui.ky*-40),
                            spacing=1)

        if len(pers) != 0:
            btn_c = ButtonWithSound(text='CONTINUE •',
                                    font_size='96px',
                                    height=100,
                                    width=600,
                                    background_color=(0, 0, 0, 0),
                                    color=(97/256, 17/256, 54/256, 1),
                                    size_hint=(1, None),
                                    halign='right',
                                    bold=True)
            btn_c.text_size = btn_c.size
            btn_c.bind(on_press=self.gui._continue)
            box.add_widget(btn_c)

        btn_ng = ButtonWithSound(text='NEW GAME',
                                 font_size='96px' if len(
                                     pers) == 0 else '60px',
                                 height=100 if len(pers) == 0 else 65,
                                 width=600,
                                 size_hint=(1, None),
                                 background_color=(1, 1, 1, 0),
                                 color=(52/256, 123/256, 169/256, 1),
                                 halign='right',
                                 bold=True)

        btn_ng.text_size = btn_ng.size
        btn_ng.bind(on_press=self.gui.create_person_menu)
        box.add_widget(btn_ng)

        if len(pers) != 0:
            btn_lg = ButtonWithSound(text='LOAD GAME •',
                                     font_size='60px',
                                     height=65,
                                     width=600,
                                     size_hint=(1, None),
                                     background_color=(0, 0, 0, 0),
                                     color=(0, 0, 0, 1),
                                     halign='right',
                                     bold=True)
            btn_lg.text_size = btn_lg.size
            btn_lg.bind(on_press=self.gui.load_person_menu)
            box.add_widget(btn_lg)

        btn_s = ButtonWithSound(text='SETTINGS •',
                                font_size='60px',
                                height=65,
                                width=600,
                                background_color=(1, 1, 1, 0),
                                halign='right',
                                color=(256, 256, 256, 1),
                                size_hint=(1, None),
                                bold=True)
        btn_s.text_size = btn_s.size
        btn_s.bind(on_press=self.gui.open_settings)
        box.add_widget(btn_s)

        btn_e = ButtonWithSound(text='EXIT •',
                                font_size='60px',
                                halign='right',
                                height=65,
                                width=600,
                                size_hint=(1, None),
                                background_color=(0, 0, 0, 0),
                                color=(256, 256, 256, 1),
                                bold=True)
        btn_e.text_size = btn_e.size
        btn_e.bind(on_press=self.gui.stop)
        box.add_widget(btn_e)
        man_alone_line = RunningLine(text="MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE ",
                                     pos=(-440*self.gui.kx, -350*self.gui.ky),
                                     size=(100*self.gui.kx, 24),
                                     angle=20,
                                     font_size='20px',
                                     color=(0, 0, 0, 1))
        soalm_line = RunningLine(text="THE STORY OF A LONELY MAN ",
                                 pos=(-350*self.gui.kx, -250*self.gui.ky),
                                 size=(100*self.gui.kx, 24),
                                 angle=20,
                                 font_size='100px',
                                 color=(0, 0, 0, 1))
        auf_line = RunningLine(text="In this world, is the destiny of mankind controlled by some transcendental entity or law? Is it like the hand of God hovering above? At least it is true that man has no control, even over his own wil",
                               pos=(360*self.gui.kx, 700*self.gui.ky),
                               size=(100*self.gui.kx, 40),
                               angle=-70,
                               font_size='40px',
                               color=(0, 0, 0, 1))
        man_alone_line2 = RunningLine(text="MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE MAN ALONE ",
                                      pos=(390*self.gui.kx, 700*self.gui.ky),
                                      size=(100*self.gui.kx, 40),
                                      angle=-70,
                                      font_size='20px',
                                      color=(0, 0, 0, 1))

        self.gui.layout.add_widget(man_alone_line)
        self.gui.layout.add_widget(man_alone_line2)
        self.gui.layout.add_widget(auf_line)
        self.gui.layout.add_widget(soalm_line)
        return box
