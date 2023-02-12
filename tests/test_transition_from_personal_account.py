from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoFromPersonalAccount:

    def test_click_logo(self, driver_signin):
        driver_signin.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
        driver_signin.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_builder(self, driver_signin):
        driver_signin.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
        driver_signin.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/'