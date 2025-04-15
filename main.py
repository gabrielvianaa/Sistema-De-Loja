from loja import *
from carrinho import *
from produto import *

loja = Loja()

processador01 = Processador("01", "I7", "12° Geração", "Intel", 1700.00, 10)
processador02 = Processador("02", "I9", "12° Geração", "Intel", 4500.00, 5)
processador03 = Processador("03", "Ryzen 7 9700X", "9° Geração", "AMD", 2199.00, 5)
processador04 = Processador("04", "Ryzen 9 7900X", "7° Geração", "AMD", 2800.00, 5)

placaVideo01 = PlacaVideo("01", "Placa de Vídeo MSI NVIDIA GeForce - Ventus", "8Gb", 3099.00, 5)
placaVideo02 = PlacaVideo("02", " RTX 4060 Ti Eagle OC Gigabyte NVIDIA GeForce", "8Gb", 3199.99, 10)

airCooler01 = AirCooler("01", "Air Cooler Gamer Rise Mode Storm", "Risemode", 299.00, 3)
airCooler02 = AirCooler("02", "Air Cooler Para Processador Cooler Master Hyper H412R", "Cooler Master", 270.00, 8)

waterCooler01 = WaterCooler("01", "Water Cooler Corsair iCUE LINK TITAN 360 RX", "Corsair", 1399.00, 10)
waterCooler02 = WaterCooler("02", "Water Cooler Rise Mode, ARGB, 240mm", "Risemode", 219.99, 5) 

loja.adicionarProdutoEstoqueProcessador(processador01)
loja.adicionarProdutoEstoqueProcessador(processador02)
loja.adicionarProdutoEstoqueProcessador(processador03)
loja.adicionarProdutoEstoqueProcessador(processador04)

loja.adicionarProdutoEstoquePlacaVideo(placaVideo01)
loja.adicionarProdutoEstoquePlacaVideo(placaVideo02)

loja.adicionarProdutoEstoqueAirCooler(airCooler01)
loja.adicionarProdutoEstoqueAirCooler(airCooler02)

loja.adicionarProdutoEstoqueWaterCooler(waterCooler01)
loja.adicionarProdutoEstoqueWaterCooler(waterCooler02)

def menu():
    while True:
        print("\n----------------- EletroBuy -----------------")
        print("1 - Produtos")
        print("2 - Comprar produto")
        print("3 - Realizar pagamento")
        print("4 - Carrinho")
        print("5 - Sair")
        opcao = input("Digite a alternativa desejada: ")

        if opcao == "1":
            loja.listarProcessadores()
            loja.listarPlacaVideos()
            loja.listarAirCooler()
            loja.listarWaterCooler()
        elif opcao == "2":
            print("\nEscolha a categoria de produto que deseja comprar:")
            print("1 - Processador")
            print("2 - Placa de Vídeo")
            print("3 - Air Cooler")
            print("4 - Water Cooler")
            tipo = input("Digite a alternativa desejada: ")

            if tipo == "1":
                loja.listarProcessadores()
                idProduto = input("Digite o ID do processador: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                produto = loja.encontrarProcessador(idProduto)
            elif tipo == "2":
                loja.listarPlacaVideos()
                idProduto = input("Digite o ID da placa de vídeo: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                produto = loja.encontrarPlacaVideo(idProduto)
            elif tipo == "3":
                loja.listarAirCooler()
                idProduto = input("Digite o ID do air cooler: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                produto = loja.encontrarAirCooler(idProduto)
            elif tipo == "4":
                loja.listarWaterCooler()
                idProduto = input("Digite o ID do water cooler: ")
                quantidade = int(input("Digite a quantidade desejada: "))
                produto = loja.encontrarWaterCooler(idProduto)
            else:
                print("Opção inválida!")
                continue

            if produto:
                if loja.carrinho.adicionarItens(produto, quantidade):
                    print(f"{quantidade} unidade(s) do produto '{produto.nome}' adicionada(s) ao carrinho.")
                else:
                    print("Quantidade insuficiente no estoque.")
            else:
                print("Produto não encontrado.")
        elif opcao == "3":
            loja.pagamento()
            loja.carrinho.limparCarrinho()
        elif opcao == "4":
            if loja.carrinho.itens:
                print("\nItens no carrinho:")
                for produto, quantidade in loja.carrinho.itens:
                    print(f"Produto: {produto.nome} | Quantidade: {quantidade} | Preço unitário: R${produto.preco:.2f}")
                print(f"Total: R${loja.carrinho.total():.2f}")
            else:
                print("\nO carrinho está vazio.")
        elif opcao == "5":
            print("Encerrando sistema...")
            loja.carrinho.limparCarrinho()
            break
        else:
            print("Opção inválida!")

menu()

