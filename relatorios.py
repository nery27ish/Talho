import encomendas
import produtos
import csv
import os
from datetime import datetime

# File to save reports
RELATORIOS_CSV = "relatorios.csv"

def faturacao_total():
    total = sum(e["total"] for e in encomendas.encomendas)
    print(f"\nFaturação Total: {total:.2f}€")
    return {"tipo": "Faturação Total", "valor": f"{total:.2f}€"}

def produtos_esgotados():
    esgotados = [p for p in produtos.produtos if p["stock"] == 0]
    result = {"tipo": "Produtos Esgotados", "valor": []}
    if esgotados:
        print("\nProdutos esgotados:")
        for p in esgotados:
            print(f"[{p['categoria']}] {p['subcategoria']}")
            result["valor"].append(f"[{p['categoria']}] {p['subcategoria']}")
    else:
        print("\nNenhum produto esgotado!")
        result["valor"] = ["Nenhum produto esgotado"]
    return result

def vendas_por_produto():
    vendas = {}
    for e in encomendas.encomendas:
        produto = e["produto"]
        if produto not in vendas:
            vendas[produto] = {"quantidade": 0, "total": 0}
        vendas[produto]["quantidade"] += e["quantidade"]
        vendas[produto]["total"] += e["total"]
    
    result = {"tipo": "Vendas por Produto", "valor": []}
    print("\nVendas por Produto:")
    for produto, info in vendas.items():
        print(f"{produto}: {info['quantidade']:.2f} {produtos.produtos[0]['unidade']} | Total: {info['total']:.2f}€")
        result["valor"].append(f"{produto}: {info['quantidade']:.2f} {produtos.produtos[0]['unidade']} | Total: {info['total']:.2f}€")
    if not vendas:
        print("Nenhuma venda registada!")
        result["valor"] = ["Nenhuma venda registada"]
    return result

def vendas_por_cliente():
    vendas = {}
    for e in encomendas.encomendas:
        cliente = e["cliente"]
        if cliente not in vendas:
            vendas[cliente] = {"quantidade": 0, "total": 0}
        vendas[cliente]["quantidade"] += e["quantidade"]
        vendas[cliente]["total"] += e["total"]
    
    result = {"tipo": "Vendas por Cliente", "valor": []}
    print("\nVendas por Cliente:")
    for cliente, info in vendas.items():
        print(f"{cliente}: {info['quantidade']:.2f} {produtos.produtos[0]['unidade']} | Total: {info['total']:.2f}€")
        result["valor"].append(f"{cliente}: {info['quantidade']:.2f} {produtos.produtos[0]['unidade']} | Total: {info['total']:.2f}€")
    if not vendas:
        print("Nenhuma venda registada!")
        result["valor"] = ["Nenhuma venda registada"]
    return result

def stock_baixo(threshold=5.0):
    baixo_stock = [p for p in produtos.produtos if 0 < p["stock"] <= threshold]
    result = {"tipo": "Stock Baixo", "valor": []}
    if baixo_stock:
        print(f"\nProdutos com stock baixo (<= {threshold:.2f}{produtos.produtos[0]['unidade']}):")
        for p in baixo_stock:
            print(f"[{p['categoria']}] {p['subcategoria']}: {p['stock']:.2f}{p['unidade']}")
            result["valor"].append(f"[{p['categoria']}] {p['subcategoria']}: {p['stock']:.2f}{p['unidade']}")
    else:
        print("\nNenhum produto com stock baixo!")
        result["valor"] = ["Nenhum produto com stock baixo"]
    return result

def guardar_relatorios_csv(relatorios_dados):
    with open(RELATORIOS_CSV, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["data", "tipo", "valor"])
        for relatorio in relatorios_dados:
            valor_str = "; ".join(relatorio["valor"]) if isinstance(relatorio["valor"], list) else relatorio["valor"]
            writer.writerow({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "tipo": relatorio["tipo"],
                "valor": valor_str
            })
    print("Relatórios guardados em CSV com sucesso.")

def menu():
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Ver faturação total")
        print("2. Ver produtos esgotados")
        print("3. Ver vendas por produto")
        print("4. Ver vendas por cliente")
        print("5. Ver produtos com stock baixo")
        print("6. Guardar relatórios em CSV")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        relatorios_dados = []
        if opcao == "1":
            relatorios_dados.append(faturacao_total())
        elif opcao == "2":
            relatorios_dados.append(produtos_esgotados())
        elif opcao == "3":
            relatorios_dados.append(vendas_por_produto())
        elif opcao == "4":
            relatorios_dados.append(vendas_por_cliente())
        elif opcao == "5":
            relatorios_dados.append(stock_baixo())
        elif opcao == "6":
            relatorios_dados = [
                faturacao_total(),
                produtos_esgotados(),
                vendas_por_produto(),
                vendas_por_cliente(),
                stock_baixo()
            ]
            guardar_relatorios_csv(relatorios_dados)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()