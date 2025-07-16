# clientes.py

clientes = []

clientes0 = [
    {"nome": "O Marquês", "nif": "", "telefone": "965325870"},
    {"nome": "A Quinta", "nif": "", "telefone": ""},
    {"nome": "Calinas", "nif": "", "telefone": ""},
    {"nome": "Elisabete", "nif": "", "telefone": ""},
    {"nome": "Baleia", "nif": "", "telefone": "918027877"},
]

clientes.extend(clientes0)

def adicionar_cliente():
    nome = input("Nome do cliente: ").strip()
    nif = input("NIF: ").strip()
    telefone = input("Telefone: ").strip()
    
    clientes.append({
        "nome": nome,
        "nif": nif,
        "telefone": telefone
    })
    print(f"Cliente '{nome}' adicionado.")

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
