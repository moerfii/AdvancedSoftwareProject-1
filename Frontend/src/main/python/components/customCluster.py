from kivy_garden.mapview.clustered_marker_layer import ClusterMapMarker
#from mapViewOverride.clustered_marker_layer import ClusterMapMarker
from kivy.garden.mapview import MapMarkerPopup
from kivy.app import App
from kivy.uix.button import ButtonBehavior

#Not very elegant
CLUSTER_CLICKED = False
import inspect
class CustomCluster(ClusterMapMarker,ButtonBehavior):
    def __init__(self,*args, **kwargs):
        super(CustomCluster,self).__init__(source="icons/cluster.png",*args, **kwargs)


if __name__== "__main__":
    import sys
    sys.setrecursionlimit(10000)
    
    print(inspect.getmro(CustomCluster()))

