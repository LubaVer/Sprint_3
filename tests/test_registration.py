from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


faker = Faker()

class TestRegistration:
    def test_registration(self, driver):
        email = faker.email()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//fieldset[1]/div[1]/div[1]/input[1]").send_keys("Love")
        driver.find_element(By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]").send_keys(email)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Вход')]")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_registratio_short_password(self, driver):
        email = faker.email()
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//fieldset[1]/div[1]/div[1]/input[1]").send_keys("Love")
        driver.find_element(By.XPATH, "//fieldset[2]/div[1]/div[1]/input[1]").send_keys(email)
        driver.find_element(By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20']//input[@type='password']").send_keys("1234")
        driver.find_element(By.XPATH, "//button[contains(text(),'Зарегистрироваться')]").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]")))
        assert driver.find_element(By.XPATH, "//p[contains(text(),'Некорректный пароль')]").text =='Некорректный пароль'
