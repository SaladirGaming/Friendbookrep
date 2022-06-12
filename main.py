from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang.builder import Builder
from helpers import username_helper, password_helper
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, MDList


class Login(MDApp):
    def build(self):
        pass


class MainApp(MDApp):
    def build(self):
        screen = MDScreen()

        list_view = MDList()

        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)

        self.toolbar = MDToolbar(title="Friendbook")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.anchor_title = "center"
        screen.add_widget(self.toolbar)



        item1= OneLineListItem(text="Item")
        item2 = OneLineListItem(text="Item")

        list_view.add_widget(item1)
        list_view.add_widget(item2)
        screen.add_widget(list_view)
        # Buttons
        login_btn = MDFillRoundFlatButton(
            text="Login",
            pos_hint={"center_x": 0.4, "center_y": 0.3},
            size_hint=(None, None),
            on_release=self.check_data
        )

        reg_btn = MDFillRoundFlatButton(
            text="Register",
            pos_hint={"center_x": 0.6, "center_y": 0.3},
            size_hint=(None, None)

        )

        # Add to Screen
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(login_btn)
        screen.add_widget(reg_btn)

        return screen

    def check_data(self, obj):

        #Ist die Eingabezeile leer?
        if self.username.text is "":
            check_string = "Please enter a username"

        else:
            check_string = self.username.text + " does not exist"

        close_btn = MDFlatButton(text="close", on_release=self.close_dialog)
        more_btn = MDFlatButton(text="more")
        self.dialog = MDDialog(title="Username Check",
                               text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_btn, more_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

        self.dialog.open()
        print(self.username.text)


if __name__ == "__main__":
    MainApp().run()
