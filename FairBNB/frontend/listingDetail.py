from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import requests
import json
from kivy.app import App
import time

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.chip import MDChip
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.utils.fitimage import FitImage

from .components.ListingSaveButton import ListingSaveButton
import webbrowser


from kivy.config import Config
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.floatlayout import FloatLayout

Config.set("graphics", "width", "500")
Config.set("graphics", "height", "300")


class RoundedCornerLayout(MDBoxLayout):

    orientation = 'vertical'

    def __init__(self):
        super().__init__()

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[(40, 40), (40, 40), (20, 20), (20, 20)],
            )
        self.bind(pos=lambda obj, pos: setattr(self.rect, "pos", pos))
        self.bind(size=lambda obj, size: setattr(self.rect, "size", size))

        self.size_hint = (None, None)
        self.size = (275, 350)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.background_color = 0, 0, 0, 1


def open_link(url):
    webbrowser.open(url)





def listingDetail(listing_id):
    #get Data
    custom_filters = {'id.eq':str(listing_id)}
    app = App.get_running_app()
    detail_data = [None]
    other_data = [None]
    location_data = [None]
    app.api.getListingDetail(detail_data,custom_filters)
    app.api.getListingOther(other_data,custom_filters)
    app.api.getListingLocations(location_data, custom_filters)

    #merge data
    data = {**detail_data[0][0], **other_data[0][0], **location_data[0][0]}
    superbox = RoundedCornerLayout(
    )
    imagebox = MDFloatLayout(
        )
    textbox = MDFloatLayout(
    )
    img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
                     pos_hint = {'center_x': .5, 'center_y': .5})
    #fittedimg = FitImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False,
    #                 pos_hint = {'center_x': .5, 'center_y': .5})
    superhost_chip = MDChip(
        text='SUPERHOST',
        pos_hint={'center_x': .24, 'center_y': .83},
        icon= '',
        color = [1,1,1,1],

    )
    staricon = MDIcon(
        icon = 'star',
        pos_hint = {'center_x': .53, 'center_y': .76}
    )
    starlabel = MDLabel(
        text= f"[b]{float(data['review_score'])/20}[/b] ({data['number_of_reviews']})", markup=True,
        pos_hint={'center_x': .63, 'center_y': .75}
    )

    label = MDLabel(text =
                         f"{data['room_type']}"
                         f"\n[b]{data['price']}$[/b]/night",
                    markup=True,
                    halign='left',
                    # TODO: make url button
                    #on_ref_press= print("test"), #open_link(data['listing_url']),
                    width= 250,
                    size_hint=(None, None),
                    pos_hint = {'center_x': .5, 'center_y': .5})



    bookmarkbutton = ListingSaveButton(data)
    webbutton = MDIconButton(
        icon = 'search-web',
        on_press= lambda x: open_link(data['listing_url']),
        user_font_size="36sp",
        pos_hint={'center_x': .90, 'center_y': .15}
    )

    imagebox.add_widget(img)
    textbox.add_widget(label)
    imagebox.add_widget(bookmarkbutton)
    textbox.add_widget(webbutton)
    textbox.add_widget(staricon)
    textbox.add_widget(starlabel)
    if data['is_superhost']:
        imagebox.add_widget(superhost_chip)
    superbox.add_widget(imagebox)
    superbox.add_widget(textbox)

    popup = Popup(
        content=superbox,
        background = 'background.jpg',
        size_hint=(None,None),
        size=(300,350),
        pos_hint={'left':0.9},
        auto_dismiss=True,
        separator_color = [.9, .4, .2, 1],
        background_color = [0, 0, 0, 0]
        )
    
    return popup
    
