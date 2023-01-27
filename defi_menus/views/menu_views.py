from .import in_out_views

class MenuView:
    """ Affichage des menus et saisie des choix de l'utilisateur"""
    def __init__(self, menu):
        self.menu = menu
        self.items = self.menu.items_menu
        # self.datas = self.menu.datas

    def display_menu(self, clear=True):
        if clear:
            in_out_views.clear_console()
        in_out_views.title(self.menu.title)
        
        for key, menu_content in self.items.items():
            print(f"{key}: {menu_content.item_menu}")

    def get_user_choice(self, clear=True) -> str:
        while True:
            self.display_menu(clear)
            print()
            choice = input("Votre choix: >> ")
            if self.menu.valid_key(choice):
                return self.items[str(choice)].action_menu
            
    def datas_to_transmit(self):
        while True:
            print()
            self.datas = input("Donnée(s) à transmettre au menu suivant: >> ")
            return self.datas
