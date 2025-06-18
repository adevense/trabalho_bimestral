from gerenciar_dados import *

def gerar_participante_mais_ativo():
    participantes = importar_dados()

    if not participantes:
        print("Não há participantes cadastrados para gerar o participante mais ativo.")
        return

    participantes_com_eventos = list(filter(lambda p: 'eventos_inscritos' in p and p['eventos_inscritos'], participantes))

    if not participantes_com_eventos:
        print("Nenhum participante encontrado com inscrições em eventos.")
        return

    participante_mais_ativo = max(participantes_com_eventos, key=lambda p: len(p.get('eventos_inscritos', [])))

    nome_participante = participante_mais_ativo.get('nome', 'Nome Desconhecido')
    cpf_participante = participante_mais_ativo.get('cpf', 'CPF Desconhecido')
    num_eventos = len(participante_mais_ativo.get('eventos_inscritos', []))

    print(f"--- Participante Mais Ativo ---")
    print(f"Nome: {nome_participante}")
    print(f"CPF: {cpf_participante}")
    print(f"Número de Eventos Inscritos: {num_eventos}") 

def gerar_temas_mais_frequentes():
    eventos = importar_dados()

    if not eventos:
        print("Não há eventos cadastrados para gerar temas frequentes.")
        return

    contagem_temas = {}

    for evento in eventos:
        if 'tema' in evento:
            tema = evento['tema'].lower()
            contagem_temas[tema] = contagem_temas.get(tema, 0) + 1

    if not contagem_temas:
        print("Nenhum tema encontrado nos eventos cadastrados.")
        return

    print("\n--- Temas de Eventos Mais Frequentes ---")
    temas_ordenados = sorted(contagem_temas.items(), key=lambda item: item[1], reverse=True)

    for tema, contagem in temas_ordenados:
        print(f"Tema: '{tema.capitalize()}', Ocorrências: {contagem}")


def calcular_taxa_media_participacao_por_tema():
    eventos = importar_dados()

    if not eventos:
        print("Não há eventos cadastrados para calcular a taxa de participação.")
        return

    dados_por_tema = {}

    for evento in eventos:
        if 'tema' in evento and 'participantes' in evento:
            tema = evento['tema'].lower()
            num_participantes = len(evento['participantes'])

            if tema not in dados_por_tema:
                dados_por_tema[tema] = {'total_participantes': 0, 'num_eventos': 0}

            dados_por_tema[tema]['total_participantes'] += num_participantes
            dados_por_tema[tema]['num_eventos'] += 1

    if not dados_por_tema:
        print("Nenhum evento com temas e participantes válidos encontrado para o cálculo.")
        return

    print("\n--- Taxa Média de Participação por Tema ---")
    for tema, dados in dados_por_tema.items():
        total_participantes = dados['total_participantes']
        num_eventos = dados['num_eventos']

        if num_eventos > 0:
            media_participacao = total_participantes / num_eventos
            print(f"Tema: '{tema.capitalize()}', Média de Participantes: {media_participacao:.2f}")
        else:
            print(f"Tema: '{tema.capitalize()}', Sem eventos válidos para cálculo de média.")

