
import os
import requests
import json
from kivy.app import App
from kivy.uix.image import AsyncImage
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.boxlayout import MDBoxLayout
from frontend.listingDetail import RoundedCornerLayout
from frontend.components import ListingSaveButton


class CompareScreen(MDBoxLayout):

    def remove_wishlist_superboxes(self):
        children = self.children
        children_copy = children.copy()
        for child in children_copy:
            self.remove_widget(child)

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
                self.add_widget(superbox)



