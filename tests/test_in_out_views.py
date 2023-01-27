from  defi_menus.views import in_out_views
def test_clear_console(capsys):
    """Verifie que le terminal soit effacé"""
    in_out_views.clear_console()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_title(capsys):
    """Vérifie que le titre de l'application s'affiche dans le terminal"""
    in_out_views.title('my title')
    assert capsys.readouterr().out == '\n****** my title ******\n\n'

