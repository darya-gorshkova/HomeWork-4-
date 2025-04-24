
from selenium import driver
from selenium.webdriver.common.by import By


class Page_Avtorize:
   def __init__(self, driver):
       self.driver = driver
       self.driver.get("http://www.saucedemo.com/")


   def __enter__(self):
       self.driver.find_element(By.ID, "user-name")
       self.driver.find_element(By.ID, "password")

#driver.find_element(By.ID, "login-button").click()
   def










