# produtos.py

import csv
import os

produtos = []

FICHEIRO_CSV = "produtos.csv"

# Categorias principais e subcategorias
categorias = {
    "Novilho": ["Cachaço", "Acém", "Pá", "Maçã", "Peito", "Chambão", "Mão", "Lombo", "Vazia", "Prego do Peito", "Aba", "Alcatra", "Chã de Fora", "Rabadilha", "Pojadouro"],
    "Porco": ["Chispe", "Perna", "Entremeada", "Entrecosto", "Pá", "Cachaço", "Costeletas do Fundo", "Costeletas do Pé", "Lombo", "Cabeça"],
    "Porco Preto": ["Entrecosto", "Lagartinhos", "Secretos", "Plumas", "Bochechas"],
    "Borrego": ["Cabeça", "Pescoço", "Mão", "Peito", "Costeletas", "Perna"],
    "Aves": ["Frango Inteiro", "Asas", "Pernas", "Peito", "Frango do Campo", "Coelho", "Codornizes", "Peito de Peru", "Pernas de Peru"],
    "Enchidos": ["Chouriço Carne Alentejano", "Chouriço das favas", "Chouriço de Sangue", "Morcela", "Alheira", "Farinheira", "Paio Porco Preto"],
    "Vinhos": ["Tinto", "Branco", "Rose"],
    "Queijos": ["Amanteigado", "Seco de Cabra", "Manteiga"],
    "Outros": ["Ovos", "Mel", "Azeite"]
}

categorias_kg = ["Novilho", "Porco", "Porco Preto", "Borrego", "Aves", "Enchidos"]
categorias_un = ["Vinhos", "Queijos", "Outros"]

def escolher_categoria():
    print("\nCategorias principais:")
    for i, cat in enumerate(categorias.keys(), 1):
        print(f"  {i}. {cat}")
    
    escolha = input("Escolha a categoria principal (número): ")
    try:
        idx = int(escolha) - 1
        lista = list(categorias.keys())
        if 0 <= idx < len(lista):
            return lista[idx]
        else:
            print("Categoria inválida.")
    except ValueError:
        print("Entrada inválida.")
    return None

def escolher_subcategoria(categoria):
    subcats = categorias.get(categoria, [])
    if not subcats:
        return None
    print(f"\nSubcategorias de {categoria}:")
    for i, sub in enumerate(subcats, 1):
        print(f"  {i}. {sub}")
    escolha = input("Escolha a subcategoria (número): ")
    try:
        idx = int(escolha) - 1
        if 0 <= idx < len(subcats):
            return subcats[idx]
        else:
            print("Subcategoria inválida.")
    except ValueError:
        print("Entrada inválida.")
    return None

def adicionar_produto():
    categoria = escolher_categoria()
    if not categoria:
        return

    subcategoria = escolher_subcategoria(categoria)
    if not subcategoria:
        return

    preco = input("Preço (€): ").strip()
    stock = input("Stock (Kg ou Unidades): ").strip()

    try:
        preco = float(preco)
        stock = float(stock)
        unidade = "Kg" if categoria in categorias_kg else "Un"
        produtos.append({
            "categoria": categoria,
            "subcategoria": subcategoria,
            "preco": preco,
            "stock": stock,
            "unidade": unidade
        })
        print(f"Produto '{subcategoria}' [{categoria}] adicionado com {stock:.2f}{unidade} a {preco:.2f}€/{unidade}")
    except ValueError:
        print("Preço ou Stock inválido!")

def listar_produtos():
    if produtos:
        print("\nLista de produtos em stock:")
        for i, p in enumerate(produtos, 1):
            print(f"{i}. [{p['categoria']}] {p['subcategoria']} - {p['preco']:.2f}€/{p['unidade']} | {p['stock']:.2f}{p['unidade']}")
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
            print(f"A editar: {p['subcategoria']} [{p['categoria']}]")
            novo_preco = input(f"Novo preço ({p['preco']}): ").strip()
            novo_stock = input(f"Novo stock ({p['stock']}): ").strip()
            if novo_preco:
                p['preco'] = float(novo_preco)
            if novo_stock:
                p['stock'] = float(novo_stock)
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
            print(f"Produto '{removido['subcategoria']}' removido com sucesso.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def guardar_csv():
    with open(FICHEIRO_CSV, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["categoria", "subcategoria", "preco", "stock", "unidade"])
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
