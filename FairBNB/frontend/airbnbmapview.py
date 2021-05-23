from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from kivy_garden.mapview import MapMarkerPopup
import time
import requests
import json
import time
from .components.map.airbnbMarker import AirbnbMarker
from .components.map.customCluster import CustomCluster
from .mapViewOverride.clustered_marker_layer import ClusteredMarkerLayer


class AirbnbMapView(MapView):
    getting_airbnb_timer = None
    listing_id_list = []

    def start_getting_airbnb_in_fov(self):
        # After one second, get listings in field of view
        try:
            self.getting_airbnb_timer.cancel()
        except:
            pass

        self.getting_airbnb_timer = Clock.schedule_once(self.get_airbnb_in_fov, 1)

    def get_airbnb_in_fov(self, *args):
        app = App.get_running_app()
        lat1, lon1, lat2, lon2 = self.get_bbox()
        custom_filter = {'latitude.ge':lat1,'latitude.le':lat2,'longitude.ge':lon1,'longitude.le':lon2}
        
        listings = [None]
        app.api.getListingLocations(listings,custom_filter)

        layer = ClusteredMarkerLayer(cluster_cls=CustomCluster,cluster_radius="200dp",cluster_max_zoom=18)
        cnt = 0
        # add listing to layer, break after 10'000 listings
        for listing in listings[0]:
            if cnt >=10000:
                break
            listing_id = listing['id']
            if listing_id in self.listing_id_list:
                continue
            else:
                layer.add_marker(
                    lon=float(listing['longitude']),
                    lat=float(listing['latitude']),
                    cls=AirbnbMarker,
                    options={
                        "source": "atlas://frontend/icons/frontendAtlas/marker",
                        "id_listing": listing['id']
                    }
                )
            cnt+= 1
        #remove old layers
        for child in self.children:
            if(isinstance(child, ClusteredMarkerLayer)):
                self.remove_widget(child)

        self.add_widget(layer)


    