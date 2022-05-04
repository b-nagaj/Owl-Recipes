from kivy.app import App
from kivy.uix.label import Label


# contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return Label(text="I'm new to Kivy")


if __name__ == "__main__":
    MyApp().run()
