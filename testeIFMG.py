import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TesteMenu(unittest.TestCase):
    def setUp(self):
        # Configurando o navegador (usando Chrome)
        self.driver = webdriver.Chrome()

    def testeBusca(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        busca = self.driver.find_element(By.ID, "nolivesearchGadget")
        busca.send_keys("processo seletivo")
        busca.submit()
        print(self.driver.title)
        WebDriverWait(self.driver, 10).until(EC.title_contains("Busca — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará"))
        self.assertIn("Busca — Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais Campus Sabará", self.driver.title)

    def testeMenuMeuIfmg(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "Meu IFMG")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("RM Portal"))
        self.assertIn("RM Portal", self.driver.title)

    def testeMenuCPA(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "CPA")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("Comissão Própria de Avaliação"))
        self.assertIn("Comissão Própria de Avaliação", self.driver.title)

    def testeMenuWebmail(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "Webmail")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("Gmail"))
        self.assertIn("Gmail", self.driver.title)

    def testeMenuContato(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "Contato")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("Contato"))
        self.assertIn("Contato", self.driver.title)
    
    def testeMenuExAlunos(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "Ex-Alunos")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("Formulário Contato Ex alunos"))
        self.assertIn("Formulário Contato Ex alunos", self.driver.title)

    def testeMenuAcesso(self):
        self.driver.get("https://www.ifmg.edu.br/sabara")

        # Verificando o link "Meu IFMG"
        meu_ifmg_link = self.driver.find_element(By.LINK_TEXT, "Acesso a Sistemas")
        meu_ifmg_link.click()
        print(self.driver.title)
        # Verificando se o título corresponde ao esperado
        WebDriverWait(self.driver, 10).until(EC.title_contains("Acesso a Sistemas"))
        self.assertIn("Acesso a Sistemas", self.driver.title)

    def tearDown(self):
        # Encerrando o navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
