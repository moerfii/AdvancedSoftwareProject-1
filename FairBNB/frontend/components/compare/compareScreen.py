
import os
import webbrowser

import requests
import json
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget
from kivymd.uix.card import MDSeparator
from kivymd.uix.chip import MDChip
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.boxlayout import MDBoxLayout
from frontend.listingDetail import RoundedCornerLayout

from frontend.components.ListingSaveButton import ListingSaveButton


def open_link(url):
    webbrowser.open(url)


class CompareScreen(MDBoxLayout):

    def remove_wishlist_superboxes(self):
        children = self.ids.comparebox.children
        print(children)
        children_copy = children.copy()
        for child in children_copy:
            print(child)
            self.ids.comparebox.remove_widget(child)
        print(len(children))

    def load_bookmarked(self):
        self.best_price = 10000000000000000000000000
        self.best_rating = 0
        best_price_box = []
        best_rating_box = []

        path = 'bookmarks'
        full_path = os.path.join(os.getcwd(), path)
        for filenames in os.walk(full_path):
            for filename in filenames[2]:
                currentfile = open(os.path.join(full_path, filename),"r")
                data = json.load(currentfile)



                superbox = MDBoxLayout(
                    size_hint_y=None,
                    height="240dp",
                    orientation = "horizontal",
                    padding = [dp(4), dp(4)],
                    spacing = dp(4)

                )
                imagebox = MDFloatLayout(
                size_hint = [0.75,1]
                )
                textbox = MDFloatLayout(
                )
                img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
                                    pos_hint={'center_x': .5, 'center_y': .5},
                                 size_hint= (1,1))
                label = MDLabel(text=
                                f"{data['room_type']}"
                                f"\n[b]{data['price']}$[/b]/night",
                                markup=True,
                                halign='left',
                                # TODO: make url button
                                # on_ref_press= print("test"), #open_link(data['listing_url']),
                                width=250,
                                size_hint=(None, None),
                                pos_hint={'center_x': .30, 'center_y': .5})

                line = MDSeparator(height = dp(1))

                if data['price'] <= self.best_price:
                    self.best_price = data['price']
                    best_price_box.append(textbox)
                if float(data['review_score']) / 20 >= self.best_rating:
                    self.best_rating = float(data['review_score']) / 20
                    best_rating_box.append(textbox)

                superhost_chip = MDChip(
                    text='SUPERHOST',
                    pos_hint={'center_x': .20, 'center_y': .90},
                    icon='',
                    color=[1, 1, 1, 1],
                )

                staricon = MDIcon(
                    icon='star',
                    pos_hint={'center_x': .5, 'center_y': .76}
                )
                starlabel = MDLabel(
                    text=f"[b]{float(data['review_score']) / 20}[/b] ({data['number_of_reviews']})", markup=True,
                    pos_hint={'center_x': .58, 'center_y': .75}
                )

                webbutton = MDIconButton(
                    icon='search-web',
                    on_press=lambda x: open_link(data['listing_url']),
                    user_font_size="36sp",
                    pos_hint={'center_x': .90, 'center_y': .15}
                )

                bookmarkbutton = ListingSaveButton(
                    data,
                    pos_hint={'center_x': .90, 'center_y': .87},
                    opposite_colors= False,
                    icon = 'delete'
                )
                imagebox.add_widget(img)
                if data['is_superhost']:
                    imagebox.add_widget(superhost_chip)
                imagebox.add_widget(bookmarkbutton)
                textbox.add_widget(staricon)
                textbox.add_widget(starlabel)
                textbox.add_widget(webbutton)
                textbox.add_widget(label)
                superbox.add_widget(imagebox)
                superbox.add_widget(textbox)
                self.ids.comparebox.add_widget(superbox)
                print("added")
                self.ids.comparebox.add_widget(line)




        for best in best_price_box:
            best_price_chip = MDChip(
                text='BEST PRICE',
                pos_hint={'center_x': .20, 'center_y': .90},
                icon='',
                color=[1, 1, 1, 1],
            )
            best.add_widget(best_price_chip)

        for best in best_rating_box:
            best_rating_chip = MDChip(
                text='BEST RATING',
                pos_hint={'center_x': .58, 'center_y': .75},
                icon='',
                color=[1, 1, 1, 1],
            )
            best.add_widget(best_rating_chip)

