
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
        best_price_box = {}
        best_rating_box = {}

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
                size_hint = [0.4,1]
                )
                textbox = MDBoxLayout(
                    orientation = 'horizontal'
                )
                supervertbox = MDBoxLayout(
                    orientation = 'vertical',

                )
                supervertbox2 = MDBoxLayout(
                    orientation = 'vertical'
                )
                vertbox1 = MDBoxLayout(
                    orientation = 'vertical'


                )
                vertbox2 = MDBoxLayout(
                    orientation = 'vertical',
                    size_hint_x = 0.15
                )
                horibox1 = MDBoxLayout(
                    orientation = 'horizontal'
                )

                img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
                                    pos_hint={'center_x': .5, 'center_y': .5},
                                 size_hint_y= 1, width = 100)



                roomtype_label = MDLabel(text=
                                f"[color=808080]{data['room_type']} in {data['village']} ({data['borough']})[/color]",
                                markup=True,
                                halign='left',
                                pos_hint={'center_x': .5, 'center_y': .95})

                title_label = MDLabel(text=
                                         f"[size=25]{data['name']}[/size]",
                                         markup=True,
                                         halign='left',
                                         pos_hint={'center_x': .5, 'center_y': .85})

                price_label = MDLabel(text=f"[size=25][b]{data['price']}$[/b]/night[/size]",
                                markup=True,
                                halign='right',
                                pos_hint={'center_x': 0.3, 'center_y': .1})


                line = MDSeparator(height = dp(1))

                # add textbox/price to dicitonary for 'best' label
                if not data['price'] == 0:
                    best_price_box[supervertbox2] = data['price']
                best_rating_box[textbox] = float(data['review_score'])/20



                superhost_chip = MDChip(
                    text='SUPERHOST',
                    pos_hint={'center_x': .20, 'center_y': .90},
                    icon='',
                    color=[1, 1, 1, 1],
                )

                staricon = MDIcon(
                    icon='star',
                    pos_hint={'center_x': .50, 'center_y': .08}
                )
                starlabel = MDLabel(
                    text=f"[b]{float(data['review_score']) / 20}[/b] ({data['number_of_reviews']})", markup=True,
                    pos_hint={'center_x': .54, 'center_y': .07}
                )

                webbutton = MDIconButton(
                    icon='search-web',
                    on_press=lambda x: open_link(data['listing_url']),
                    user_font_size="36sp",
                    pos_hint={'center_x': 0.9, 'center_y': .1}
                )

                bookmarkbutton = ListingSaveButton(
                    data,
                    pos_hint={'center_x': .9, 'center_y': .9},
                    opposite_colors= False,
                    icon = 'delete'
                )
                imagebox.add_widget(img)
                if data['is_superhost']:
                    imagebox.add_widget(superhost_chip)

                vertbox1.add_widget(roomtype_label)
                vertbox1.add_widget(title_label)

                horibox1.add_widget(staricon)
                horibox1.add_widget(price_label)

                vertbox2.add_widget(bookmarkbutton)
                vertbox2.add_widget(webbutton)


                supervertbox.add_widget(vertbox1)
                supervertbox.add_widget(horibox1)
                textbox.add_widget(supervertbox)
                textbox.add_widget(vertbox2)
                superbox.add_widget(imagebox)
                superbox.add_widget(textbox)
                self.ids.comparebox.add_widget(superbox)
                print("added")
                self.ids.comparebox.add_widget(line)

        best_price_chip = MDChip(
            text='BEST PRICE',
            pos_hint={'center_x': .20, 'center_y': .90},
            icon='',
            color=[1, 0.8, 0.06, 1],
        )
        min(best_price_box, key=best_price_box.get).add_widget(best_price_chip)

        best_rating_chip = MDChip(
            text='BEST RATING',
            pos_hint={'center_x': .50, 'center_y': .90},
            icon='',
            color=[1, 0.8, 0.06, 1],
        )
        # needs 10 ratings
        max(best_rating_box, key=best_rating_box.get).add_widget(best_rating_chip)

