import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


first_nam = driver.find_element(By.NAME, 'first-name')
first_nam.send_keys('Иван')
last_nam = driver.find_element(By.NAME, 'last-name')
last_nam.send_keys('Петров')
address_nam = driver.find_element(By.NAME, 'address')
address_nam.send_keys('Ленина, 55-3')
email_nam = driver.find_element(By.NAME, 'e-mail')
email_nam.send_keys('test@skypro.com')
phone_num = driver.find_element(By.NAME, 'phone')
phone_num.send_keys('+7985899998787')
zipcode_num = driver.find_element(By.NAME, 'zip-code')
zipcode_num.send_keys('')
city_nam = driver.find_element(By.NAME, 'city')
city_nam.send_keys('Москва')
country_nam = driver.find_element(By.NAME, 'country')
country_nam.send_keys('Россия')
jobpos_nam = driver.find_element(By.NAME, 'job-position')
jobpos_nam.send_keys('QA')
comp_nam = driver.find_element(By.NAME, 'company')
comp_nam.send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#проверка
def test_check_colors():
    zip_code_element = driver.find_element(By.ID, 'zip-code')
    zip_code_class = zip_code_element.get_attribute("class")
    assert "danger" in zip_code_class, "Поле Zip code не подсвечено красным (класс danger)"

first_namе = driver.find_element(By.ID, 'first-name')
first_name_class = first_namе.get_attribute("class")
assert "success" in first_name_class, "Поле First_Name не подсвечено зеленым (класс success)"

last_name = driver.find_element(By.ID, 'last-name')
last_name_class = last_name.get_attribute("class")
assert "success" in last_name_class, "Поле Last_Name не подсвечено зеленым (класс success)"

address_element = driver.find_element(By.ID, 'address')
address_class = address_element.get_attribute("class")
assert "success" in address_class, "Поле Address не подсвечено зеленым (класс success)"

email_element = driver.find_element(By.ID, 'e-mail')
email_class = email_element.get_attribute("class")
assert "success" in email_class, "Поле Email не подсвечено зеленым (класс success)"

phone_number_element = driver.find_element(By.ID, 'phone')
phone_number_class = phone_number_element.get_attribute("class")
assert "success" in phone_number_class, "Поле Phone Number не подсвечено зеленым (класс success)"

city_element = driver.find_element(By.ID, 'city')
city_class = city_element.get_attribute("class")
assert "success" in city_class, "Поле City не подсвечено зеленым (класс success)"

country_element = driver.find_element(By.ID, 'country')
country_class = country_element.get_attribute("class")
assert "success" in country_class, "Поле Country не подсвечено зеленым (класс success)"

job_position_element = driver.find_element(By.ID, 'job-position')
job_position_class = job_position_element.get_attribute("class")
assert "success" in job_position_class, "Поле Job_Position не подсвечено зеленым (класс success)"

company_element = driver.find_element(By.ID, 'company')
company_class = company_element.get_attribute("class")
assert "success" in company_class, "Поле Company не подсвечено зеленым (класс success)"
test_check_colors()

driver.quit()

