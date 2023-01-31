from defi_menus.controllers import menu_controller
from defi_menus.controllers.constants import SWITCH


class MenuManager:
    def __init__(self, next_menu, datas_to_transmit):
        self.next_menu = next_menu
        self.datas_to_transmit = datas_to_transmit

    def run(self):
        if self.next_menu:
            if self.next_menu == 'previous':
                h = menu_controller.MenuController.get_nav_history()
                if h[-1] == 'previous':
                    h[-1] = h[-3]
                return menu_controller.MenuController(
                    SWITCH.get(h[-1].upper()), self.datas_to_transmit
                )

            return menu_controller.MenuController(
                SWITCH.get(self.next_menu.upper()), self.datas_to_transmit
            )
        return menu_controller.MenuController(self.next_menu, "")

   