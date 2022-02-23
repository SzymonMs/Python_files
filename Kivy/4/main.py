import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Property
from kivy.graphics import Rectangle
from kivy.graphics import Color

class Touch(Widget):
    btn=Property(None)
    def on_touch_down(self, touch):
        print("DOWN",touch)
        #self.btn.opacity=0.5
    def on_touch_move(self, touch):
        print("MOVE",touch)
    def on_touch_up(self, touch):
        print("UP",touch)
        #self.btn.opacity = 1
class MyApp(App):
    def build(self):
        return Touch()

if __name__=="__main__":
    MyApp().run()