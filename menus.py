from gerenciar_participantes import *
import  os
import time
import random

def limpar_tela():
    if os.name == 'nt': 
        _ = os.system('cls')
    else: 
        _ = os.system('clear')

def menu_principal():
    limpar_tela()

    while True:
        carregando()
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
            carregando()
            print("Saindo do programa...")
            limpar_tela()
            break 
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

def menu_participantes():
    limpar_tela()
    carregando()
    print("\n--- Menu de Gerenciamento de Participantes (Em construção) ---")
    input("Pressione Enter para voltar ao menu principal...") 

def menu_relatorios():
    limpar_tela()
    carregando()
    print("\n--- Menu de Relatórios (Em construção) ---")
    input("Pressione Enter para voltar ao menu principal...") 

def menu_visualizar():
    limpar_tela()
    while True:
        carregando() 
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

def carregando_omni():
    tempo = random.randint(1, 3)
    for _  in range(tempo):
        with open('omni_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('omni_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('omni_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()

        with open('omni_pose.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3)
        limpar_tela()
        
def carregando_rock():
    tempo = random.randint(1, 3)
    for _  in range(tempo):
        with open('rock_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('rock_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('rock_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()

        with open('rock_meme.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3)
        limpar_tela()
        
def carregando_molusco():
    tempo = random.randint(1, 3)
    for _  in range(tempo):
        with open('molusco_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('molusco_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()
        with open('molusco_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.5)
        limpar_tela()

        with open('molusco_chad.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3)
        limpar_tela()

def carregando():
    escolha = random.randint(1, 3)
    if escolha == 1:
        carregando_omni()
    elif  escolha  == 2:
        carregando_rock()
    elif escolha == 3:
        carregando_molusco()