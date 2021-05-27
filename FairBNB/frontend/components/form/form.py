from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.card import MDCard
from kivymd.uix.picker import MDDatePicker
from kivy.app import App
from kivymd.app import MDApp


class Form(MDCard):
    """
    Questionnaire Screen: here all the widgets seen on the questionnaire are initialised. Once an option is modified, it
    directly sets the filter for the REST-API get request. The search button is simply to switch the screen to the map.
    """
    def __init__(self, **kwargs):
        super(Form, self).__init__(**kwargs)

    def on_start(self):
        
        neighborhoods = [
            {"viewclass": "OneLineListItem",
             "text": "---",
             "on_release": lambda x=f"---": self.set_neighborhood(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "Bronx",
             "on_release": lambda x=f"Bronx": self.set_neighborhood(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "Brooklyn",
             "on_release": lambda x=f"Brooklyn": self.set_neighborhood(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "Manhattan",
             "on_release": lambda x=f"Manhattan": self.set_neighborhood(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "Queens",
             "on_release": lambda x=f"Queens": self.set_neighborhood(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "Staten Island",
             "on_release": lambda x=f"Staten Island": self.set_neighborhood(x)
             }
        ]

        ages = [
            {"viewclass": "OneLineListItem",
             "text": "---",
             "on_release": lambda x=f"---": self.set_age(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "18 - 30",
             "on_release": lambda x=f"18-30": self.set_age(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "31 - 50",
             "on_release": lambda x=f"31-50": self.set_age(x),
             },
            {"viewclass": "OneLineListItem",
             "text": "50+",
             "on_release": lambda x=f"51-120": self.set_age(x),
             }
        ]

        self.menu_n = MDDropdownMenu(
            caller=self.ids.field_n,
            items=neighborhoods,
            position="auto",
            width_mult=3,)
        self.menu_a = MDDropdownMenu(
            caller=self.ids.field_a,
            items=ages,
            position="auto",
            width_mult=2,)

        self.ids.field_g.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message)

        app = App.get_running_app()
        self.api = app.api

    def set_neighborhood(self, text__neighbor):
<<<<<<< HEAD
        print(text__neighbor)
        print(text__neighbor=="---")
        if text__neighbor=='---':
            self.ids.field_n.text = text__neighbor
            filter = {"borough.eq":None}
        else:
            self.ids.field_n.text = text__neighbor
            filter = {"borough.eq":"'"+text__neighbor+"'"}


        self.menu_n.dismiss()
        self.api.setFilters(filter)
=======
        self.ids.field_n.text = text__neighbor
        self.menu_n.dismiss()
        neighborhood_filter = {"borough.eq": "'"+text__neighbor+"'"}
        self.api.set_filters(neighborhood_filter)
>>>>>>> 67d42751ac15b73338b41012b17871b925d23e29

    def set_guest(self, text__guest):
        print(text__guest.text)

    def set_error_message(self, instance_textfield):
        g_num = instance_textfield.text
        if g_num.isdigit():
            g_num = int(g_num)
            if g_num not in list(range(1, 17)):
                self.ids.field_g.error = True
<<<<<<< HEAD
                return
            self.ids.field_g.error = False
        else :
=======
        else:
>>>>>>> 1e034ec727cb1e274c8c71b44f0af0d9b2c45862
            self.ids.field_g.error = True
        
    def set_age(self, text__age):
        if text__age=="---":
            self.ids.field_a.text = ""
            filter = {"age.eq":None}
        else:
            self.ids.field_a.text = text__age
            filter = {"age.eq": f"'{text__age}'"}

        self.menu_a.dismiss()
<<<<<<< HEAD
=======
        age_filter = {"age.eq": f"'{text__age}'"}
>>>>>>> 67d42751ac15b73338b41012b17871b925d23e29
        res = [None]
        self.api.get_village_category(res, age_filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
            
<<<<<<< HEAD
        filter = {"village.in[]":village_list}
        self.api.setFilters(filter)
    """
    For the interests
    """
=======
        age_filter = {"village.in[]": village_list}
        self.api.set_filters(age_filter)

>>>>>>> 67d42751ac15b73338b41012b17871b925d23e29
    def set_chips(self, instance_chips):
        if instance_chips.color == [0, 0, 0, 0.1]:
            instance_chips.color = [252/255, 186/255, 3/255, 1]
<<<<<<< HEAD
            print(instance_chips.text)
            filters = self.api.filters
            filter={"interest.in[]": [instance_chips.text]}

            print(instance_chips.color)
            # call set_interests 
        else:
            instance_chips.color = [0, 0, 0, 0.1]
            filter = self.api.filters
        res = [None]    
        self.api.getVillageCategory(res,filter)
        print(res)
=======
            # call set_interests
        else:
            instance_chips.color = [0, 0, 0, 0.1]
>>>>>>> 67d42751ac15b73338b41012b17871b925d23e29

    def set_interests(self, text__interest):
        self.ids.field_i.text = text__interest
        self.menu_i.dismiss()
        interests_filter = {"interest.in[]": [text__interest]}
        res = [None]
        self.api.get_village_category(res, interests_filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
        interests_filter = {"village.in[]": village_list}
        self.api.set_filters(interests_filter)

    def set_highrating(self, status):
        pass

    def set_superhost(self, status):
        superhost_filter = {"is_superhost.eq": None}
        if status:
            superhost_filter['is_superhost.eq'] = True
        self.api.set_filters(superhost_filter)

    def set_fairfilter(self, status):
        fair_filter = {"total_listings_count.le": None}
        if status:
            fair_filter['total_listings_count.le'] = 3
        self.api.set_filters(fair_filter)

    def show_datepicker(self):
        picker = MDDatePicker()
        picker.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        picker.open()

    def switch_to_mapscreen(self):
        app = App.get_running_app()
        mapview = app.root.ids['mapview']
        # mapview.firstCall=True
        screenmanager = app.root.ids['screen_manager']
        screenmanager.current = "mapscreen"
        #mapview.get_airbnb_in_fov()
        #mapview._need_redraw_all = True
        #Clock.schedule_once(mapview.fakeClick,0.5)
        #Clock.schedule_once(mapview.get_airbnb_in_fov,0.1)
        #Clock.schedule_once(lambda dt: mapview.canvas.ask_update(), 0.5)


if __name__ == "__main__":

    class SliderApp(MDApp):
        def build(self):
            return Form()


    SliderApp().run()
