from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

# event handler for clicking the button on the main page
class Widgets(Widget):
    def btn(self):
        show_popup()

# basic popup window
class P(FloatLayout):
    pass


# contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return Widgets()


# function to open an overlay of the popup window on the main screen
def show_popup():
    show = P()

    popupWindow = Popup(title="New Popup", content=show, size_hint=(None, None), size=(400, 400))  # define a new popup window and initialize it with desired parameters

    popupWindow.open()


if __name__ == "__main__":  # tells the python interpreter that this is the main program
    MyApp().run()
