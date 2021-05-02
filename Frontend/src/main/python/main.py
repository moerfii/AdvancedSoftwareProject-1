from urllib import parse

from kivy.lang import Builder
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from airbnbmapview import AirbnbMapView
from kivymd.uix.picker import MDDatePicker

from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Content(BoxLayout):
    pass


class MainApp(MDApp):
    dialog = None
    search_menu = None

    def on_start(self):
        self.fps_monitor_start()

    def build(self):

        self.theme_cls.primary_palette = "DeepOrange"
        # self.theme_cls.theme_style = "Dark" #darkmode
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]
        
    def show_datepicker(self):
        picker = MDDatePicker()
        picker.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        picker.open()

    def on_save(self, instance, value, date_range):
        pass

    def on_cancel(self, value, date_range):
        pass

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Search:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.theme_cls.primary_color, on_release=self.grab_text
                    ),
                ],
            )
        self.dialog.get_normal_height()
        self.dialog.open()

    def grab_text(self, inst):
        for obj in self.dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
        self.dialog.dismiss()

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def show_filter_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(

            )

    pass



MainApp().run()


