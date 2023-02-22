from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


register_button = Locators.register_button
card_cheese = Locators.card_cheese
card_meat = Locators.card_meat
card_bulka = Locators.card_bulka
bulki_header = Locators.bulki_header
card_sous = Locators.card_sous
sous_header = Locators.sous_header
nachinki_header = Locators.nachinki_header
bulki_button = Locators.bulki_button
sous_button = Locators.sous_button
nachinki_button = Locators.nachinki_button



class TestConstructionSection:

    def test_transition_bulki(self, driver_signin):

        element = driver_signin.find_element(By.XPATH, card_cheese)
        driver_signin.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver_signin, 10).until(EC.element_to_be_clickable((By.XPATH, card_cheese)))
        driver_signin.find_element(By.XPATH, bulki_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, bulki_header)))
        assert driver_signin.find_element(By.XPATH, card_bulka).text == 'Флюоресцентная булка R2-D3'

    def test_transition_sous(self, driver_signin):

        element = driver_signin.find_element(By.XPATH, card_cheese)
        driver_signin.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver_signin, 10).until(EC.element_to_be_clickable((By.XPATH, card_cheese)))
        driver_signin.find_element(By.XPATH, sous_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, sous_header)))
        assert driver_signin.find_element(By.XPATH, card_sous).text == 'Соус Spicy-X'

    def test_transition_nachinki(self, driver_signin):

        driver_signin.find_element(By.XPATH, nachinki_button).click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, nachinki_header)))
        assert driver_signin.find_element(By.XPATH, card_meat).text == 'Мясо бессмертных моллюсков Protostomia'
