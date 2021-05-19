from kivy_garden.mapview.clustered_marker_layer import ClusterMapMarker
from kivy.garden.mapview import MapMarkerPopup
from kivy.app import App
from kivy.uix.button import ButtonBehavior
import inspect
class CustomCluster(ClusterMapMarker,ButtonBehavior):
    def __init__(self,*args, **kwargs):
        super(CustomCluster,self).__init__(source="atlas://frontend/icons/frontendAtlas/cluster",*args, **kwargs)
        
