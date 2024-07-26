import pytest
from string_utils import StringUtils
utils = StringUtils()

@pytest.mark.parametrize("in_string, ex_string" , [("skypro", "Skypro"),
                                                  ("", ""), (" ", " "),
                                                  ("123", "123"),
                                                  ("Строка с пробелами", "Строка с пробелами")
])
def test_capitilize(in_string, ex_string):
    assert utils.capitilize(in_string) == ex_string



def test_trim():
    assert utils.trim(" skypro") == "skypro"
    assert utils.trim(" Строка с пробелами ") == "Строка с пробелами "
    assert utils.trim("") == ""
@pytest.mark.xfail()
def test_trim_nums():
    assert utils.trim(9999) == "9999"
@pytest.mark.xfail()
def test_trim_space():
    assert utils.trim(" Строка с пробелами ") == "Строка с пробелами "


@pytest.mark.parametrize("string, delimeter, result", [("Случайный,набор,слов", ",", ["Случайный", "набор", "слов"]), ("", None, [])])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [("skypro", "s", True),
                                                   ("skypro%", "%", True),
                                                   ("skypro1", "1", True),
                                                   ("", "", True),
                                                   ("Skypro", "s", False),
                                                   ("999", "$", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [("skypro", "s", "kypro"),
                                                   ("skypro%", "%", "skypro"),
                                                   ("skypro1", "2", "skypro1"),
                                                   ("", "", ""),
                                                   ("skypro ", " ", "skypro"),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [("skypro", "s", True),
                                                   ("skypro%", "%", False),
                                                   ("999", "9", True),
                                                   ("skypro", "k", False),
                                                   ("skypro ", " ", False),
])
def test_start_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [("skypro", "o", True),
                                                   ("skypro%", "r", False),
                                                   ("999", "9", True),
                                                   ("", "", True),
                                                   ("skypro ", " ", True),
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize("string, result", [("", True),
                                            ("    ", True),
                                            ("skypro", False),
                                            ("999", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


@pytest.mark.parametrize("lst, joiner, result", [(["Точь", "в", "точь"], "-", "Точь-в-точь"),
                                                 ([9, 8, 7, 6], None, "9, 8, 7, 6"),
                                                 ([], "-", ""),
                                                 (["Тарелка", "плова"], ",готового,", "Тарелка,готового,плова"),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
