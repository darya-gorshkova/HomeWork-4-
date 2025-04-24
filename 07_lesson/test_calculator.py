import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import Calculator


@pytest.fixture(scope="function")
def chrome_browser():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver


def test_calculator_form(chrome_browser):
        calculator = Calculator(chrome_browser)
        calculator.set_delay(1)
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')


def test_wait_results(self):
        self.wait_results().until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
        return self.driver.find_elements(*self.results_selector)

        final_result = self.calculator.read_result()
        self.assertEqual(final_result, "15", "Результат сложения неверен.")

