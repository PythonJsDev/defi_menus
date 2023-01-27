from collections import namedtuple
import pytest
from defi_menus.utils.menu import Menu

@pytest.fixture(scope="session")
def mock_menu():
    test_menu = Menu()
    test_menu.title = 'title test'
    test_menu.datas_menu = 'name'
    menu_content = namedtuple('menu_content', ['item_menu', 'action_menu'])
    test_menu.menu_entries = {
        '1': menu_content(item_menu='test item 1', action_menu='no action'),
        '2': menu_content(item_menu='test item 2', action_menu='action'),
    }
    return test_menu


# @pytest.fixture(scope="session")
# def mock_menu():
#     test_menu = Menu()
#     menu_content = namedtuple('menu_content', ['item_menu', 'action_menu'])
#     test_menu.menu_entries = {
#         '1': menu_content(item_menu='test item 1', action_menu='no action'),
#         '2': menu_content(item_menu='test item 2', action_menu='action'),
#     }
#     return test_menu