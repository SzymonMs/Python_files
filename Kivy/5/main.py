import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Property
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line

class Touch(Widget):

    def __init__(self,**kwargs):
        super(Touch,self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 1, 0.5, mode="rgba")
            Line(points=(20,30,400,500,60,500))
            Color(0,0,1,0.5,mode="rgba")
            self.Rectangle=Rectangle(pos=(0,0),size=(50,50))
            #Color(1, 1, 0, 0.5, mode="rgba")
            #self.Rectangle = Rectangle(pos=(200, 300), size=(70, 50))

    btn=Property(None)
    def on_touch_down(self, touch):
        print("DOWN",touch)
    def on_touch_move(self, touch):
        self.Rectangle.pos = touch.pos
        print("MOVE",touch)
    def on_touch_up(self, touch):
        print("UP",touch)
class MyApp(App):
    def build(self):
        return Touch()

if __name__=="__main__":
    MyApp().run()