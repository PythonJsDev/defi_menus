from collections import namedtuple
from typing import Any


class Menu:
    """ Classe de création des menus """
    def __init__(self):
        self.menu_entries = {}
        self.menu_title = ""
        self.auto_num = 1

    @property
    def title(self) -> str:
        return self.menu_title.upper()

    @title.setter
    def title(self, menu_title: str):
        self.menu_title = menu_title

    def add(self, key: str,  item_menu: str, action_menu: Any):
        if key == "auto":
            key = str(self.auto_num)
            self.auto_num += 1
        menu_content = namedtuple('menu_content', ['item_menu', 'action_menu'])
        self.menu_entries[str(key)] = menu_content(item_menu, action_menu)

        
    @property
    def items_menu(self) -> dict:
        """Retourne les items du menu"""
        return self.menu_entries

    def valid_key(self, choice: str) -> bool:
        """Retourne True si le choix de l'utilisateur est valide sinon False"""
        return choice in self.menu_entries

