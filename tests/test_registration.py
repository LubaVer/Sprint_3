from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Locators


register_button_link = Locators.register_button_link
personal_acc_button = Locators.personal_acc_button
password_reg = Locators.password_reg
register_button = Locators.register_button
enter_link = Locators.enter_header_in_personal_acc
incorrect_password_hint = Locators.incorrect_password_hint
name_reg = Locators.name_reg
email_reg = Locators.email_reg

faker = Faker()

class TestRegistration:
    def test_registration(self, driver):
        email = faker.email()
        driver.find_element(By.XPATH, personal_acc_button).click()
        driver.find_element(By.XPATH, register_button_link).click()
        driver.find_element(By.XPATH, name_reg).send_keys("Love")
        driver.find_element(By.XPATH, email_reg).send_keys(email)
        driver.find_element(By.XPATH, password_reg).send_keys("123456")
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, enter_link)))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"


    def test_registratio_short_password(self, driver):
        email = faker.email()
        driver.find_element(By.XPATH, personal_acc_button).click()
        driver.find_element(By.XPATH, register_button_link).click()
        driver.find_element(By.XPATH, name_reg).send_keys("Love")
        driver.find_element(By.XPATH, email_reg).send_keys(email)
        driver.find_element(By.XPATH, password_reg).send_keys("1234")
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, incorrect_password_hint)))
        assert driver.find_element(By.XPATH, incorrect_password_hint).text =='Некорректный пароль'
