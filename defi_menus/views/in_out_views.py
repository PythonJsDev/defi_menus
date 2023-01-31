import os
import sys
""" Fonctions d'affichage et de saisie de donneés utilisées dans les modules du package views """


def clear_console():
    """Nettoyage de la console pour windows ou mac"""
    os.system('cls') if sys.platform.startswith('win32') else os.system('clear')


def title(title: str):
    print()
    print("****** " + title + " ******")
    print()


def get_user_entry(msg: str, ask_for: str, default_value: str) -> str:
    usr_entry = input(ask_for + " >> ").strip()
    while not usr_entry:
        if default_value:
            usr_entry = default_value
        else:
            usr_entry = input(ask_for + " >> ").strip()
    return usr_entry


def datas_to_display(datas:str):
    if datas :
        print("Donnée(s) en provenance du menu précédent:")
        print(datas)
        print()
