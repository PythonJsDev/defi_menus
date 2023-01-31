from . import in_out_views


class MenuView:
    """Affichage des menus et saisie des choix de l'utilisateur"""

    def __init__(self, menu):
        self.menu = menu
        self.menu_items = self.menu.items_menu

    def display_menu(self, clear: bool = True):
        """Affiche le menu et les données transmisent"""
        if clear:
            in_out_views.clear_console()
        in_out_views.title(self.menu.title)
        datas_to_print = self.menu.datas_to_transmit
        if datas_to_print:
            in_out_views.datas_to_display(datas_to_print)

        for key, value in self.menu_items.items():
            print(key, value)

    def get_user_choice(self, clear: bool = True) -> tuple[str, str]:
        """Affiche le menu et les données transmisent tant que le
        choix de l'utilisateur n'est pas valide"""
        while True:
            self.display_menu(clear)
            print()
            choice = input("Votre choix: >> ")
            if self.menu.valid_key(choice):
                datas = (
                    self.get_datas_to_transmit(choice)
                    if not self.menu.quit_key(choice)
                    else ''
                )
                return choice, datas

    def get_datas_to_transmit(self, choice: str):
        print()
        print(
            (
                "Vous pouvez passer plusieurs données en"
                " les séparants par des ',' ou des ';'."
            )
        )
        return input(f"Donnée(s) à transmettre au menu {choice}: >> ")
