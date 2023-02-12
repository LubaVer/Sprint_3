from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestConstructionSection:

    def test_transition_bulki(self, driver_signin):

        element = driver_signin.find_element(By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
        driver_signin.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver_signin, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]")))
        driver_signin.find_element(By.XPATH, "//div[./span[contains(text(),'Булки')]]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))
        assert driver_signin.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]").text == 'Флюоресцентная булка R2-D3'

    def test_transition_bulki(self, driver_signin):

        element = driver_signin.find_element(By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
        driver_signin.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver_signin, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")))
        driver_signin.find_element(By.XPATH, "//div[./span[contains(text(),'Булки')]]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Булки')]")))
        assert driver_signin.find_element(By.XPATH, "//p[contains(text(),'Флюоресцентная булка R2-D3')]").text == 'Флюоресцентная булка R2-D3'

    def test_transition_sous(self, driver_signin):

        element = driver_signin.find_element(By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")
        driver_signin.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(driver_signin, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Сыр с астероидной плесенью')]")))
        driver_signin.find_element(By.XPATH, "//div[./span[contains(text(),'Соусы')]]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Соусы')]")))
        assert driver_signin.find_element(By.XPATH, "//p[contains(text(),'Соус Spicy-X')]").text == 'Соус Spicy-X'

    def test_transition_nachinki(self, driver_signin):

        driver_signin.find_element(By.XPATH, "//div[./span[contains(text(),'Начинки')]]").click()
        WebDriverWait(driver_signin, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Начинки')]")))
        assert driver_signin.find_element(By.XPATH, "//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]").text == 'Мясо бессмертных моллюсков Protostomia'
