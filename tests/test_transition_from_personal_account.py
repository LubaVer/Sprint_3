from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


personal_acc_button = Locators.personal_acc_button
profile_link = Locators.profile_link
constructor_button = Locators.constructor_button


class TestGoFromPersonalAccount:

    def test_click_logo(self, driver_signin):
        driver_signin.find_element(By.XPATH, personal_acc_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, profile_link)))
        driver_signin.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_click_builder(self, driver_signin):
        driver_signin.find_element(By.XPATH, personal_acc_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, profile_link)))
        driver_signin.find_element(By.XPATH, constructor_button).click()
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/'