from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


# handles mouse click/touch events
class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):  # when the mouse button is clicked, print x + y coordinates
        print("Mouse Down", touch)
        self.btn.opacity = 0.5  # highlight when clicked

    def on_touch_move(self, touch):  # when the mouse is dragged, print x + y coordinates
        print("Mouse Move", touch)

    def on_touch_up(self, touch):  # when the mouse button is released, print x + y coordinates
        print("Mouse Up", touch)
        self.btn.opacity = 1  # remove highlighting when released


# # contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":  # tells the python interpreter that this is the main program
    MyApp().run()
