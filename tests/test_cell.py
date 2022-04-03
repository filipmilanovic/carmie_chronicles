from classes.cells import Cell


def test_create_cell():
    assert Cell() is not None


def test_valid_cell_appearance():
    assert Cell().appearance == 'o'
