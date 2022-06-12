from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang.builder import Builder

KV = """
MDTextField:
    hint_text:'Enter Username'
    pos_hint:{"center_x": 0.5, "center_y": 0.5}
    size_hint_x:None
    width;:300


"""


class MainApp(MDApp):
    def build(self):
        screen = MDScreen()

        '''self.username = MDTextField(text="Enter Username",
                                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                                    size_hint_x=None,
                                    width=300
                                    )'''

        self.toolbar = MDToolbar(title="Friendbook")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.anchor_title = "center"
        screen.add_widget(self.toolbar)

        # Buttons
        login_btn = MDFillRoundFlatButton(
            text="login",
            pos_hint={"center_x": 0.4, "center_y": 0.3}

        )

        reg_btn = MDFillRoundFlatButton(
            text="login",
            pos_hint={"center_x": 0.6, "center_y": 0.3}

        )

        # Add to Screen
        screen.add_widget(KV)
        screen.add_widget(login_btn)
        screen.add_widget(reg_btn)

        return screen


if __name__ == "__main__":
    MainApp().run()
