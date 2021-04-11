from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from airbnbmapview import AirbnbMapView
from searchpopupmenu import SearchPopupMenu
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MapScreen(Screen):

    pass

class FormScreen(Screen):
    pass

class CompareScreen(Screen):
    pass

class MainApp(MDApp):

    search_menu = None

    def on_start(self):
        # init searchpopup
        self.search_menu = SearchPopupMenu()

    def build(self):

        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Compare",
                "on_release": lambda x=1: self.menu_callback(x),

            },
            {
                "viewclass": "OneLineListItem",
                "text": f"Questionaire",
                "on_release": lambda x=2: self.menu_callback(x),

            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        self.sm = ScreenManager(transition=WipeTransition())
        self.sm.add_widget(MapScreen(name='mapscreen'))
        self.sm.add_widget(FormScreen(name='formscreen'))
        self.sm.add_widget((CompareScreen(name='comparescreen')))
        return self.sm

    def callback(self, button):
        self.menu.caller = button
        self.menu.open()


    def menu_callback(self, screen_nr):
        print(self.sm.current)

        self.menu.dismiss()
        self.sm.switch_to(self.sm.screens[screen_nr])
        print(self.sm.current)
        return

        #Snackbar(text=text_item).open()
    pass



MainApp().run()


