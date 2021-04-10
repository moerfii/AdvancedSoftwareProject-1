from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import NumericProperty
from locationpopupmenu import LocationPopupMenu
from listingDetail import listingDetail

class AirbnbMarker(MapMarkerPopup):
    #id_listing=NumericProperty(0)
    def __init__(self, id_listing, lon, lat, source):
        super(MapMarkerPopup, self).__init__(lon=lon, lat=lat, source=source)
        self.id_listing = id_listing


    def on_release(self):
        popup=listingDetail(self.id_listing)
        popup.open()
        #menu = LocationPopupMenu(**self.listing_data)
        #menu.open()
