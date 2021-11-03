from e2e.utils.definition import BasePage
from selenium.webdriver.common.by import By
from e2e.page_factory.page_locator import BuscaPageLocator

class BuscaPage(BasePage):

    def buscar_produto_por_codigo(self, cod_produto):
        self.driver.find_element(By.XPATH, BuscaPageLocator.BUSCA_CAMPO).click()
        self.driver.find_element(By.XPATH, BuscaPageLocator.BUSCA_CAMPO).send_keys(cod_produto)
        self.driver.find_element(By.XPATH, BuscaPageLocator.BUSCA_BOTAO).click()


