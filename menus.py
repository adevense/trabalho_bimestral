from gerenciar_participantes import *
from gerenciar_eventos import *
from relatorios import *
import os
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
        print("4. Inscrever Participante em Evento") 
        print("5. Sair") 
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            menu_visualizar()
        elif opcao == '2':
            menu_gerenciar()
        elif opcao == '3':
            menu_relatorios()
        elif opcao == '4': 
            limpar_tela()
            inscrever_participante_evento()
            input("\nPressione Enter para continuar...") 
            limpar_tela()
        elif opcao == '5': 
            carregando()
            print("Saindo do programa...")
            limpar_tela()
            break 
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")
        input("\nPressione Enter para continuar...") 


def menu_gerenciar():
    limpar_tela()
    carregando()
    while True:
        print("\n--- Menu de Gerenciamento ---")
        print("1. Adicionar Evento")
        print("2. Remover Evento")
        print("3. Atualizar Tema de Evento")
        print("4. Adicionar Participante")
        print("5. Remover Participante")
        print("6. Atualizar email de Participante")
        print("7. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            limpar_tela()
            adicionar_evento()
        elif opcao == '2':
            limpar_tela()
            remover_eventos()
        elif opcao == '3':
            limpar_tela()
            atualizar_tema_evento()
        elif opcao == '4':
            limpar_tela()
            adicionar_participante()
        elif opcao == '5':
            limpar_tela()
            remover_participante()
        elif opcao == '6':
            limpar_tela()
            atualizar_email_participante()
        elif opcao == '7':
            limpar_tela()
            break
        input("\nPressione Enter para continuar...")
        limpar_tela() 


def menu_relatorios():
    limpar_tela()
    carregando()
    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Participante Mais Ativo")
        print("2. Temas Mais Frequentes")
        print("3. Taxa Média de Participação por Tema")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            limpar_tela()
            gerar_participante_mais_ativo()
        elif opcao == '2':
            limpar_tela()
            gerar_temas_mais_frequentes()
        elif opcao == '3':
            limpar_tela()
            calcular_taxa_media_participacao_por_tema()
        elif opcao == '4':
            limpar_tela()
            break
        input("\nPressione Enter para continuar...") 
        limpar_tela()

def menu_visualizar():
    limpar_tela()
    while True:
        carregando() 
        print("\n--- Menu de Visualização ---")
        print("1. Buscar Participantes por CPF")
        print("2. Listar Eventos por Participante")
        print("3. Listar Participantes por Evento")
        print("4. Listar Eventos")
        print("5. Agrupar Eventos por Tema")
        print("6. Contar Eventos por Tema")
        print("7. Identificar Eventos com Poucos Participantes")
        print("8. Buscar Eventos por Tema")
        print("9. Buscar Eventos por Faixa de Data")
        print("10. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            limpar_tela()
            buscar_participante_por_cpf()
        elif opcao == '2':
            limpar_tela()
            listar_evento_por_participante()
        elif opcao == '3':
            limpar_tela()
            listar_participantes_por_evento()
        elif opcao == '4':
            limpar_tela()
            listar_eventos()
        elif opcao == '5':
            limpar_tela()
            agrupar_eventos_por_tema()
        elif opcao == '6':
            limpar_tela()
            contar_eventos_por_tema()
        elif opcao == '7':
            limpar_tela()
            identificar_eventos_poucos_participantes()
        elif opcao == '8':
            limpar_tela()
            buscar_eventos_por_tema()
        elif opcao == '9':
            limpar_tela()
            buscar_eventos_por_faixa_data()
        elif opcao == '10':
            limpar_tela()
            break 
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")
        input("\nPressione Enter para continuar...") 
        limpar_tela()

def carregando_omni():
    tempo = random.randint(1, 2) 
    for _ in range(tempo):
        with open('omni_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('omni_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('omni_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()

        with open('omni_pose.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.2) 
        limpar_tela()
        
def carregando_rock():
    tempo = random.randint(1, 2) 
    for _ in range(tempo):
        with open('rock_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('rock_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('rock_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()

        with open('rock_meme.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.2) 
        limpar_tela()
        
def carregando_molusco():
    tempo = random.randint(1, 2) 
    for _ in range(tempo):
        with open('molusco_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('molusco_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('molusco_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()

        with open('molusco_chad.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.2) 
        limpar_tela()
        
def carregando_vegeta():
    tempo = random.randint(1, 2) 
    for _ in range(tempo):
        with open('vegeta_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('vegeta_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('vegeta_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()

        with open('vegeta_calvo.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.2) 
        limpar_tela()
        
def carregando_vergil():
    tempo = random.randint(1, 2) 
    for _ in range(tempo):
        with open('vergil_1.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('vergil_2.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()
        with open('vergil_3.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.3) 
        limpar_tela()

        with open('vergil_cadeira.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
        time.sleep(0.2) 
        limpar_tela()

def carregando():
    escolha = random.randint(1, 5)
    if escolha == 1:
        carregando_omni()
    elif escolha == 2:
        carregando_rock()
    elif escolha == 3:
        carregando_molusco()
    elif escolha == 4:
        carregando_vegeta()
    elif escolha == 5:
        carregando_vergil()