from defi_menus.controllers.home_menu_controller import HomeMenuController

class AppController():
    
    def start_app(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller.run()

     