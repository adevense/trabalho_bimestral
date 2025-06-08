
def menu_principal():
    print("Menu de Opções:")
    print("1. Gerenciar eventos")
    print("2. Gerenciar participantes")
    print("3. Gerenciar relatórios")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        menu_eventos()
    elif opcao == '2':
        menu_participantes()
    elif opcao == '3':
        menu_relatorios()
    elif opcao == '4':
        print("Saindo do programa...")
        exit()
    
def menu_participantes():
    pass
def  menu_relatorios():
    pass


def menu_eventos():
    print("Menu de Visualização:")
    print("1. Ver todos os eventos cadastrados")
    print("2. Cadastrar novo evento")
    print("3. Editar detalhes de evento")
    print("4. Listar participantes por evento")
    print("5.")
    print("6.")
    print("7.")
    print("8. Voltar ao menu principal")