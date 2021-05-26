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
from kivy.input.providers.mouse import MouseMotionEvent


class AirbnbMapView(MapView):
    listing_id_list = []
    firstCall=True

    def __init__(self, *args, **kwargs):
        super(AirbnbMapView,self).__init__(*args,**kwargs)

    def get_airbnb_in_fov(self, *args):
        if(len(args)>0 and args[0]=="on_enter"):
            print("enter")
            self.firstCall=True
        lat1, lon1, lat2, lon2 = self.get_bbox()
        if(self.firstCall):
            lat1+=(lat1-lat2)*2
            lat2-=(lat1-lat2)*2
            lon1+=(lon1-lon2)*2
            lon2-=(lon1-lon2)*2
            self.firstCall=False

    
        app = App.get_running_app()
        print(lat1, lat2, lon1, lon2)
        print(lat1-lat2,lon1-lon2)
        custom_filter = {'latitude.ge':lat1,'latitude.le':lat2,'longitude.ge':lon1,'longitude.le':lon2}
        
        #seems to be more efficient to exploit the pointer ability of list elements
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
    