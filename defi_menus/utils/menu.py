from collections import namedtuple
from typing import Any
from defi_menus.controllers.constants import QUIT_APP

class Menu:
    """ Classe de création des menus """
    def __init__(self):
        self.menu_entries = {}
        self.menu_title = ""
        self.menu_datas = ""
        self.auto_num = 1

    @property
    def title(self) -> str:
        return self.menu_title.upper()

    @title.setter
    def title(self, menu_title: str):
        self.menu_title = menu_title

    def add(self, key: str,  item_menu: str):
        if key == "auto":
            key = str(self.auto_num)
            self.auto_num += 1
        self.menu_entries[str(key)] = item_menu
        
    @property
    def items_menu(self) -> dict:
        """Retourne les items du menu"""
        return self.menu_entries

    def valid_key(self, choice: str) -> bool:
        """Retourne True si le choix de l'utilisateur est valide sinon False"""
        return choice in self.menu_entries
    
    def quit_key(self, choice: str) -> bool:
        """Retourne True si le choix de l'utilisateur est de quitter le programme sinon False"""
        if self.menu_entries.get(choice) == QUIT_APP:
            return True
        return False


    @property
    def datas_to_transmit(self) -> str:
        """Retourne les datas à transmettre"""
        return self.menu_datas
    
    @datas_to_transmit.setter
    def datas_to_transmit(self, menu_datas: str):
        """Saisie des datas à transmettre"""
        self.menu_datas = menu_datas