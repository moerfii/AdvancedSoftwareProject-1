from kivymd.app import MDApp
from airbnbmapview import AirbnbMapView
from searchpopupmenu import SearchPopupMenu

class MainApp(MDApp):

    main_menu = None
    search_menu = None

    def on_start(self):
        # init searchpopup
        self.search_menu = SearchPopupMenu()
    pass


MainApp().run()


