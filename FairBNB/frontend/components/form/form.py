import time
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivymd.app import MDApp
from kivy.clock import Clock

from kivy.lang import Builder


class Form(MDCard):
    def __init__(self,**kwargs):
        super(Form,self).__init__(**kwargs)
        #self.screen = Builder.load_string(KV)


    def on_start(self):
        print("ON START")
        
        neighborhoods = [
            {"viewclass": "OneLineListItem",
            "text": "Bronx",
            "on_release": lambda x=f"Bronx": self.set_neighborhood(x),
            },{"viewclass": "OneLineListItem",
            "text": "Brooklyn",
            "on_release": lambda x=f"Brooklyn": self.set_neighborhood(x),
            },{"viewclass": "OneLineListItem",
            "text": "Manhattan",
            "on_release": lambda x=f"Manhattan": self.set_neighborhood(x),
            },{"viewclass": "OneLineListItem",
            "text": "Queens",
            "on_release": lambda x=f"Queens": self.set_neighborhood(x),
            }, {"viewclass": "OneLineListItem",
            "text": "Staten Island",
            "on_release": lambda x=f"Staten Island": self.set_neighborhood(x),}
        ]

        ages = [
            {"viewclass": "OneLineListItem",
            "text": "18 - 30",
            "on_release": lambda x=f"18-30": self.set_age(x),
            },{"viewclass": "OneLineListItem",
            "text": "31 - 50",
            "on_release": lambda x=f"31-50": self.set_age(x),
            },{"viewclass": "OneLineListItem",
            "text": "50+",
            "on_release": lambda x=f"51-120": self.set_age(x),
            }
        ]

        interests = [
            {"viewclass": "OneLineListItem",
            "text": "5 stars",
            "on_release": lambda x=f"5stars": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "4 stars",
            "on_release": lambda x=f"4starts": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "3 stars",
            "on_release": lambda x=f"3stars": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "2 stars",
            "on_release": lambda x=f"2stars": self.set_interests(x),
            }, {"viewclass": "OneLineListItem",
            "text": "1 star",
            "on_release": lambda x=f"1star": self.set_interests(x),}
        ]

        self.menu_n = MDDropdownMenu(
            caller=self.ids.field_n,
            items=neighborhoods,
            position="bottom",
            width_mult=3,)
        self.menu_a = MDDropdownMenu(
            caller=self.ids.field_a,
            items=ages,
            position="bottom",
            width_mult=2,)
        self.menu_i = MDDropdownMenu(
            caller=self.ids.field_i,
            items=interests,
            position="bottom",
            width_mult=2,)
        
        app = App.get_running_app()
        self.api=app.api

    def set_neighborhood(self, text__neighbor):

        self.ids.field_n.text = text__neighbor
        self.menu_n.dismiss()
        filter = {"borough.eq":"'"+text__neighbor+"'"}
        self.api.setFilters(filter)


    def set_age(self, text__age):
        self.ids.field_a.text = text__age
        self.menu_a.dismiss()
        filter = {"age.eq": f"'{text__age}'"}
        res = [None]
        self.api.getVillageCategory(res,filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
            
        filter = {"village.in[]":village_list}
        self.api.setFilters(filter)

    def set_interests(self, text__interest):
        self.ids.field_i.text = text__interest
        self.menu_i.dismiss()
        filter = {"interest.in[]": [text__interest]}
        res = [None]
        self.api.getVillageCategory(res,filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
        filter = {"village.in[]":village_list}
        self.api.setFilters(filter)

    def set_superhost(self,status):
        filter = {"is_superhost.eq":None}
        if status:
            filter['is_superhost.eq'] = True
        self.api.setFilters(filter)

    def set_fairfilter(self,status):
        filter = {"total_listings_count.le":None}
        if status:
            filter['total_listings_count.le'] = 3
        self.api.setFilters(filter)

    def show_datepicker(self):
        picker = MDDatePicker()
        picker.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        picker.open()

    def switch_to_mapscreen(self):
        print("search")
        app=App.get_running_app()
        mapview = app.root.ids['mapview']
        #mapview.firstCall=True
        screenmanager = app.root.ids['screen_manager']
        screenmanager.current="mapscreen"
        #mapview.get_airbnb_in_fov()
        #mapview._need_redraw_all = True
        #Clock.schedule_once(mapview.fakeClick,0.5)
        #Clock.schedule_once(mapview.get_airbnb_in_fov,0.1)
        #Clock.schedule_once(lambda dt: mapview.canvas.ask_update(), 0.5)


        



if __name__ =="__main__":

    class SliderApp(MDApp):
        def build(self):
            return Form()


    SliderApp().run()