# relatorios.py

import encomendas
import produtos

def faturacao_total():
    total = sum(e["total"] for e in encomendas.encomendas)
    print(f"\n Faturação Total: {total:.2f}€")
    
def produtos_esgotados():
    esgotados = [p for p in produtos.produtos if p["stock"] == 0]
    if esgotados:
        print("\nProdutos esgotados:")
        for p in esgotados:
            print(f"{p['nome']}")
    else:
        print("\nNenhum produto esgotado!")

def menu():
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Ver faturação total")
        print("2. Ver produtos esgotados")
        print("0. Voltar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            faturacao_total()
        elif opcao == "2":
            produtos_esgotados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()