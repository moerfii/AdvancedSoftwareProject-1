from kivy.metrics import dp
from kivy.uix.button import Button
import os
import json

from kivymd.uix.button import MDIconButton


class ListingSaveButton(MDIconButton):
    """
    This is a button that saves the listing information or removes it
    """
    size_hint = None, None
    background_color = [0, 0, 1, 1]


    def __init__(self,data,**kwargs):
        super(MDIconButton,self).__init__(**kwargs)
        self.data=data
        self.pos_hint = {'center_x': .95, 'center_y': .90}
        self.icon = 'heart-outline'
        self.opposite_colors = True
        if os.path.isfile(f"bookmarks/{data['id']}.json"):
            print("folder found")
            self.isBookmarked=True
            self.halign = 'center'
            self.valign = 'center'

        else:
            self.isBookmarked=False
            self.halign = 'center'
            self.valign = 'center'

    
    def on_press(self):
        if not self.isBookmarked:
            self.bookmark()
        else:
            self.removeBookmark()

    def bookmark(self):
        print("bookmark")
        if not os.path.isdir("bookmarks"):
            os.mkdir("bookmarks")
        with open(f"bookmarks/{self.data['id']}.json","w+") as f:
            f.write(json.dumps(self.data))
        self.isBookmarked=True
        self.icon = 'heart'


    def removeBookmark(self):
        print("remove bookmark")
        os.remove(f"bookmarks/{self.data['id']}.json")
        self.isBookmarked=False
        self.icon = 'heart-outline'
