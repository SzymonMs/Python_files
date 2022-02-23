from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
#W kivy (0,0) jest w dolnym lewym narożniku, nie jak w pygame w górnym

class MyApp(App):
    def build(self):
        return FloatLayout()
if __name__=="__main__":
    MyApp().run()