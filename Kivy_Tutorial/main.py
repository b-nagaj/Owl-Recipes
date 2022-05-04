from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    # initialization method (kind of like a constructor)
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)  # initializes the GridLayout object's constructor
        self.cols = 1

        self.inside = GridLayout()  # creates a grid inside of another grid to show the submit button at the bottom center
        self.inside.cols = 2

        # text input into the grid for a first name
        # for each of these text inputs, we add a label, a textbox, then add them to the screen
        self.inside.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        # text input into the grid for a last name
        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        # test input into the grid for an email address
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    # on press event for the submit button
    def pressed(self, instance):
        print("| First: ", self.firstName.text, "| Last: ", self.lastName.text, "| Email: ", self.email.text, "|") # print the user's input to the console

        self.firstName.text = ""  # clear the user's input
        self.lastName.text = ""
        self.email.text = ""


# contains the build method that App utilizes when initialized
class MyApp(App):
    def build(self):
        return MyGrid()  # instantiating the MyGrid object's constructor here


if __name__ == "__main__":  # tells the python interpreter that this is the main program
    MyApp().run()
