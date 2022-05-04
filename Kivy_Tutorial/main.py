from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):               # initialization method (kind of like a constructor
        super(MyGrid, self).__init__(**kwargs)  # initializes the GridLayout object's constructor
        self.cols = 2                           # dictates # of columns in the grid

        # Text input into the grid for a first name
        # for each of these text inputs, we add a label, a textbox, then add them to the screen
        self.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.add_widget(self.firstName)

        # text input into the grid for a last name
        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        # test input into the grid for an email address
        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


# contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return MyGrid()  # instantiating the MyGrid object's constructor here


if __name__ == "__main__": # tells the python interpreter that this is the main program
    MyApp().run()
