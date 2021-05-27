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
        self.interests = set()

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

        if text__neighbor=='---':
            self.ids.field_n.text = text__neighbor
            borough_filter = {"borough.eq":None}
        else:
            self.ids.field_n.text = text__neighbor
            borough_filter = {"borough.eq":"'"+text__neighbor+"'"}


        self.menu_n.dismiss()
        self.api.set_filters(borough_filter)

    def set_guest(self, n_guests):
        guest_filter = {"guests_inclueded.ge":n_guests}
        self.api.set_filters(guest_filter)

    def set_error_message(self, instance_textfield):
        print(instance_textfield.text)
        g_num = instance_textfield.text
        if g_num.isdigit():
            g_num = int(g_num)
            if g_num not in list(range(1, 17)):
                self.ids.field_g.error = True
                return
            self.set_guest(g_num)
            self.ids.field_g.error = False
        else:
            self.ids.field_g.error = True
        
    def set_age(self, text__age):
        if text__age=="---":
            self.ids.field_a.text = ""
            age_filter = {"age.eq":None}
        else:
            self.ids.field_a.text = text__age
            age_filter = {"age.eq": f"'{text__age}'"}
        self.api.set_filters(age_filter)
        self.menu_a.dismiss()
        res = [None]
        self.api.get_village_category(res, age_filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
            
        village_filter = {"village.in[]":village_list}
        self.api.set_filters(village_filter)


    """
    For the interests
    """
    def set_interest(self, instance_chips):
        if instance_chips.color == [0, 0, 0, 0.1]:
            instance_chips.color = [252/255, 186/255, 3/255, 1]
            self.interests.add(instance_chips.text)
            print(instance_chips.color)
        else:
            instance_chips.color = [0, 0, 0, 0.1]
            self.interests.discard(instance_chips.text)

        interest_filter = {"interest.in[]":self.interests}
        self.api.set_filters(interest_filter)
        res = [None]    
        self.api.get_village_category(res,interest_filter)
        village_list = []
        for i in res[0]:
            village_list.append(i[0])
        village_filter = {"village.in[]": village_list}
        self.api.set_filters(village_filter)



    def set_highrating(self, status):
        rating_filter = {"review_score.ge":None}
        if(status):
            rating_filter["review_score.ge"] = 90
        self.api.set_filters(rating_filter)

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
        price_range=self.ids.price_filter.value
        print(price_range)
        if(price_range[0]==0):
            price_range[0]=None
        if(price_range[1]==9999):
            price_range[1]=None
        price_filter = {"price.ge":price_range[0],"price.le":price_range[1]}
        
        self.api.set_filters(price_filter)
        app = App.get_running_app()

        # mapview.firstCall=True
        screenmanager = app.root.ids['screen_manager']
        screenmanager.current = "mapscreen"
        mapview = app.root.ids['mapview']
        #mapview.get_airbnb_in_fov()
        #mapview._need_redraw_all = True
        #Clock.schedule_once(mapview.fakeClick,0.5)
        #Clock.schedule_once(mapview.get_airbnb_in_fov,0.1)
        #Clock.schedule_once(lambda dt: mapview.canvas.ask_update(), 0.5)

    def set_price(self, price):
        print(price)

if __name__ == "__main__":

    class SliderApp(MDApp):
        def build(self):
            return Form()


    SliderApp().run()
