from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import Screen
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivymd.app import MDApp

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
            "text": "Manhanttan",
            "on_release": lambda x=f"Manhanttan": self.set_neighborhood(x),
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
            "text": "Shopping",
            "on_release": lambda x=f"Shopping": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "Food",
            "on_release": lambda x=f"Food": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "Sightseeing",
            "on_release": lambda x=f"Sightseeing": self.set_interests(x),
            },{"viewclass": "OneLineListItem",
            "text": "Art & Music",
            "on_release": lambda x=f"Art & Music": self.set_interests(x),
            }, {"viewclass": "OneLineListItem",
            "text": "Nightlife",
            "on_release": lambda x=f"Nightlife": self.set_interests(x),}
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
        filter = {"category.eg": [text__age]}
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
        filter = {"category.in[]": [text__interest]}
        res = [None]
        self.api.getVillageCategory(res,filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
        filter = {"village.in[]":village_list}
        self.api.setFilters(filter)

    def set_superhost(self,status):
        filter = {"superhost.eq":None}
        if status:
            filter['superhost.eq'] = True
        self.api.setFilters(filter)

    def set_fairfilter(self,status):
        filter = {"fairfilter.eq":None}
        if status:
            filter['total_listings_count.le'] = 3
        self.api.setFilters(filter)

    def show_datepicker(self):
        picker = MDDatePicker()
        picker.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        picker.open()



if __name__ =="__main__":

    class SliderApp(MDApp):
        def build(self):
            return Form()


    SliderApp().run()