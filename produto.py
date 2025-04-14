class Produto:
    def __init__(self, idProduto, nome, preco, quantidade):
        self.idProduto = idProduto
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

    def atualizarEstoque(self, quantidadeVendida):
        if self.quantidade >= quantidadeVendida:
            self.quantidade -= quantidadeVendida
        else:
            raise ValueError("Estoque insuficiente")

class Processador(Produto):
    def __init__(self, idProduto, nome, geracao, marca, preco, quantidade):
        super().__init__(idProduto, nome, preco, quantidade)
        self.geracao = geracao
        self.marca = marca

class PlacaVideo(Produto):
    def __init__(self, idProduto, nome, memoria, preco, quantidade):
        super().__init__(idProduto, nome, preco, quantidade)
        self.memoria = memoria

class Cooler(Produto):
    def __init__(self, idProduto, nome, marca, preco, quantidade):
        super().__init__(idProduto, nome, preco, quantidade)
        self.marca = marca

class AirCooler(Cooler):
    def __init__(self, idProduto, nome, marca, preco, quantidade):
        super().__init__(idProduto, nome, marca, preco, quantidade)

class WaterCooler(Cooler):
    def __init__(self, idProduto, nome, marca, preco, quantidade):
        super().__init__(idProduto, nome, marca, preco, quantidade)







