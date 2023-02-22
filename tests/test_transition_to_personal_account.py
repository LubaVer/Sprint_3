from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


personal_acc_button = Locators.personal_acc_button
enter_header_in_personal_acc = Locators.enter_header_in_personal_acc
profile_link = Locators.profile_link

class TestGoToPersonalAccount:

    def test_go_to_personal_account_without_login(self, driver):
        driver.find_element(By.XPATH, personal_acc_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, enter_header_in_personal_acc)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_go_to_personal_account_with_login(self, driver_signin):
        driver_signin.find_element(By.XPATH, personal_acc_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, profile_link)))
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
