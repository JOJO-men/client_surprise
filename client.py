from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.button import MDRectangleFlatButton
from urllib import request

count = 1


class Hello(FloatLayout):
    def __init__(self, **kwargs):
        super(Hello, self).__init__(**kwargs)

        self.player1 = None
        self.player = VideoPlayer(source="https://surprise.jojo-men.repl.co/static/sta.mp4")
        self.player.state = 'pause'
        self.player.options = {'eos': 'loop'}
        self.player.allow_stretch = True

        self.btn = MDRectangleFlatButton(text="дальше", pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                         on_release=self.click,
                                         md_bg_color=[1, 1, 1, 1])

        self.add_widget(self.player)
        self.add_widget(self.btn)

        self.current_text = "Default"

    def click(self, event=None):
        global count
        data = "sta.mp4", "rub.mp4", "ang.mp4", "ana.mp4", "rom.mp4", "emi.mp4", "mar.mp4"
        try:

            temp = request.urlopen(f"https://surprise.jojo-men.repl.co/static/{data[count]}", timeout=2).getcode()
            print(temp)
            self.player.disabled = True
            self.player.opacity = 0
            self.player.state = 'pause'
            self.player = VideoPlayer(source=f"https://surprise.jojo-men.repl.co/static/{data[count]}")
            self.player.state = 'pause'
            self.player.options = {'eos': 'loop'}
            self.player.allow_stretch = True
            self.add_widget(self.player)
            self.btn.disabled = True
            self.btn.opacity = 0
            self.btn = MDRectangleFlatButton(text="дальше", pos_hint={'center_x': 0.5, 'center_y': 0.95},
                                             on_release=self.click,
                                             md_bg_color=[1, 1, 1, 1])
            self.add_widget(self.btn)
            count += 1
        except:
            if count < 8:
                count += 1
                print(count)
                self.click()
            else:
                count = 0
                print(count)
                self.click()


class app1(MDApp):
    def build(self):
        return Hello()
