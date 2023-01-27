from defi_menus.controllers.home_menu_controller import HomeMenuController
# from ..controllers import home_menu_controller

class MenuManager():
    def __init__(self, menu_name):
        self.menu_name = menu_name
    
    def run(self):
        if self.menu_name == 'home_menu':
            print('home')
            # home_menu_controller.HomeMenuController()
            HomeMenuController()
    