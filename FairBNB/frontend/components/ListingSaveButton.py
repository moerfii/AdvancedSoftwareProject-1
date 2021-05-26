import time

from kivy.metrics import dp
from kivy.uix.button import Button
import os
import json

from kivymd.uix.button import MDIconButton
from kivy.app import App

class ListingSaveButton(MDIconButton):
    """
    This is a button that saves the listing information or removes it
    """
    size_hint = None, None
    background_color = [0, 0, 1, 1]


    def __init__(self,data,pos_hint = None,opposite_colors = None,icon = None,**kwargs):
        super(MDIconButton,self).__init__(**kwargs)
        self.data=data
        if pos_hint is None:
            self.pos_hint = {'center_x': .90, 'center_y': .83}
        else:
            self.pos_hint = pos_hint
        if not os.path.isdir("bookmarks"):
            os.mkdir("bookmarks")
        path = 'bookmarks'
        full_path = os.path.join(os.getcwd(), path)
        if not os.listdir(full_path):
            if icon is None:
                self.icon = 'heart-outline'
            else:
                self.icon = icon
        else:
            for filenames in os.walk(full_path):
                for filename in filenames[2]:
                    currentfile = open(os.path.join(full_path, filename), "r")
                    json_data = json.load(currentfile)
                    if self.data["id"] == json_data['id']:
                        if icon is None:
                            self.icon = 'heart'
                        else:
                            self.icon = icon
                        break
                    else:
                        if icon is None:
                            self.icon = 'heart-outline'
                        else:
                            self.icon = icon
        self.user_font_size = "36sp"
        if opposite_colors is None:
            self.opposite_colors = True
        else:
            self.opposite_colors = opposite_colors
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
        print(type(self.icon))
        if not self.isBookmarked:
            self.bookmark()
        else:
            app = App.get_running_app()
            self.removeBookmark(self.parent.parent.parent)


    def bookmark(self):
        print("bookmark")
        if not os.path.isdir("bookmarks"):
            os.mkdir("bookmarks")
        with open(f"bookmarks/{self.data['id']}.json","w+") as f:
            f.write(json.dumps(self.data))
        self.isBookmarked=True
        self.icon = 'heart'


    def removeBookmark(self, child):
        if self.icon == 'delete':
            print("updateing screenn")
            print(self.parent.parent.parent)
            self.parent.parent.parent.parent.remove_widget(child)
        print("remove bookmark")
        os.remove(f"bookmarks/{self.data['id']}.json")
        self.isBookmarked=False
        self.icon = 'heart-outline'
