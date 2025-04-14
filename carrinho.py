from produto import *

class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionarItens(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            self.itens.append((produto, quantidade))
            produto.atualizarEstoque(quantidade) 
            return True
        return False

    def total(self):
        return sum(produto.preco * quantidade for produto, quantidade in self.itens)

    def limparCarrinho(self):
        self.itens = []
