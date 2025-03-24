import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#открыть страницу
driver = webdriver.Chrome()
driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку  Add Element
button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
button.click()
button.click()
button.click()
button.click()
button.click()

# список кнопок Delete
delete_buttons_xpath = "//button[@data-action='delete']"
delete_buttons = driver.find_elements(By.XPATH, delete_buttons_xpath)

# Вывести размер списка
print(len(delete_buttons))

time.sleep(5)

driver.quit()

