from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()
