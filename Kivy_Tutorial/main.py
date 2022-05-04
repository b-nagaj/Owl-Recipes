from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color


# handles mouse click/touch events
class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.6, mode='rgba')  # makes the rectangle red
            self.rectangle = Rectangle(pos=(0, 0), size=(50, 50))  # draw a rectangle in the bottom left of canvas

    def on_touch_down(self, touch):  # when the mouse button is clicked, move the rectangle accordingly and print the x + y coordinates
        self.rectangle.pos = touch.pos
        print("Mouse Down", touch)

    def on_touch_move(self, touch):  # when the mouse is dragged, move the rectangle accordingly and print the x + y coordinates
        self.rectangle.pos = touch.pos
        print("Mouse Move", touch)


# # contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":  # tells the python interpreter that this is the main program
    MyApp().run()
