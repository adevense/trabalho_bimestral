from gerenciar_participantes import *
import  os

def limpar_tela():
    if os.name == 'nt': 
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

def menu_principal():
    limpar_tela()
    while True:
        print("\n--- Menu de Opções ---")
        print("1. Visualizar")
        print("2. Gerenciar")
        print("3. Relatórios")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            menu_visualizar()
        elif opcao == '2':
            menu_participantes()
        elif opcao == '3':
            menu_relatorios()
        elif opcao == '4':
            print("Saindo do programa...")
            break 
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

def menu_participantes():
    limpar_tela()
    print("\n--- Menu de Gerenciamento de Participantes (Em construção) ---")
    input("Pressione Enter para voltar ao menu principal...") 

def menu_relatorios():
    limpar_tela()
    print("\n--- Menu de Relatórios (Em construção) ---")
    input("Pressione Enter para voltar ao menu principal...") 

def menu_visualizar():
    limpar_tela()
    while True: 
        print("\n--- Menu de Visualização ---")
        print("1. Buscar Participantes por CPF")
        print("2. (Opção Vazia)") 
        print("3. (Opção Vazia)")
        print("4. (Opção Vazia)")
        print("5. (Opção Vazia)")
        print("6. (Opção Vazia)")
        print("7. (Opção Vazia)")
        print("8. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            buscar_participante_por_cpf()
        elif opcao == '2':
            pass
        elif opcao == '3':
            pass
        elif opcao == '4':
            pass
        elif opcao == '5':
            pass
        elif opcao == '6':
            pass
        elif opcao == '7':
            pass
        elif opcao == '8':
            break 
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")
