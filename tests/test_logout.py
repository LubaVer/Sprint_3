from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


personal_acc_button = Locators.personal_acc_button
exit_button = Locators.exit_button
enter_header_in_personal_acc = Locators.enter_header_in_personal_acc
profile_link = Locators.profile_link


class TestLogout:

    def test_logout(self, driver_signin):
        driver_signin.find_element(By.XPATH, personal_acc_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, profile_link)))
        driver_signin.find_element(By.XPATH, exit_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, enter_header_in_personal_acc)))
        assert driver_signin.current_url == 'https://stellarburgers.nomoreparties.site/login'