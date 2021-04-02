from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu


class AirbnbMarker(MapMarkerPopup):
    listing_data = []

    def on_release(self):
        menu = LocationPopupMenu(**self.listing_data)
        menu.open()
