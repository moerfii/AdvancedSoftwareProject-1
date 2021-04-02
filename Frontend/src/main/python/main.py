from kivymd.app import MDApp
from airbnbmapview import AirbnbMapView


class MainApp(MDApp):
    def on_start(self):
        pass
    pass



MainApp().run()

'''
def on_start(self):
    lat1, lon1, lat2, lon2 = self.root.get_bbox()
    data = requests.get(f"http://localhost:8888/listings/location?lat1={lat1}&lat2={lat2}&lon1={lon1}&lon2={lon2}")
    data = json.loads(data.text)
    start = time.time()
    print(len(data))
    for i in range(len(data)):
        print(i)
        marker = MapMarkerPopup(lat=data[i]["latitude"], lon=data[i]["longitude"], source="marker.png")

        self.root.add_marker(marker)

    print(time.time() - start)


'''
