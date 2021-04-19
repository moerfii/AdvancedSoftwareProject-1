from kivy.uix.button import Button
import os
import json

class ListingSaveButton(Button):
    """
    This is a button that saves the listing information or removes it
    """
    def __init__(self,data,**kwargs):
        super(Button,self).__init__(**kwargs)
        self.data=data
        if os.path.isfile(f"bookmarks/{data['id']}.json"):
            print("folder found")
            self.isBookmarked=True
            self.text = "Remove Bookmark"
        else:
            self.isBookmarked=False
            self.text = "Bookmark"
    
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
        self.text = "Remove Bookmark"

    def removeBookmark(self):
        print("remove bookmark")
        os.remove(f"bookmarks/{self.data['id']}.json")
        self.isBookmarked=False
        self.text = "Bookmark"

