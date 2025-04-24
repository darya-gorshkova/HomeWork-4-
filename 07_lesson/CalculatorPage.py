import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self,delay):
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)


    def click_button(button):
        self.driver.find_element(By.XPATH, "//span[text()='']").click()

    def wait_results(self):
        element = self.wait_results().until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "delay"), "delay")
    )
        return element





