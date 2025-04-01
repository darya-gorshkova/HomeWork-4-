from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

wait = WebDriverWait(driver, 20)

driver.find_element(By.ID, "ajaxButton").click()
success_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))
print(success_text.text)

driver.quit()

