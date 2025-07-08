# clientes.py

clientes = []

def adicionar_cliente():
    nome = input("Nome do cliente: ").strip()
    if nome:
        clientes.append(nome)
        print(f"Cliente '{nome}' adicionado.")
    else:
        print("Nome inválido.")

def listar_clientes():
    if clientes:
        print("\nLista de clientes:")
        for i, nome in enumerate(clientes, start=1):
            print(f"{i}. {nome}")
    else:
        print("Ainda não há clientes registados.")

def menu():
    while True:
        print("\n--- Menu de Clientes ---")
        print("1. Adicionar cliente")
        print("2. Listar clientes")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_cliente()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    menu()
