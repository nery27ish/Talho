# produtos.py

produtos = []

def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    preco = input("Preço(€) / Kg: ").strip()
    stock = input("Quantidade em stock (Kg): ").strip()
    
    try:
        preco = float(preco)
        stock = float(stock)
        produtos.append({"nome": nome, "preco": preco, "stock": stock})
        print(f"Produto '{nome}' adicionado com {stock:.2g}kg a {preco:.2f}€/Kg")
    except ValueError:
        print("Preço ou Stock inválido!")

def listar_produtos():
    if produtos:
        print("\nLista de produtos em stock:")
        for i, p in enumerate(produtos, 1):
            print(f"{i}. {p['nome']} - {p['preco']:.2f}€/Kg | {p['stock']:.2f}Kg") 
    else:
        print("Não existem produtos registados!")
        
def menu():
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "0":
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    menu()
