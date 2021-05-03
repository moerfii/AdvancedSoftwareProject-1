from urllib import parse
from os.path import join, dirname
from kivy.lang import Builder
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.app import App
from airbnbmapview import AirbnbMapView
import json
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
import requests
from restAPIConnection import RestAPIConnection

from kivy.core.window import Window
from components.customCluster import CLUSTER_CLICKED
#Window.fullscreen = 'auto'
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Content(BoxLayout):
    pass


class MainApp(MDApp):
    dialog = None
    search_menu = None
    api=RestAPIConnection()

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
                query=obj.text
                query+=' NY United States'
                response = requests.get("http://localhost:8888/search_address",params={'location':query})
                app = App.get_running_app()
                mapview = app.root.ids.mapview
                locations = json.loads(response.text)
                mapview.center_on(locations['lat'],locations['lng'])
                #print(response.text)
        self.dialog.dismiss()

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def show_filter_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(

            )

    pass

print("boi")
print(join(dirname(__file__), "icons", "cluster.png"))
MainApp().run()


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

    def on_cancel(Self, value, date_range):
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


