import glob
from urllib import parse
from os.path import join, dirname

from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


from kivymd.app import MDApp

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton, MDRectangleFlatIconButton, MDFillRoundFlatIconButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.picker import MDDatePicker

from .components.ListingSaveButton import ListingSaveButton
from .listingDetail import RoundedCornerLayout
from .components.filtering.filterMenu import FilterMenu
from .components.form.form import Form
import json
import requests
import os

from .airbnbmapview import AirbnbMapView
from restAPIConnection.restAPIConnection import RestAPIConnection





class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Content(BoxLayout):
    pass


class BaseWidget(MDFloatLayout):
    pass



class MainApp(MDApp):
    dialog = None
    search_menu = None
    api=RestAPIConnection()

    def on_start(self):
        self.fps_monitor_start()
        #print(self)
        form = self.root.ids.form
        form.on_start()
        
    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.font_styles["JetBrainsMono"] = [
            "JetBrainsMono",
            16,
            False,
            0.15,
        ]
    def option_callback(self, text_of_the_option):
        #print(text_of_the_option)
        pass

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
            #print(child)
            self.root.ids.supercomparebox.remove_widget(child)
        #print(len(children))

    def load_bookmarked(self):
        path = 'bookmarks'
        full_path = os.path.join(os.getcwd(), path)
        for filenames in os.walk(full_path):
            for filename in filenames[2]:
                currentfile = open(os.path.join(full_path, filename),"r")
                data = json.load(currentfile)
                superbox = RoundedCornerLayout(

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

    def load_results(self):
        path = 'bookmarks'
        
        full_path = os.path.join(os.getcwd(), path)
        for filenames in os.walk(full_path):
            for filename in filenames[2]:
                currentfile = open(os.path.join(full_path, filename), "r")
                data = json.load(currentfile)

                superbox = SmartTileWithLabel(
                    size_hint_y= None,
                    height= "240dp",
                    source = data['picture_url'],
                    text=f"Price: {data['price']}$/night"
                         f"\nRoomType: {data['room_type']}"
                         f"\nBorough: {data['neighbourhood_group_cleansed']}"

                )
                print('here')
                bookmarkbutton = ListingSaveButton(data)
                superbox.add_widget(bookmarkbutton)
                self.root.ids.imagelist.add_widget(superbox)



    pass

def run():
    MainApp().run()

if __name__ == '__main__':
    run()

