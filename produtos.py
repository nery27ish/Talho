# produtos.py

import csv
import os

produtos = []

categorias_kg = ["Novilho", "Porco", "Porco Preto", "Borrego", "Aves", "Enchidos"]
categorias_un = ["Vinhos", "Queijos", "Outros"]

FICHEIRO_CSV = "produtos.csv"

def escolher_categoria():
    print("\nCategorias disponíveis:")
    print("Stock em Kg:")
    for i, cat in enumerate(categorias_kg, 1):
        print(f"  {i}. {cat}")
    print("Stock em Unidades:")
    for i, cat in enumerate(categorias_un, 1):
        print(f"  {i+len(categorias_kg)}. {cat}")
    
    todas = categorias_kg + categorias_un
    escolha = input("Escolha a categoria (número): ")
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(todas):
            return todas[idx]
        else:
            print("Categoria inválida.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None
    
def adicionar_produto():
    categoria = escolher_categoria()
    if not categoria:
        return
    
    nome = input("Nome do produto: ").strip()
    preco = input("Preço (€): ").strip()
    stock = input("Stock (Kg ou Unidades): ").strip()
    
    try:
        preco = float(preco)
        stock = float(stock)
        unidade = "Kg" if categoria in categorias_kg else "Un"
        produtos.append({
            "categoria": categoria,
            "nome": nome,
            "preco": preco,
            "stock": stock,
            "unidade": unidade
        })
        print(f"Produto '{nome}' adicionado à categoria '{categoria}' com {stock:.2f}{unidade} a {preco:.2f}€/ {unidade}")
    except ValueError:
        print("Preço ou Stock inválido!")

def listar_produtos():
    if produtos:
        print("\nLista de produtos em stock:")
        for i, p in enumerate(produtos, 1):
            print(f"{i}. [{p['categoria']}] {p['nome']} - {p['preco']:.2f}€/ {p['unidade']} | {p['stock']:.2f}{p['unidade']}") 
    else:
        print("Não existem produtos registados!")
 
def editar_produto():
    listar_produtos()
    if not produtos:
        return

    try:
        idx = int(input("Número do produto a editar: ")) - 1
        if 0 <= idx < len(produtos):
            p = produtos[idx]
            print(f"A editar: {p['nome']} [{p['categoria']}]")
            novo_nome = input(f"Novo nome ({p['nome']}): ").strip() or p['nome']
            novo_preco = input(f"Novo preço ({p['preco']}): ").strip()
            novo_stock = input(f"Novo stock ({p['stock']}): ").strip()
            
            if novo_preco:
                p['preco'] = float(novo_preco)
            if novo_stock:
                p['stock'] = float(novo_stock)
            p['nome'] = novo_nome
            print("Produto atualizado com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_produto():
    listar_produtos()
    if not produtos:
        return

    try:
        idx = int(input("Número do produto a remover: ")) - 1
        if 0 <= idx < len(produtos):
            removido = produtos.pop(idx)
            print(f"Produto '{removido['nome']}' removido com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")
        
def guardar_csv():
    with open(FICHEIRO_CSV, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["categoria", "nome", "preco", "stock", "unidade"])
        writer.writeheader()
        writer.writerows(produtos)
    print("Produtos guardados em CSV com sucesso.")
    
def carregar_csv():
    if not os.path.exists(FICHEIRO_CSV):
        return

    with open(FICHEIRO_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["preco"] = float(row["preco"])
                row["stock"] = float(row["stock"])
                produtos.append(row)
            except ValueError:
                continue 
        
def menu():
    carregar_csv()
    while True:
        print("\n--- Menu de Produtos ---")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Editar produto")
        print("4. Remover produto")
        print("5. Guardar em CSV")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            guardar_csv()
        elif opcao == "0":
            guardar_csv()
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    menu()
