from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:

    def test_logout(self, driver_signin):
        driver_signin.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Профиль')]")))
        driver_signin.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]")))
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/login'