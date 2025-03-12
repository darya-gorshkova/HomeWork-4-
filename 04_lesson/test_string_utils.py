from pickle import FALSE

import pytest
from string_utils import StringUtils


string_utils = StringUtils()

#capitalize
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("aabbcc", "Aabbcc"), #Многократные буквы
    ("skypro", "Skypro"), #Буквы в нижнем регистре
    ("another example", "Another example"),#Строка с пробелами
])

def test_capitalize_positive(input_str, expected):
    utils = StringUtils()
    result = utils.capitalize(input_str)
    assert result == expected
#trim
#Несколько  пробелов в начале и в конце:
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    hello world    ", "hello world"),
    ("   python   ", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


#Пробелы (вместо символов)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", "")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


#Пустая строка
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", "")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


#Пустой список
@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [ ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

#contains
#Символ в середине строки
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("hello world", "l", True),
    ("hello world", "h", True),
    ("hello world", "r", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


#Символ в начале строки:
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert StringUtils().contains("SkyPro", "S")


#Нет совпадений
@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "z", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert not StringUtils().contains("SkyPro", "z")

#delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("hello world", "h", "ello world"), #один символ
    ("python", "th", "pyoo"),#несколько символов в середине
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

#Некорректные данные
pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (123, "l", TypeError),
    ("", "a", None),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    with pytest.raises(expected):
        string_utils.delete_symbol(input_str, symbol)
