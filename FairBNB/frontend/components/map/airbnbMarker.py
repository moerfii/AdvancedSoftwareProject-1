from kivy_garden.mapview import MapMarkerPopup
from ...listingDetail import listing_detail


class AirbnbMarker(MapMarkerPopup):
    """
    Definition of image source + call of function listing_detail when marker is clicked.
    """
    def __init__(self, id_listing, lon, lat, source):
        super(MapMarkerPopup, self).__init__(lon=lon, lat=lat, source=source)
        self.id_listing = id_listing

    def on_release(self):
        popup = listing_detail(self.id_listing)
        popup.open()
