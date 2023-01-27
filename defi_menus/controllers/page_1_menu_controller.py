from ..utils.menu import Menu
from . menu_manager import MenuManager
from ..views.menu_views import MenuView
from .import home_menu_controller


class Page1MenuController():
    def __init__(self, menu_name):
        self.menu = Menu()
        self.view = MenuView(self.menu)
        self.menu_name = menu_name
         
    
    def run(self):
        self.menu.title = "La page 1"
        self.menu.add("auto", "vers la page 1a", "")
        self.menu.add("auto", "vers la page 1b", "")
        self.menu.add("auto", "Menu précédent", MenuManager(self.menu_name))
        self.menu.add("auto", "Revenir à l'accueil", home_menu_controller.HomeMenuController())
        self.menu.add("auto", "Quitter le programme", None)
        user_choice = self.view.get_user_choice()
        return user_choice
