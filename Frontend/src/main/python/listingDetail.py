from kivy.uix.popup import Popup
from kivy.uix.label import Label
import requests
import json

def listingDetail(listing_id):
    response = requests.get(f"http://localhost:8888/listing/{listing_id}")
    data = json.loads(response.text)[0]
    print(data)
    popup = Popup(
        title=data['name'],
        content=Label(text = f"""
            Price: {data['price']}$/night
            RoomType: {data['room_type']}
            """
        ),
        size_hint=(None,None),
        size=(400,400),
        auto_dismiss=False)
    
    return popup
    
