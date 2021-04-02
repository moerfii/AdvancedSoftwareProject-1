from Frontend.src.main.python.kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineAvatarListItem

KV = '''
MDFloatLayout:

    MDFlatButton:
        text: "ALERT DIALOG"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()
'''


class LocationPopupMenu(MDDialog):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)



