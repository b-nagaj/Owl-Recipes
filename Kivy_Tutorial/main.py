from kivy.app import App  # import kivy components and libraries from kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    firstName = ObjectProperty(None)  # no object property until the kv file is read
    lastName = ObjectProperty(None)
    email = ObjectProperty(None)

    def submitBtn(self):
        print("| First: ", self.firstName.text, "| Last: ", self.lastName.text, "| Email: ", self.email.text, "|")  # print the user's input to the console

        self.firstName.text = ""  # clear the user's input
        self.lastName.text = ""
        self.email.text = ""

# contains the build method that Kivy's App library utilizes when initialized
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__": # tells the python interpreter that this is the main program
    MyApp().run()
