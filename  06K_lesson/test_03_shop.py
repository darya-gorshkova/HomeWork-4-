from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


def test_total():
     driver = webdriver.Chrome()
     driver.get("http://www.saucedemo.com/")
     driver.implicitly_wait(5)
     driver.find_element(By.ID, "user-name").send_keys("standard_user")
     driver.find_element(By.ID, "password").send_keys("secret_sauce")
     driver.find_element(By.ID, "login-button").click()
     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
     driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
     driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
     driver.find_element(By.ID, "shopping_cart_container").click()
     driver.find_element(By.ID, "checkout").click()
#Заполните форму своими данными:
     driver.find_element(By.ID, "first-name").send_keys("Darya")
     driver.find_element(By.ID, "last-name").send_keys("Gorshkova")
     driver.find_element(By.ID, "postal-code").send_keys("607652")
     driver.find_element(By.ID, "continue").click()

     total = driver.find_element(By.CLASS_NAME, "summary_total_label").text
     expected_total = "Total: $58.29"
     assert total == expected_total


     driver.quit()




