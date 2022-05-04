from kivy.app import App  # import kivy components and libraries from kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


# login page
class MainWindow(Screen):
    pass


# page after successful login
class SecondWindow(Screen):
    pass


# manage transitions between the windows
class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")  # process the specified .kv file (doesn't have to match typical naming convention)


# # contains the build method that App utilizes when initialized
class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":  # tells the python interpreter that this is the main program
    MyMainApp().run()
