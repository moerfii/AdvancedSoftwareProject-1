from kivy_garden.mapview import MapMarkerPopup
from kivy.properties import NumericProperty
from listingDetail import listingDetail

class AirbnbMarker(MapMarkerPopup):
<<<<<<< HEAD:Frontend/src/main/python/components/airbnbMarker.py
=======

    #id_listing=NumericProperty(0)
>>>>>>> c11c8117beea6e6d85bf4ee2f89ad0f27508349c:Frontend/src/main/python/airbnbmarker.py
    def __init__(self, id_listing, lon, lat, source):
        super(MapMarkerPopup, self).__init__(lon=lon, lat=lat, source=source)
        self.id_listing = id_listing


    def on_release(self):
        popup=listingDetail(self.id_listing)
        popup.open()

