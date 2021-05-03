from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from mapViewOverride.clustered_marker_layer import ClusteredMarkerLayer
from kivy_garden.mapview import MapMarkerPopup
import time
import requests
import json
from components.airbnbMarker import AirbnbMarker
from components.customCluster import CustomCluster
from restAPIConnection import RestAPIConnection
import time
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
        print("get_airbnb")
        start=time.time()
        app = App.get_running_app()
        lat1, lon1, lat2, lon2 = self.get_bbox()
        custom_filter = {'latitude.ge':lat1,'latitude.le':lat2,'longitude.ge':lon1,'longitude.le':lon2}
        
        listings = [None]
        app.api.getListingLocations(listings,custom_filter)
        print(time.time()-start)
        print("size")
        print(len(listings[0]))
        """
        start = time.time()
        data = requests.get(f"http://localhost:8888/listing_location?latitude.ge={lat1}&latitude.le={lat2}&longitude.ge={lon1}&longitude.le={lon2}")
        listings = json.loads(data.text)
        listings = RestAPIConnection().getListingLocations(custom_filter)
        print(time.time()-start)
        1/0
        """
        layer = ClusteredMarkerLayer(cluster_cls=CustomCluster,cluster_radius="200dp",cluster_max_zoom=18)
        #layer = ClusteredMarkerLayer(cluster_radius="200dp",cluster_cls_source="icons/cluster.png")
        for listing in listings[0]:
            id = listing['id']
            if id in self.listing_id_list:
                continue
            else:
                # self.add_listing(listing)
                layer.add_marker(
                    # id_listing=listing['id'],
                    lon=float(listing['longitude']),
                    lat=float(listing['latitude']),
                    cls=AirbnbMarker,
                    options={
                        "source": "icons/marker.png",
                        "id_listing": listing['id']
                    }

                )

        self.add_widget(layer)

        def add_listing(self, listing):
            # create marker
            lat = listing['latitude']
            lon = listing['longitude']
            marker = AirbnbMarker(id_listing=listing['id'], lat=lat, lon=lon, source='marker.png')
            marker.listing_data = listing

            # add marker to map
            self.add_widget(marker)

            # keep track of markers id (avoid adding marker twice and keep it onscreen)
            id = listing['id']
            self.listing_id_list.append(id)
    

    