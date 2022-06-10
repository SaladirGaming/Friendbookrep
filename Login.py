from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen, MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from helpers import username_helper,password_helper
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDToolbar
from kivymd.app import MDApp
import sqlite3

verbindung = sqlite3.connect("Account_Data.db")



class Friendbook(MDApp):
    def show_data(self, obj):

        if self.username.text or self.password.text is "":
            check_string = 'Ivalid Data'

        else:
            if self.username.text == "Jeremy":
                if self.password.text == "blacky257":
                    check_string = self.username.text + ', schön das du wieder da bist'
                else:
                    check_string = 'Falsches Passwort'
            else:
                check_string = self.username.text + ' does not exist'

        close = MDFlatButton(text='Close', on_release=self.close_dialog)
        more = MDFlatButton(text='More')

        self.dialog = MDDialog(title="Username Check", text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close, more])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def regist_data(self, obj):

        password = str(self.password.text)
        username = str(self.username.text)
        string_data = (username, password)

        zeiger = verbindung.cursor()
        zeiger.execute("Create Table if not exists Account_Data (Username VARCHAR(20), Password VARCHAR(20))")

        zeiger.execute("Insert Into Account_data VALUES(?, ?)", string_data)
        verbindung.commit()
        zeiger.execute("Select Username From Account_Data WHERE Username=?", (username,))
        verbindung.commit()
        inhalt = zeiger.fetchall()
        print(inhalt)
        verbindung.close()

    def build(self):

        screen = Screen()

        self.theme_cls.primary_palette = "Green"

        # Buttons
        login_button = MDRectangleFlatButton(text='Login',
                                             pos_hint={'center_x': 0.35, 'center_y': 0.3},
                                             on_release=self.show_data,
                                             size_hint=(None,None))

        regist_button = MDRectangleFlatButton(text='Register',
                                             pos_hint={'center_x': 0.60, 'center_y': 0.3},
                                             on_release=self.regist_data,
                                             size_hint=(None,None))

        self.username = Builder.load_string(username_helper)
        self.password = Builder.load_string(password_helper)

        # Toolbar

        self.top_toolbar = MDToolbar(title="Friendbook", anchor_title="center")
        self.top_toolbar.pos_hint = {"top": 1}


        # Zum fenster Hinzufügen
        screen.add_widget(login_button)
        screen.add_widget(regist_button)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        screen.add_widget(self.top_toolbar)

        return screen