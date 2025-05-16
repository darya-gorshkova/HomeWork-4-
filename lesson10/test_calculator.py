import pytest
from selenium import webdriver
from lesson10.CalculatorPage import (Calculator)
import allure


@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Проверка калькулятора: сложение чисел")
@allure.description("Тестирование формы калькулятора путем выполнения операции сложения.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator_form(chrome_browser):
    with allure.step("Инициализация страницы калькулятора"):
        calculator = Calculator(chrome_browser)

    with allure.step("Установка задержки"):
        calculator.set_delay(1)

    with allure.step("Нажатие кнопки '7'"):
        calculator.click_button('7')

    with allure.step("Нажатие кнопки '+'"):
        calculator.click_button('+')

    with allure.step("Нажатие кнопки '8'"):
        calculator.click_button('8')

    with allure.step("Нажатие кнопки '='"):
        calculator.click_button('=')

    # Проверяем результат вычисления
    @allure.step("Проверка результата сложения")
    def check_result():
        result = calculator.wait_results(15, 1)
        assert result == '15', f'Ошибка! Ожидалось {result}, получилось 15'

    check_result()