import pandas as pd


class Produto:
	def __init__(self, material, preco):
		self.material = material
		self.preco = preco


def get_produtos():
	# conteudo_planilha = pd.read_excel(r"C:\Users\Thais\Downloads\carga_samsung.xlsx")
	conteudo_planilha = pd.read_excel(r"..\utils\carga_planilha.xlsx")
	dados = [Produto(material, format(preco, '.2f').replace(".", "")) for material, preco in zip(conteudo_planilha['MATERIAL'], conteudo_planilha['PREÇO'])]

	return dados
