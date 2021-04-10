from kivymd.uix.dialog import MDDialog


class SearchPopupMenu(MDDialog):
    title = "Search neighbourhood"
    type = 'custom'

    def __init__(self):
        super(SearchPopupMenu, self).__init__()
        self.size_hint = [.9, .3]
