from ..utils.menu import Menu
from ..views.menu_views import MenuView
from defi_menus.utils.menu_manager import MenuManager


class MenuController:
    """Menus de l'application"""
    nav_history = ['ACCUEIL']
    def __init__(self, params_menu: dict, datas_to_transmit: str):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.params_menu = params_menu
        self.datas_to_transmit = datas_to_transmit

    def run(self):
        if self.params_menu:
            self.menu.title = self.params_menu.get("title")
            self.menu.datas_to_transmit = self.datas_to_transmit
           
            for item, item_menu in self.params_menu.get("items"):
                self.menu.add("auto", item)
            
            choice, datas = self.view.get_user_choice()
            next_page = self.params_menu.get("items")[int(choice) - 1][1]
            MenuController.nav_history.append(next_page)
            return MenuManager(next_page, datas).run()
        return None
    
    
    @staticmethod
    def get_nav_history():
        return MenuController.nav_history
