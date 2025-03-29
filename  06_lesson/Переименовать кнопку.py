from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

search_box = driver.find_element(By.TAG_NAME, 'input')
search_box.send_keys('SkyPro')

driver.find_element(By.ID, "updatingButton").click()

wait = WebDriverWait(driver, 15)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".btn.btn-primary"), "SkyPro"))


driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").text


txt = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").text
print(txt)

driver.quit()

