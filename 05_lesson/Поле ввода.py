import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get(" http://the-internet.herokuapp.com/inputs")


search_box = driver.find_element(By.TAG_NAME, 'input')
search_box.send_keys('1000') #вводим в поле ввода 1000
time.sleep(10)
search_box.clear() #чистить поле
search_box.send_keys('999') #вводим в это же поле значение 999
time.sleep(10)


driver.quit()

