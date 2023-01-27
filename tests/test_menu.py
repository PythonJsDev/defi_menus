from defi_menus.utils.menu import Menu
from collections import namedtuple


def test_title(mock_menu):
    """Verifie la mise en majuscule du titre"""
    assert mock_menu.title == 'TITLE TEST'

def test_datas_menu(mock_menu):
    """Verifie la mise en majuscule du titre"""
    assert mock_menu.datas_menu == 'name'

def test_add_auto_key():
    """Verifie l'ajout d'un item au menu avec numérotation automatique"""
    test_menu = Menu()
    menu_content = namedtuple('menu_content', ['item_menu', 'action_menu'])
    test_menu.add(key="auto", item_menu="test item 1", action_menu="no action")
    assert test_menu.items_menu == {
        '1': menu_content(item_menu='test item 1', action_menu='no action')
    }


def test_add_not_auto_key():
    """Verifie l'ajout d'un item au menu sans numérotation automatique"""
    test_menu = Menu()
    menu_content = namedtuple('menu_content', ['item_menu', 'action_menu'])
    test_menu.add(key="a", item_menu="test item 1", action_menu="no action")
    assert test_menu.items_menu == {
        'a': menu_content(item_menu='test item 1', action_menu='no action')
    }


def test_valid_key(mock_menu):
    """Verifie la validité du choix du menu par l'utilisateur"""
    assert mock_menu.valid_key('1')


def test_not_valid_key(mock_menu):
    """Verifie la non validité du choix du menu par l'utilisateur"""
    assert not mock_menu.valid_key('11')