
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
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.boxlayout import MDBoxLayout
from frontend.listingDetail import RoundedCornerLayout

from frontend.components.ListingSaveButton import ListingSaveButton


def open_link(url):
    webbrowser.open(url)


class ContentReviews(MDBoxLayout):
    pass


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
                superhoribox = MDBoxLayout(
                    orientation = 'horizontal'
                )

                vertbox_title_roomtype = MDBoxLayout(
                    orientation = 'vertical',
                    size_hint_y = 0.7
                )
                vertbox_roomtype = MDBoxLayout(
                    size_hint_y = 0.3
                )
                vertbox_title = MDBoxLayout(
                    size_hint_y=0.7
                )
                vertbox_buttons = MDFloatLayout(
                    size_hint_x = 0.1
                )
                vertbox_guests_included = MDBoxLayout(
                    orientation = 'horizontal'

                )
                horibox_rating = MDBoxLayout(
                    orientation = 'horizontal'
                )
                horibox_star = MDBoxLayout(
                    orientation = 'horizontal',
                    size_hint_x = 0.3
                )



                img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
                                    pos_hint={'center_x': .5, 'center_y': .5},
                                 size_hint_y= 1, width = 100)



                roomtype_label = MDLabel(text=
                                f"[color=808080]{data['room_type']} in {data['village']} ({data['borough']})[/color]",
                                markup=True,
                                halign='left',
                                pos_hint={'center_x': .5, 'center_y': .75})

                title_label = MDLabel(text=
                                         f"[size=25]{data['name']}[/size]",
                                         markup=True,
                                         halign='left',
                                         pos_hint={'center_x': .5, 'center_y': .85})


                reviews_expansion = MDExpansionPanel(
                                        icon="",  # panel icon
                                        content=ContentReviews(),  # panel content
                                        panel_cls=MDExpansionPanelOneLine(text="Reviews"),  # panel class
    )


                if data['guests_included'] == 1:
                    guest_text = f"{data['guests_included']} guest"
                else:
                    guest_text = f"{data['guests_included']} guests"

                guests_inclueded_label = MDLabel(
                    text= guest_text,
                    halign='left',
                    pos_hint={'center_x': .5, 'center_y': .35}
                )

                price_label = MDLabel(text=f"[size=25][b]{data['price']}$[/b]/night[/size]",
                                markup=True,
                                halign='right',
                                pos_hint={'center_x': 0.3, 'center_y': .1})


                line = MDSeparator(height = dp(1))

                # add textbox/price to dicitonary for 'best' label
                if not data['price'] == 0:
                    best_price_box[imagebox] = data['price']
                if data['number_of_reviews'] >=10:
                    best_rating_box[imagebox] = float(data['review_score'])/20



                superhost_chip = MDChip(
                    text='SUPERHOST',
                    pos_hint={'center_x': .20, 'center_y': .90},
                    icon='',
                    color=[1, 1, 1, 1],
                )

                staricon = MDIcon(
                    icon='star',
                    pos_hint={'left_x': .50, 'center_y': .08}
                )
                starlabel = MDLabel(
                    text=f"[b]{float(data['review_score']) / 20}[/b] ({data['number_of_reviews']})", markup=True,
                    pos_hint={'left_x': .50, 'center_y': .07}
                )

                webbutton = MDIconButton(
                    icon='search-web',
                    on_press=lambda x: open_link(data['listing_url']),
                    user_font_size="36sp",
                    pos_hint={'center_x': .9, 'center_y': .4}
                )

                bookmarkbutton = ListingSaveButton(
                    data,
                    pos_hint={'center_x': .9, 'center_y': .6},
                    opposite_colors= False,
                    icon = 'delete'
                )


                ##### ADD WIDGETS

                imagebox.add_widget(img)
                if data['is_superhost']:
                    imagebox.add_widget(superhost_chip)

                vertbox_title.add_widget(title_label)
                vertbox_roomtype.add_widget(roomtype_label)
                vertbox_title_roomtype.add_widget(vertbox_roomtype)
                vertbox_title_roomtype.add_widget(vertbox_title)


                vertbox_buttons.add_widget(bookmarkbutton)
                vertbox_buttons.add_widget(webbutton)


                horibox_star.add_widget(staricon)
                horibox_star.add_widget(starlabel)
                horibox_rating.add_widget(horibox_star)
                horibox_rating.add_widget(price_label)
                superhoribox.add_widget(horibox_rating)

                vertbox_guests_included.add_widget(guests_inclueded_label)
                vertbox_guests_included.add_widget(reviews_expansion)

                supervertbox.add_widget(vertbox_title_roomtype)
                supervertbox.add_widget(vertbox_guests_included)
                supervertbox.add_widget(superhoribox)

                textbox.add_widget(supervertbox)
                textbox.add_widget(vertbox_buttons)


                superbox.add_widget(imagebox)
                superbox.add_widget(textbox)
                self.ids.comparebox.add_widget(superbox)
                print("added")
                self.ids.comparebox.add_widget(line)

        best_price_chip = MDChip(
            text='BEST PRICE',
            pos_hint={'center_x': .8, 'center_y': .9},
            icon='',
            color=[0.2, 0.65, 0.92, 1],
            spacing = dp(4)
        )
        min(best_price_box, key=best_price_box.get).add_widget(best_price_chip)

        if min(best_price_box, key=best_price_box.get) == max(best_rating_box, key=best_rating_box.get):
            pos = {'center_x': .8, 'center_y': 0.77}
        else:
            pos = {'center_x': .8, 'center_y': .9}
        best_rating_chip = MDChip(
            text='BEST RATING',
            pos_hint=pos,
            icon='',
            color=[0.2, 0.65, 0.92, 1],
            spacing = dp(4)
        )
        # needs 10 ratings
        if len(best_rating_box) is not 0:
            max(best_rating_box, key=best_rating_box.get).add_widget(best_rating_chip)

