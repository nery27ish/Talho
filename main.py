# main.py

import produtos
import clientes
import encomendas
import relatorios

def menu_principal():
    while True:
        print("\n--- Talho do Carlos ---")
        print("1. Gestão de Produtos")
        print("2. Gestão de Clientes")
        print("3. Gestão de Encomendas")
        print("4. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produtos.menu()
        elif opcao == "2":
            clientes.menu()
        elif opcao == "3":
            encomendas.menu()
        elif opcao == "4":
            relatorios.menu()
        elif opcao == "0":
            print("A sair do programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
