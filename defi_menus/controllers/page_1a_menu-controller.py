
from ..utils.menu import Menu, MenuManager
from ..utils import menu
from ..views.menu_views import MenuView
from .import home_menu_controller
from ..views import in_out_views


class Page1MenuController():
    def __init__(self):
        self.menu = Menu()
        self.view = MenuView(self.menu)
    
         

    def run(self):
        self.menu.title = "La page 1"
        print(home_menu_controller.HomeMenuController.get_nav(self))

        self.menu.add("auto", "vers la page 1aa", "")
        self.menu.add("auto", "vers la page 1bb", "")
        self.menu.add("auto", "Menu précédent", "")
        self.menu.add("auto", "Revenir à l'accueil", home_menu_controller.HomeMenuController())
        self.menu.add("auto", "Quitter le programme", None)
        # user_choice = self.view.get_user_choice()
        # return user_choice
    
    