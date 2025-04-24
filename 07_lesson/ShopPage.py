from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'user-name')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item):
        self.driver.find_element(By.ID, item).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, 'cart_item')



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, 'first-name')
        self.last_name_input = (By.ID, 'last-name')
        self.zip_code_input = (By.ID, 'postal-code')
        self.continue_button = (By.ID, 'continue')
        self.total_price = (By.CLASS_NAME, 'summary_total_label')

    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text

