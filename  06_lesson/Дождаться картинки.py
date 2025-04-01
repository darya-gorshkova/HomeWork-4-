from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 30)


images = wait.until(
    lambda driver: driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    if len(driver.find_elements(By.CSS_SELECTOR, "#image-container img")) == 4
    else False
)

src = images[2].get_attribute("src")
print(f"Ссылка на третье изображение: {src}")

driver.quit()

