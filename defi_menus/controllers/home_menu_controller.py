from ..utils.menu import Menu
from ..views.menu_views import MenuView
from . page_1_menu_controller import Page1MenuController


class HomeMenuController:
    """ Menu principal de l'application """
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)

    
    def run(self):
        self.menu.title = "Accueil"
        
        self.menu.add("auto", "aller à la page 1", Page1MenuController('home_menu'))
        self.menu.add("auto", "aller à la page 2", None)
        self.menu.add("auto", "aller à la page 3", None)
        self.menu.add("auto", "Quitter le programme", None)
        user_choice = self.view.get_user_choice()
        return user_choice