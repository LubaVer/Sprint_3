from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


register_button_link = Locators.register_button_link
personal_acc_button = Locators.personal_acc_button
password_reg = Locators.password_reg
enter_button = Locators.enter_button
enter_acc_button = Locators.enter_acc_button
place_order_button = Locators.place_order_button
email_reg = Locators.email_reg
enter_link = Locators.enter_link
restore_password_link = Locators.restore_password_link

class TestSignin():

    def helper_signin_action(self, web_driver):
        web_driver.find_element(By.XPATH, email_reg).send_keys("love666@gmail.com")
        web_driver.find_element(By.XPATH, password_reg).send_keys("123456")
        web_driver.find_element(By.XPATH, enter_button).click()

    def test_signin_from_main(self, driver):
        driver.find_element(By.XPATH, enter_acc_button).click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, place_order_button)))
        button = driver.find_element(By.XPATH, place_order_button).text
        assert button == "Оформить заказ"

    def test_signin_from_personal_account(self, driver):
        driver.find_element(By.XPATH, personal_acc_button).click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, place_order_button)))
        button = driver.find_element(By.XPATH, place_order_button).text
        assert button == "Оформить заказ"

    def test_signin_from_registration_form(self, driver):
        driver.find_element(By.XPATH, personal_acc_button).click()
        driver.find_element(By.XPATH, register_button_link).click()
        driver.find_element(By.XPATH, enter_link).click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, place_order_button)))
        button = driver.find_element(By.XPATH, place_order_button).text
        assert button == "Оформить заказ"

    def test_signin_from_password_recovery(self, driver):
        driver.find_element(By.XPATH, enter_acc_button).click()
        driver.find_element(By.XPATH, restore_password_link).click()
        driver.find_element(By.XPATH, enter_link).click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, place_order_button)))
        button = driver.find_element(By.XPATH, place_order_button).text
        assert button == "Оформить заказ"

