from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSignin():

    def helper_signin_action(self, web_driver):
        web_driver.find_element(By.XPATH, "//fieldset[1]/div[1]/div[1]/input[1]").send_keys("love666@gmail.com")
        web_driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")
        web_driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

    def test_signin_from_main(self, driver): #вход по кнопке "Войти в аккаунт" на главной
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text
        assert button == "Оформить заказ"

    def test_signin_from_personal_account(self, driver): #вход через кнопку «Личный кабинет»
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text
        assert button == "Оформить заказ"

    def test_signin_from_registration_form(self, driver): #вход через кнопку в регистрации
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text
        assert button == "Оформить заказ"

    def test_signin_from_password_recovery(self, driver): #вход через кнопку в форме восстановления пароля
        driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()
        self.helper_signin_action(driver)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))
        button = driver.find_element(By.XPATH, "//button[contains(text(),'Оформить заказ')]").text
        assert button == "Оформить заказ"

