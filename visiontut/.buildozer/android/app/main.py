from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class works(FloatLayout):

    def __init__(self):
        super().__init__()

        self.camobj = Camera(play=True, index=0, resolution=(1000,1000))
        self.add_widget(self.camobj)

        self.flip = Button(text="Switch to different camera")
        self.flip.bind(on_press=self.camflip)
        self.flip.size_hint = (.5, .1)
        self.add_widget(self.flip)

        self.flip = Button(text="Capture")
        self.flip.bind(on_press=self.take)
        self.flip.pos_hint={'right': 1}
        self.flip.size_hint = (.5, .1)
        self.add_widget(self.flip)

    def take(self, f):
        self.camobj.export_to_png('lower.png')
        print('work')

    def camflip(self, f):
        if self.camobj.index == 0:
            self.camobj.index = 1
        elif self.camobj.index == 1:
            self.camobj.index = 0

class Cam(App):
    def build(self):
        return works()

if __name__ == '__main__':
    Cam().run()