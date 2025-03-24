import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")


#Найти поле username, ввести значение tomsmith.

search_box = driver.find_element(By.NAME, "username")
search_box.send_keys("tomsmith")
time.sleep(5)

 #Найти поле password введите значение SuperSecretPassword!
search_box = driver.find_element(By.NAME, "password")
search_box.send_keys("SuperSecretPassword")
time.sleep(5)


 #Найти и нажать кнопку Login.
login_button = driver.find_element(By.NAME, "login")
login_button.click()

driver.quit()



