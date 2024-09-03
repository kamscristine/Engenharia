import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (no exemplo, será o Firefox)
        self.driver = webdriver.Firefox()

    def test_google_search_for_software(self):
        self.driver.get("https://www.google.com")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]")))
        botaoClick = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]")
        botaoClick.click()
        WebDriverWait(self.driver, 10).until(EC.title_contains("Doodles"))
        time.sleep(5)
        self.assertIn("doodles", self.driver.title.lower())

    def tearDown(self):
        # Encerrando o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 

