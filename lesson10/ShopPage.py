from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации.

    Атрибуты:
        driver (webdriver): Объект драйвера Selenium для управления браузером.
        username_input (tuple): Локатор поля ввода имени пользователя.
        password_input (tuple): Локатор поля ввода пароля.
        login_button (tuple): Локатор кнопки входа.
    """

    @allure.step("Авторизация в магазине" )
    def __init__(self, driver):
        """     Параметры:
                    driver (webdriver): Объект драйвера Selenium для управления браузером.

                Возвращаемое значение:
                    None
                """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input))
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')


    @allure.step("Добавление товаров в корзину")
    def login(self, username, password):
        """Метод для авторизации пользователя.

               Параметры:
                   username (str): Имя пользователя.
                   password (str): Пароль пользователя.

               Возвращаемое значение:
                   None
               """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class MainPage:
    """
               Главная страница магазина.

               Атрибуты:
                   driver (webdriver): Объект драйвера Selenium для управления браузером.
                   cart_link (tuple): Локатор корзины.
               """
    @allure.step("Переход на главную страницу")
    def __init__(self, driver):
        """Конструктор класса MainPage.

                Параметры:
                    driver (webdriver): Объект драйвера Selenium для управления браузером.

                Возвращаемое значение:
                    None
                """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("")
    def add_item_to_cart(self, item: str) -> None:
        """Метод добавляет товар в корзину.

                Параметры:
                    item (str): Идентификатор элемента (например, ID товара).

                Возвращаемое значение:
                    None
                """
        self.driver.find_element(By.ID, item).click()

    @allure.step("переход на страницу ")
    def go_to_cart(self) -> None:
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step("переход в корзину")
    def go_to_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, 'cart_item')


class CheckoutPage:
    """
        Страница оформления заказа.

        Атрибуты:
            driver (webdriver): Объект драйвера Selenium для управления браузером.
            first_name_input (tuple): Локатор поля ввода имени.
            last_name_input (tuple): Локатор поля ввода фамилии.
            zip_code_input (tuple): Локатор поля ввода ZIP-кода.
            continue_button (tuple): Локатор кнопки продолжения.
            total_price (tuple): Локатор итоговой стоимости заказа.
        """

    @allure.step("Переход к оформлению заказа")
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.zip_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_price = (By.CLASS_NAME, 'summary_total_label')

    @allure.step("Заполнение формы оформления заказа")
    def fill_checkout_form(self, first_name, last_name, zip_code):
        """Метод заполняет форму доставки.

                Параметры:
                    first_name (str): Имя заказчика.
                    last_name (str): Фамилия заказчика.
                    zip_code (str): Почтовый индекс.

                Возвращаемое значение:
                    None
                """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Проверка итоговой стоимости")
    def get_total_price(self):
        """Возвращает строку с итоговой стоимостью заказа.

              Возвращаемое значение:
                  str: Текущая итоговая стоимость заказа.
              """
        return self.driver.find_element(*self.total_price).text

