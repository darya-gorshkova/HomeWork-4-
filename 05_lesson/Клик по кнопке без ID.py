from selenium import webdriver
from selenium.webdriver.common.by import By


import time

#Открываем страницу
driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')
time.sleep(5)


for i in range(3):
    button = driver.find_element(By.CSS_SELECTOR, '.btn-primary') #выбор кнопки по значению цвет
    button.click()
time.sleep(5)

driver.quit()

