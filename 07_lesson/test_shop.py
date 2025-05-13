import pytest
from selenium import webdriver
from ShopPage import *


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_shop(driver):
    # Шаг 1: Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Шаг 2: Добавление товаров в корзину
    main_page = MainPage(driver)
    main_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")  # Добавляем "Sauce Labs Backpack"
    main_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")  # Добавляем "Sauce Labs Bolt T-Shirt"
    main_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")  # Добавляем "Sauce Labs Onesie"

    # Шаг 3: Переход в корзину
    main_page.go_to_cart()

    # Шаг 4: Переход к оформлению заказа
    cart_page = CartPage(driver)
    cart_page.go_to_checkout()

    # Шаг 5: Заполнение формы оформления заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("John", "Doe", "12345")

    # Шаг 6: Проверка итоговой стоимости
    total_price = checkout_page.get_total_price()

    assert total_price == "Total: $58.29", f"Expected total price to be $58.29, but got {total_price}"