from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoToPersonalAccount:

    def test_go_to_personal_account_without_login(self, driver): #тест без входа в аккаунт
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_go_to_personal_account_with_login(self, driver_signin):
        driver_signin.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'