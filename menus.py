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

    # Mapeamento das opções para as funções correspondentes
    opcoes_menu_principal = {
        '1': menu_visualizar,
        '2': menu_gerenciar,
        '3': menu_relatorios,
        '4': inscrever_participante_evento,
        '5': lambda: print("Saindo do programa...") or True # Retorna True para sinalizar saída
    }

    while True:
        carregando()
        print("\n--- Menu de Opções ---")
        print("1. Visualizar")
        print("2. Gerenciar")
        print("3. Relatórios")
        print("4. Inscrever Participante em Evento")
        print("5. Sair")
        opcao = input("Escolha uma opção: ").strip()

        acao = opcoes_menu_principal.get(opcao)

        if acao:
            if opcao == '4':
                limpar_tela()
                acao()
                input("\nPressione Enter para continuar...")
                limpar_tela()
            elif opcao == '5':
                carregando()
                acao()
                limpar_tela()
                break
            else:
                acao() # Chama a função mapeada
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

        if opcao != '5': # Para não pedir Enter ao sair
            input("\nPressione Enter para continuar...")
        limpar_tela()


def menu_gerenciar():
    limpar_tela()
    carregando()

    # Mapeamento das opções para as funções correspondentes
    opcoes_menu_gerenciar = {
        '1': adicionar_evento,
        '2': remover_eventos,
        '3': atualizar_tema_evento,
        '4': adicionar_participante,
        '5': remover_participante,
        '6': atualizar_email_participante,
        '7': lambda: True # Retorna True para sinalizar saída do loop
    }

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

        acao = opcoes_menu_gerenciar.get(opcao)

        if acao:
            limpar_tela() # Limpa a tela antes de executar a ação, se for uma ação válida
            if opcao == '7':
                break # Sai do loop se a opção for '7'
            else:
                acao() # Chama a função mapeada
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

        if opcao != '7': # Para não pedir Enter ao voltar ao menu principal
            input("\nPressione Enter para continuar...")
            limpar_tela()


def menu_relatorios():
    limpar_tela()
    carregando()

    # Mapeamento das opções para as funções correspondentes
    opcoes_menu_relatorios = {
        '1': gerar_participante_mais_ativo,
        '2': gerar_temas_mais_frequentes,
        '3': calcular_taxa_media_participacao_por_tema,
        '4': lambda: True # Retorna True para sinalizar saída do loop
    }

    while True:
        print("\n--- Menu de Relatórios ---")
        print("1. Participante Mais Ativo")
        print("2. Temas Mais Frequentes")
        print("3. Taxa Média de Participação por Tema")
        print("4. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ").strip()

        acao = opcoes_menu_relatorios.get(opcao)

        if acao:
            limpar_tela() # Limpa a tela antes de executar a ação, se for uma ação válida
            if opcao == '4':
                break # Sai do loop se a opção for '4'
            else:
                acao() # Chama a função mapeada
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

        if opcao != '4': # Para não pedir Enter ao voltar ao menu principal
            input("\nPressione Enter para continuar...")
            limpar_tela()

def menu_visualizar():
    limpar_tela()
    # Mapeamento das opções para as funções correspondentes
    opcoes_menu_visualizar = {
        '1': buscar_participante_por_cpf,
        '2': listar_evento_por_participante,
        '3': listar_participantes_por_evento,
        '4': listar_eventos,
        '5': agrupar_eventos_por_tema,
        '6': contar_eventos_por_tema,
        '7': identificar_eventos_poucos_participantes,
        '8': buscar_eventos_por_tema,
        '9': buscar_eventos_por_faixa_data,
        '10': lambda: True # Retorna True para sinalizar saída do loop
    }

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

        acao = opcoes_menu_visualizar.get(opcao)

        if acao:
            limpar_tela() # Limpa a tela antes de executar a ação, se for uma ação válida
            if opcao == '10':
                break # Sai do loop se a opção for '10'
            else:
                acao() # Chama a função mapeada
        else:
            print("Opção inválida. Por favor, escolha uma das opções acima.")

        if opcao != '10': # Para não pedir Enter ao voltar ao menu principal
            input("\nPressione Enter para continuar...")
            limpar_tela()

# Funções de carregamento (mantidas como estão, pois já usam o padrão de dicionário)
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
    opcoes = {
        "1": carregando_omni,
        "2": carregando_rock,
        "3": carregando_molusco,
        "4": carregando_vegeta,
        "5": carregando_vergil
    }
    randola = str(random.randint(1, 5))
    adasd = opcoes.get(randola)
    if adasd:
        adasd()