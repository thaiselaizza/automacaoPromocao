from e2e.utils.definition import BasePage
from selenium.webdriver.common.by import By
from e2e.page_factory.page_locator import DetalhesProdutoPageLocator



class DetalhesProdutoPage(BasePage):

    def procurar_preco_promocional(self):
        preco_encontrado = self.driver.find_element(By.XPATH, DetalhesProdutoPageLocator.PRECO_PROMOCIONAL)
        return preco_encontrado