from kivy_garden.mapview.clustered_marker_layer import ClusterMapMarker

class CustomCluster(ClusterMapMarker):
    def __init__(self,*args, **kwargs):
        super(CustomCluster,self).__init__(source="icons/cluster.png",*args, **kwargs)

    def on_touch_down(self,x):
        print(x)
