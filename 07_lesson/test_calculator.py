import pytest
from selenium import webdriver
from CaiculatorPage import Calculator


@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver


def test_calculator_form(chrome_browser):
        calculator = Calculator(chrome_browser)
        calculator.set_delay(1)
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')
        assert calculator.wait_results(15, 1) == '15', "Результат сложения неверен."