from carrinho import *
from produto import *

class Loja:
    def __init__(self):
        self.carrinho = Carrinho()
        self.estoque_processadores = []
        self.estoque_placas_video = []
        self.estoque_air_coolers = []
        self.estoque_water_coolers = []

    
    def adicionarProdutoEstoqueProcessador(self, processador):
        self.estoque_processadores.append(processador)

    def adicionarProdutoEstoquePlacaVideo(self, placaVideo):
        self.estoque_placas_video.append(placaVideo)
    
    def adicionarProdutoEstoqueAirCooler(self, airCooler):
        self.estoque_air_coolers.append(airCooler)

    def adicionarProdutoEstoqueWaterCooler(self, waterCooler):
        self.estoque_water_coolers.append(waterCooler)

    def listarProcessadores(self):
        print("\nProcessadores disponíveis:")
        for processador in self.estoque_processadores:
            print(f"ID: {processador.idProduto} | Nome: {processador.nome} | Geração: {processador.geracao} | Marca: {processador.marca} | Preço: R${processador.preco} | Quantidade: {processador.quantidade}")

    def listarPlacaVideos(self):
        print("\nPlaca de vídeo disponíveis:")
        for placa in self.estoque_placas_video:
            print(f"ID: {placa.idProduto} | Nome: {placa.nome} | Memória: {placa.memoria} | Preço: R${placa.preco} | Quantidade: {placa.quantidade}")
    
    def listarAirCooler(self):
        print("\nAir Cooler disponíveis:")
        for air_cooler in self.estoque_air_coolers:
            print(f"ID: {air_cooler.idProduto} | Nome: {air_cooler.nome} | Marca: {air_cooler.marca} | Preço R${air_cooler.preco} | Quantidade: {air_cooler.quantidade}")
    
    def listarWaterCooler(self):
        print("\nWater Cooler disponíveis:")
        for water_cooler in self.estoque_water_coolers:
            print(f"ID: {water_cooler.idProduto} | Nome: {water_cooler.nome} | Marca: {water_cooler.marca} | Preço: R${water_cooler.preco} | Quantidade: {water_cooler.quantidade}")
    
    def encontrarProcessador(self, idProduto):
        for processador in self.estoque_processadores:
            if processador.idProduto == idProduto:
                return processador
        return None

    def encontrarPlacaVideo(self, idProduto):
        for placa in self.estoque_placas_video:
            if placa.idProduto == idProduto:
                return placa
        return None

    def encontrarAirCooler(self, idProduto):
        for air_cooler in self.estoque_air_coolers:
            if air_cooler.idProduto == idProduto:
                return air_cooler
        return None

    def encontrarWaterCooler(self, idProduto):
        for water_cooler in self.estoque_water_coolers:
            if water_cooler.idProduto == idProduto:
                return water_cooler
        return None

    def pagamento(self):
        total = self.carrinho.total()
        print(f"\nTotal da compra: R$ {total:.2f}")
        print("Forma de pagamento:")
        print("1 - À vista (5% de desconto)")
        print("2 - Pix (5% de desconto)")
        print("3 - Cartão de débito")
        print("4 - Cartão de crédito:\n1x: sem juros\n2x: sem juros\n3x: 3.78% de juros\n4x: 5.69% de juros\n5x: 7.25% de juros")
        opcao = input("Escolha a forma de pagamento: ")

        if opcao == "1":
            total *= 0.95
        elif opcao == "2":
            total *= 0.95
        elif opcao == "3":
            print(f"Valor final: R$ {total:.2f}")
        elif opcao == "4":
            parcelas = int(input("Número de parcelas: "))
            if parcelas == 1 or parcelas == 2:
                print(f"Valor final: R$ {total:.2f}")
            elif parcelas == 3:
                total *= 1.0378  
            elif parcelas == 4:
                total *= 1.0569  
            elif parcelas == 5:
                total *= 1.0725  
            else:
                print("Número de parcelas inválido.")
                return
        else:
            print("Opção de pagamento inválida.")
            return

        print(f"Valor final: R$ {total:.2f}")


