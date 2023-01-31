from collections import namedtuple
import pytest
from defi_menus.utils.menu import Menu

@pytest.fixture(scope="session")
def mock_menu():
    test_menu = Menu()
    test_menu.title = 'title test'
    
    test_menu.menu_entries = {
        '1': 'test item 1',
        '2': 'test item 2',
    }
    return test_menu
