from kivy_garden.mapview.clustered_marker_layer import ClusterMapMarker
from kivy.uix.button import ButtonBehavior


class CustomCluster(ClusterMapMarker, ButtonBehavior):
    """
    Import cluster image for mapview
    """
    def __init__(self, *args, **kwargs):
        super(CustomCluster, self).__init__(source="atlas://frontend/icons/frontendAtlas/cluster", *args, **kwargs)
