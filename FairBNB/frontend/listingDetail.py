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
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

from .components.ListingSaveButton import ListingSaveButton
import webbrowser


def open_link(url):
    webbrowser.open(url)


def listingDetail(listing_id):
    #get Data
    custom_filters = {'id.eq':str(listing_id)}
    app = App.get_running_app()
    detail_data = [None]
    other_data = [None]
    app.api.getListingDetail(detail_data,custom_filters)
    app.api.getListingOther(other_data,custom_filters)

    #merge data
    data = {**detail_data[0][0], **other_data[0][0]}
    superbox = MDBoxLayout(
        orientation='vertical'
    )
    imagebox = MDFloatLayout(
        )
    textbox = MDFloatLayout(
    )
    img = AsyncImage(source=data['picture_url'], allow_stretch=True, keep_ratio=False, pos_hint = {'center_x': .5, 'center_y': .5})
    label = MDLabel(text = f"Price: {data['price']}$/night"
                         f"\nRoomType: {data['room_type']}"
                        f"\nListing URL: [ref=www.airbnb.com][color=0000ff]{data['listing_url']}[/color][/ref]", markup=True,
                    halign='center',
                    # TODO: make url button
                    #on_ref_press= print("test"), #open_link(data['listing_url']),
                    width= 250,
                    size_hint=(None, None),
                    pos_hint = {'center_x': .5, 'center_y': .5})
    print(ListingSaveButton)
    button = ListingSaveButton(data)

    print(data['picture_url'])
    imagebox.add_widget(img)
    textbox.add_widget(label)
    imagebox.add_widget(button)

    superbox.add_widget(imagebox)
    superbox.add_widget(textbox)
    
    popup = Popup(
        title=data['name'],
        title_color= [0, 0, 0, 1],
        content=superbox,
        background = 'background.jpg',
        size_hint=(None,None),
        size=(400,400),
        auto_dismiss=True,
        separator_color = [.9, .4, .2, 1]
        )
    
    return popup
    
