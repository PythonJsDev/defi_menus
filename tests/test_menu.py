from defi_menus.utils.menu import Menu


def test_title(mock_menu):
    """Verifie la mise en majuscule du titre"""
    assert mock_menu.title == 'TITLE TEST'

def test_add_auto_key():
    """Verifie l'ajout d'un item au menu avec numérotation automatique"""
    test_menu = Menu()
    items = [['test item 1', 'action_1'], ['test item 2', 'action_2']]
    test_menu.add(key="auto", item_menu=items)
    assert test_menu.items_menu == {
        '1': [['test item 1', 'action_1'], ['test item 2', 'action_2']]
    }


def test_add_not_auto_key():
    """Verifie l'ajout d'un item au menu sans numérotation automatique"""
    test_menu = Menu()
    items = [['test item 1', 'action_1'], ['test item 2', 'action_2']]
    test_menu.add(key="a", item_menu=items)
    assert test_menu.items_menu == {
        'a': [['test item 1', 'action_1'], ['test item 2', 'action_2']]
    }


def test_valid_key(mock_menu):
    """Verifie la validité du choix du menu par l'utilisateur"""
    assert mock_menu.valid_key('1')


def test_not_valid_key(mock_menu):
    """Verifie la non validité du choix du menu par l'utilisateur"""
    assert not mock_menu.valid_key('11')