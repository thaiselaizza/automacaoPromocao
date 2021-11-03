from selenium import webdriver

from e2e.page_object.buscar_produto_page import BuscaPage
from e2e.page_object.detalhes_produto_page import DetalhesProdutoPage
from e2e.utils.planilha_produtos import Produto, get_produtos
import unittest
import time



class ValidarPrecoPromocional(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../driver/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://www.bemol.com.br/")
        self.driver.implicitly_wait(30)

    def test_buscar_produto_e_validar_preco(self):
        busca_page = BuscaPage(self.driver)
        detalhes_page = DetalhesProdutoPage(self.driver)
        produtos = get_produtos()


        for produto in produtos:
           busca_page.buscar_produto_por_codigo(produto.material)
           time.sleep(3)
           preco_aux = detalhes_page.procurar_preco_promocional().text.replace(".","").replace(",", "")
           p_promocional = preco_aux.replace("R$ ", "")
           self.assertEqual(produto.preco, p_promocional)








