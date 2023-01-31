from defi_menus.controllers.menu_controller import MenuController
from defi_menus.controllers import constants
class AppController:
    
    def start_app(self):
        self.controller = MenuController(constants.HOME, "")
        while self.controller:
            self.controller = self.controller.run()

     