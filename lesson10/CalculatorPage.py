from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Calculator:
    """
        Класс для представления веб-интерфейса калькулятора и автоматизации действий над ним.

        Методы:
            __init__(): Конструктор класса, открывающий страницу калькулятора.
            set_delay(int): Устанавливает задержку между действиями на странице.
            click_button(int): Кликает заданную кнопку на калькуляторе.
            wait_results(int): Ждет появления указанного результата на экране калькулятора.

        Атрибуты:
            driver (webdriver): Объект драйвера Selenium для управления браузером.
        """
    @allure.step('Открыть страницу калькулятора')  # Шаг: Открытие страницы
    def __init__(self, driver):
        """
                Конструктор класса, инициализирует драйвер и открывает страницу калькулятора.

                Аргументы:
                    driver (webdriver): Драйвер Selenium для управления браузером.
                """
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step('Установить задержку на калькуляторе ({delay}) мс')  # Шаг: Установка заде
    def set_delay(self,delay):
        """
              Метод устанавливает задержку между нажатиями кнопок на калькуляторе.

              Аргументы:
                  delay (int): Значение задержки в миллисекундах.
              """
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step('Нажать кнопку "{button}"')  # Шаг: Нажатие конкретной кнопки
    def click_button(self, button):
        """
                Метод нажимает указанную кнопку на калькуляторе.

                Аргументы:
                    button (str): Название кнопки ("+", "-", "*", "/", цифры).
                """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step('Ждем появление результата "{result}" с задержкой {delay}')  # Шаг: Проверка результата
    def wait_results(self, result, delay):
        """
                Метод ожидает появления определенного значения на дисплее калькулятора.

                Аргументы:
                    result (int): Результат, который ожидается увидеть на экране.
                    delay (float): Задержка ожидания результата.

                Возвращает:
                    text (str): Текущее значение на экране калькулятора.
                """
        waiter = WebDriverWait(self.driver, delay + 1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(result)))
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text

