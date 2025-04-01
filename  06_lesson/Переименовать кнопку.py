from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")
wait = WebDriverWait(driver, 15)

input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro"))

print(button.text)

driver.quit()

