#from kivy_garden.mapview.clustered_marker_layer import ClusterMapMarker
from mapViewOverride.clustered_marker_layer import ClusterMapMarker
from kivy.app import App
from kivy.uix.button import ButtonBehavior
from globals import CLUSTER_CLICKED

#Not very elegant
CLUSTER_CLICKED = False

class CustomCluster(ClusterMapMarker):
    def __init__(self,*args, **kwargs):
        #super(ButtonBehavior,self).__init__(**kwargs)
        super(CustomCluster,self).__init__(source="icons/cluster.png",*args, **kwargs)
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        self.zoom=mapview.zoom
        self.clicked=False
    """
    def on_touch_down(self,x): 
        print("CustomCluster: on_touch_down")
        print(f"self.clicked: {self.clicked}")
        if not self.clicked:
            app = App.get_running_app()
            mapview = app.root.ids.mapview
            print(mapview.zoom)
            lat,lon = mapview.get_latlon_at(self.cluster.y,self.cluster.x)
            print(lon)
            print(lat)
            mapview.zoom = self.zoom
            print(self.cluster.x)
            print(self.cluster.y)
            #mapview.center_on(self.cluster.x,self.cluster.y)
            print(mapview.zoom)
            self.clicked=True
    """
    def on_touch_up(self,touch):
        global CLUSTER_CLICKED
        
        if not CLUSTER_CLICKED:
            print("CustomCluster: on_touch_up")

            #CLUSTER_CLICKED=True
            app = App.get_running_app()
            mapview = app.root.ids.mapview
            print(f"zoom: {mapview.zoom}")
            lat,lon = mapview.get_latlon_at(self.cluster.y,self.cluster.x)
            print(f"lon1: {lon}")
            print(f"lat1: {lat}")
            print(f"lonCluster: {self.cluster.lon}")
            print(f"latCluster: {self.cluster.lat}")
            print(f"selfLon: {self.lon}")
            print(f"selfLat: {self.lat}")


            mapview.center_on(self.cluster.lat,self.cluster.lon)
            
            print(f"newzoom: {mapview.zoom}")

 
