import glob
from urllib import parse
from os.path import join, dirname
from kivy.lang import Builder
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from .airbnbmapview import AirbnbMapView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.app import App

from .airbnbmapview import AirbnbMapView
from .components.filterMenu import FilterMenu
import json
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
import requests
import os
from restAPIConnection.restAPIConnection import RestAPIConnection
from kivy.core.window import Window

from kivymd.uix.picker import MDDatePicker


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
                query = obj.text
                query += ' NY United States'
                response = requests.get("http://localhost:8888/search_address",params={'location':query})
                app = App.get_running_app()
                mapview = app.root.ids.mapview
                locations = json.loads(response.text)
                mapview.center_on(locations['lat'], locations['lng'])
                #print(response.text)
        self.dialog.dismiss()

    def close_dialog(self, inst):
        self.dialog.dismiss()

    def show_filter_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(

            )

    def remove_wishlist_superboxes(self):
        children = self.root.ids.supercomparebox.children
        children_copy = children.copy()
        for child in children_copy:
            print(child)
            self.root.ids.supercomparebox.remove_widget(child)
        print(len(children))

    def load_bookmarked(self):
        path = 'bookmarks'
        full_path = os.path.join(os.getcwd(), path)
        for filenames in os.walk(full_path):
            for filename in filenames[2]:
                currentfile = open(os.path.join(full_path, filename),"r")
                data = json.load(currentfile)
                superbox = MDBoxLayout(
                    orientation='vertical'
                )
                imagebox = MDFloatLayout(
                )
                textbox = MDFloatLayout(
                )
                img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
                                 pos_hint={'center_x': .5, 'center_y': .5})
                label = MDLabel(text=f"Price: {data['price']}$/night"
                                     f"\nRoomType: {data['room_type']}"
                                     f"\nListing URL: [ref=www.airbnb.com][color=0000ff]{data['listing_url']}[/color][/ref]",
                                markup=True,
                                halign='center',
                                #on_ref_press= print("test"), #open_link(data['listing_url']),
                                width=250,
                                size_hint=(None, None),
                                pos_hint={'center_x': .5, 'center_y': .5})
                imagebox.add_widget(img)
                textbox.add_widget(label)
                superbox.add_widget(imagebox)
                superbox.add_widget(textbox)
                self.root.ids.supercomparebox.add_widget(superbox)




    pass

def run():
    MainApp().run()

if __name__ == '__main__':
    run()

