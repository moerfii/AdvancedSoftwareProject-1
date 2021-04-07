from kivy_garden.mapview import MapMarker
from locationpopupmenu import LocationPopupMenu


class AirbnbMarker(MapMarker):
    listing_data = []
    source = 'marker.png'

    def on_release(self):
        menu = LocationPopupMenu(**self.listing_data)
        menu.open()
