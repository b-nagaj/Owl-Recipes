import sys
from kivy.app import App  # import necessary kivy libraries
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout


# handles navigation between different pages
class WindowManager(ScreenManager):
    pass


# default application page
# allows the user to enter login credentials and click the login button for redirection
class LoginWindow(Screen):
    username = ObjectProperty(None)  # declare local variables to store credentials provided by the user
    password = ObjectProperty(None)
    usernameFound = None  # flags for when credentials are successfully found in the text file(s)
    passwordFound = None

    # event handler for clicking the login button
    def loginBtnClick(self):
        if self.username.text == "" or self.password == "":  # test to see if the user provided input
            self.showPopup()
        else:
            self.findCredential("usernames.txt", self.username.text)  # validate the credentials
            self.findCredential("passwords.txt", self.password.text)

            if self.usernameFound is False or self.passwordFound is False:  # if valid - login, if invalid display a popup message
                self.showPopup()
            else:
                self.login()

    # helper function to display the popup message
    def showPopup(self):
        error = IncorrectLoginPopup()
        error.ShowIncorrectLoginPopup()
        self.invalidateCredentials()
        self.clearCredentials()
        App.get_running_app().root.current = "login"  # stay on the login page

    # helper function to login to the application
    def login(self):
        self.invalidateCredentials()
        self.clearCredentials()
        App.get_running_app().root.current = "questionPrompt"  # leave the login page

    # helper function to validate credentials entered by the user
    def findCredential(self, filename, credential):
        with open(filename, 'r') as file:  # process the file
            credentials = file.read().splitlines()

        for c in credentials:  # scan the file for a matching credential
            if c == credential:
                if filename == "usernames.txt":  # if found - mark validated, if not mark invalidated
                    self.usernameFound = True
                else:
                    self.passwordFound = True

        file.close()

    # helper function to reset validations to default
    def invalidateCredentials(self):
        self.usernameFound = False
        self.passwordFound = False

    # helper function to erase the text entered by the user
    def clearCredentials(self):
        self.username.text = ""
        self.password.text = ""


# allows the user to create a new account by entering new login credentials
class CreateAccountWindow(Screen):
    username = ObjectProperty(None)  # declare local variables to store credentials provided by the user
    password = ObjectProperty(None)

    # adds the user's new login credentials to txt files to keep a record of it
    def createAccount(self):
        with open('usernames.txt', 'a') as file:  # add the username
            file.write(self.username.text)
            file.write("\n")
            file.close()

        with open('passwords.txt', 'a') as file:  # add the password
            file.write(self.password.text)
            file.write("\n")
            file.close()


# message displayed to the user when incorrect credentials are provided
class IncorrectLoginPopup(FloatLayout):
    # initializes a new Popup object and opens it
    def ShowIncorrectLoginPopup(self):
        error = IncorrectLoginPopup()
        popupWindow = Popup(title="Error", content=error, size_hint=(None, None), size=(400, 400))
        popupWindow.open()


# allows the user to select from 1 of 3 checkboxes and save their response to be viewed on another screen
class QuestionPromptWindow(Screen):
    # event handler for clicking a checkbox from screen and saving it
    def checkboxClick(self, instance, value, choice):
        if value is True:
            App.get_running_app().root.ids.DisplaySelectedCheckboxWindow.ids.selectedCheckbox.text = choice  # update the DisplaySelectedCheckbox window's label
        else:
            pass


# allows the user to see their choice from the QuestionPromptWindow
class DisplaySelectedCheckboxWindow(Screen):
    # helper function to quit the application
    def exitApp(self):
        sys.exit()


# contains the build method that App utilizes when initialized
class TutorialApp(App):
    def build(self):
        self.root = Builder.load_file("my.kv")
        return self.root


if __name__ == "__main__":  # run as the main program
    TutorialApp().run()
