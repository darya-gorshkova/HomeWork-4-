from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self,delay):
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)


    def click_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    def wait_results(self, result, delay):
        waiter = WebDriverWait(self.driver, delay + 1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), str(result)))
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text