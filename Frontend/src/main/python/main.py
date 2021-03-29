from kivy.app import App
from kivy_garden.mapview import MapMarkerPopup


class MainApp(App):
    def on_start(self):
        marker = MapMarkerPopup(lat=40.754, lon=-73.984)
        self.root.add_widget(marker)
    pass


MainApp().run()
