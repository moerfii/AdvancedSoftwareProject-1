from kivy_garden.mapview import MapMarkerPopup
from ...listingDetail import listing_detail
from kivy.app import App

class AirbnbMarker(MapMarkerPopup):
    """
    Definition of image source + call of function listing_detail when marker is clicked.
    """
    def __init__(self, id_listing, lon, lat, source):
        super(MapMarkerPopup, self).__init__(lon=lon, lat=lat, source=source)
        self.lon=lon
        
        self.id_listing = id_listing

    def on_release(self):
        app = App.get_running_app()
        app.root.ids.mapview.selected_id=self.id_listing
        self.source= "frontend/icons/marker2.png"
        popup = listing_detail(self.id_listing,self)
        popup.open()

    def reset_marker(self,*args):
        self.source = "atlas://frontend/icons/frontendAtlas/marker"
        app=App.get_running_app()
        app.root.ids.mapview.selected_id=None
