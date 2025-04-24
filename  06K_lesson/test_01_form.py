from selenium import webdriver
from selenium.webdriver.common.by import By


def test_check_colors():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, 'first-name').send_keys('Иван')
    driver.find_element(By.NAME, 'last-name').send_keys('Петров')
    driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
    driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
    driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
    driver.find_element(By.NAME, 'zip-code').send_keys('')
    driver.find_element(By.NAME, 'city').send_keys('Москва')
    driver.find_element(By.NAME, 'country').send_keys('Россия')
    driver.find_element(By.NAME, 'job-position').send_keys('QA')
    driver.find_element(By.NAME, 'company').send_keys('SkyPro')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#проверка
    assert "danger" in driver.find_element(By.ID, 'zip-code').get_attribute("class"), "Поле Zip code не подсвечено красным"
    assert "success" in driver.find_element(By.ID, 'first-name').get_attribute("class"), "Поле First_Name не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'last-name').get_attribute("class"),"Поле Last_Name не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'address').get_attribute("class"),"Поле Address не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'e-mail').get_attribute("class"),"Поле Email не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'phone').get_attribute("class"), "Поле City не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'city').get_attribute("class"), "Поле City не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'country').get_attribute("class"), "Поле Country не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'job-position').get_attribute("class"), "Поле Job_Position не подсвечено зеленым"
    assert "success" in driver.find_element(By.ID, 'company').get_attribute("class"), "Поле Company не подсвечено зеленым"

    driver.quit()