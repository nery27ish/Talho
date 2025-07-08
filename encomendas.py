# encomendas.py

import produtos

encomendas = []

def registar_encomendas():
    if not produtos.produtos:
        print("Não existem produtos disponíveis para encomenda!")
        return
    
    cliente = input("Nome do cliente: ").strip()
    
    print("\nProdutos disponíveis:")
    for i, p in enumerate(produtos.produtos, 1):
        print(f"{i}. {p['nome']} - {p['preco']:.2f}€/kg | {p['stock']:.2f}kg")
    
    try:
        escolha = int(input("Escolha o nº do produto: "))
        if 1 <= escolha <= len(produtos.produtos):
            produto = produtos.produtos[escolha - 1]
            quantidade = float(input(f"Quantidade (kg) de {produto['nome']}: "))
            
            if quantidade <= 0:
                print("Quantidade inválida!")
                
            if quantidade > produto["stock"]:
                print(f"Stock insuficiente! Só há {produto['stock']:.2f}Kg disponíveis.")
                return
        
            total = quantidade * produto["preco"]
            produto["stock"] -= quantidade
            encomendas.append({
                "cliente": cliente,
                "produto": produto["nome"],
                "quantidade": quantidade,
                "total": total
            })
            
            print(f"Encomenda de {cliente} registada - {quantidade:.2f}Kg de {produto['nome']} ({total:.2f}€)")
            
        else:
            print("Produto inválido!")
            
    except ValueError:
        print("Entrada inválida!")

def listar_encomendas():
    if encomendas:
        print("\nLista de encomendas:")
        for i, e in enumerate(encomendas, 1):
            print(f"{i}. {e['cliente']} - {e['quantidade']:.2f}Kg de {e['produto']} ({e['total']:.2f}€)")
    else:
        print("Não existem encomendas registadas!")

def menu():
    while True:
        print("\n--- Menu de Encomendas ---")
        print("1. Registar encomenda")
        print("2. Listar encomendas")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_encomendas()
        elif opcao == "2":
            listar_encomendas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            
if __name__ == "__main__":
    menu()