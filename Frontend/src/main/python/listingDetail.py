from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from components.ListingSaveButton import ListingSaveButton
import os
import requests
import json



def listingDetail(listing_id):
    #get Data
    detail_response = requests.get(f"http://localhost:8888/listing_detail/{listing_id}")
    detail_data = json.loads(detail_response.text)[0]
    other_response = requests.get(f"http://localhost:8888/listing_other/{listing_id}")
    other_data = json.loads(other_response.text)[0]

    #merge data
    data = {**detail_data, **other_data}
    box = BoxLayout()
    img = AsyncImage(source=data['picture_url'])
    label = Label(text = f"Price: {data['price']}$/night\nRoomType: {data['room_type']}")
    print(ListingSaveButton)
    button = ListingSaveButton(data,text="Bookmark listing")

    print(data['picture_url'])
    box.add_widget(img)
    box.add_widget(label)
    box.add_widget(button)
    
    
    popup = Popup(
        title=data['name'],
        content=box,
        size_hint=(None,None),
        size=(600,600),
        auto_dismiss=True)
    
    return popup
    
