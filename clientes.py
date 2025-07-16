# clientes.py

import csv
import os

FICHEIRO_CSV = "clientes.csv"
clientes = []

def carregar_clientes_csv():
    if os.path.exists(FICHEIRO_CSV):
        with open(FICHEIRO_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    else:
        clientes0 = [
            {"nome": "O Marquês", "nif": "", "telefone": "965325870"},
            {"nome": "A Quinta", "nif": "", "telefone": ""},
            {"nome": "Calinas", "nif": "", "telefone": ""},
            {"nome": "Elisabete", "nif": "122034481", "telefone": ""},
            {"nome": "Baleia", "nif": "", "telefone": "918027877"},
        ]
        guardar_clientes_csv(clientes0)
        return clientes0

def guardar_clientes_csv(lista_clientes=None):
    if lista_clientes is None:
        lista_clientes = clientes
    with open(FICHEIRO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "nif", "telefone"])
        writer.writeheader()
        writer.writerows(lista_clientes)

clientes = carregar_clientes_csv()

def adicionar_cliente():
    nome = input("Nome do cliente: ").strip()
    nif = input("NIF: ").strip()
    telefone = input("Telefone: ").strip()
    
    novo_cliente = {
        "nome": nome,
        "nif": nif,
        "telefone": telefone
    }
    clientes.append(novo_cliente)
    guardar_clientes_csv()
    print(f"Cliente '{nome}' adicionado.")

def listar_clientes():
    if clientes:
        print("\nLista de clientes:")
        for i, c in enumerate(clientes, 1):
            print(f"{i}. {c['nome']} | NIF: {c['nif']} | Tel: {c['telefone']}")
    else:
        print("Não existem clientes registados!")

def alterar_cliente():
    listar_clientes()
    try:
        idx = int(input("Número do cliente a alterar: ")) - 1
        if 0 <= idx < len(clientes):
            print("Deixa vazio se não quiseres alterar o campo.")
            nome = input(f"Novo nome ({clientes[idx]['nome']}): ").strip()
            nif = input(f"Novo NIF ({clientes[idx]['nif']}): ").strip()
            telefone = input(f"Novo telefone ({clientes[idx]['telefone']}): ").strip()

            if nome:
                clientes[idx]['nome'] = nome
            if nif:
                clientes[idx]['nif'] = nif
            if telefone:
                clientes[idx]['telefone'] = telefone

            guardar_clientes_csv()
            print("Cliente alterado com sucesso.")
        else:
            print("Cliente inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_cliente():
    listar_clientes()
    try:
        idx = int(input("Número do cliente a remover: ")) - 1
        if 0 <= idx < len(clientes):
            removido = clientes.pop(idx)
            guardar_clientes_csv()
            print(f"Cliente '{removido['nome']}' removido com sucesso.")
        else:
            print("Cliente inválido.")
    except ValueError:
        print("Entrada inválida.")
        
def menu():
    while True:
        print("\n--- Menu de Clientes ---")
        print("1. Adicionar cliente")
        print("2. Listar clientes")
        print("3. Alterar cliente")
        print("4. Remover cliente")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_cliente()
        elif escolha == "2":
            listar_clientes()
        elif escolha == "3":
            alterar_cliente()
        elif escolha == "4":
            remover_cliente()
        elif escolha == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    menu()
