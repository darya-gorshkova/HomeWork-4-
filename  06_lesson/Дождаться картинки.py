from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 20)

images = waiter.until(

    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container")))


print(len(images))

src = images[2].get_attribute("src")
print("src")



driver.quit()

