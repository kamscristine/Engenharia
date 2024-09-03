import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (no exemplo, será o Firefox)
        self.driver = webdriver.Firefox()

    def test_login(self):
        self.driver.get("http://the-internet.herokuapp.com/login")

        # Localize os campos de usuário e senha
        usuario = self.driver.find_element(By.ID, "username")
        senha = self.driver.find_element(By.ID, "password")

        # Preencha os campos com as credenciais fornecidas no site
        usuario.send_keys("tomsmith")
        senha.send_keys("SuperSecretPassword!")

        # Envie o formulário
        senha.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )

        msgPósLogin = self.driver.find_element(By.CSS_SELECTOR, ".flash.success")
        self.assertIn("You logged into a secure area!", msgPósLogin.text)

    def tearDown(self):
        # Encerrando o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
