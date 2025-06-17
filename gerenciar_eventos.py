from gerenciar_dados import *


def adicionar_evento():

    eventos,participantes = importar_dados()
    nome = input("Digite o nome do eveto: ")
    while True:
        data = input("Digite a data do evento no formato DD/MM/AAAA: ").strip()
        if verificar_data(data, data_formato="%d/%m/%Y") == False:
            print("Data inválida. Certifique-se de que o formato está correto (DD/MM/AAAA) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Cadastro cancelado.")
                return
        else:
            break
    tema = input("Digite o tema do evento: ")
    if nome == '' or tema == '':
        print("Nome e tema do evento não podem ser vazios. Cadastro cancelado.")
        return
    novo_evento = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }
    
    eventos.append(novo_evento)
    salvar_dados(eventos,participantes)
     
def remover_eventos():
    eventos, participantes = importar_dados()
    nome = input("Digite o nome do evento a ser excluído: ").strip()
    data = input("Digite a data do evento no formato DD/MM/AAAA: ").strip()

    if not verificar_data(data, data_formato="%d/%m/%Y"):
        print("Data inválida. Certifique-se de que o formato está correto (DD/MM/AAAA) e tente novamente.")
        return

    evento_removido = False
    novos_eventos = []

    for evento in eventos:
        if evento['nome'] == nome and evento['data'] == data:
            evento_removido = True
            print(f"Evento '{nome}' na data '{data}' removido com sucesso.")
        else:
            novos_eventos.append(evento)

    if evento_removido:
        salvar_dados(novos_eventos, participantes)
    else:
        print(f"Evento '{nome}' na data '{data}' não encontrado.")


def atualizar_tema_evento():
    eventos, participantes = importar_dados()
    nome = input("Digite o nome do evento a ter o tema atualizado: ").strip()
    data = input("Digite a data do evento no formato DD/MM/AAAA: ").strip()

    if not verificar_data(data, data_formato="%d/%m/%Y"):
        print("Data inválida. Certifique-se de que o formato está correto (DD/MM/AAAA) e tente novamente.")
        return
    evento_encontrado = False

    for evento in eventos:
        if evento['nome'] == nome and evento['data'] == data:
            evento_encontrado = True
            novo_tema = input("Digite o novo tema do evento: ").strip()
            if novo_tema:
                evento['tema'] = novo_tema
                print(f"Tema do evento '{nome}' atualizado para '{novo_tema}'.")
            else:
                print("Tema não pode ser vazio. Atualização cancelada.")
            break
    salvar_dados(eventos, participantes)
    

def listar_eventos():
    eventos = importar_dados()
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    print("Lista de Eventos:")
    for evento in eventos:
        print(f"Nome: {evento['nome']}, Data: {evento['data']}, Tema: {evento['tema']}, Participantes: {len(evento['participantes'])}")
    


def agrupar_eventos_por_tema():
    eventos = importar_dados()
    tema_procurado = input("Digite o tema para agrupar os eventos: ").strip()
    eventos_filtrados = list(filter(lambda evento: evento['tema'].lower() == tema_procurado.lower(), eventos))
    if eventos_filtrados:
        print(f"Eventos com o tema '{tema_procurado}':")
        for evento_formatado in map(lambda evento: f"Nome: {evento['nome']}, Data: {evento['data']}, Participantes: {len(evento['participantes'])}", eventos_filtrados):
            print(evento_formatado)
    else:
        print(f"Nenhum evento encontrado com o tema '{tema_procurado}'.")
    
agrupar_eventos_por_tema()

def contar_eventos_por_tema():
    pass

def identificar_eventos_poucos_participantes():
    pass

def buscar_eventos_por_tema():
    pass

def buscar_eventos_por_faixa_data():
    pass

def listar_participantes_por_evento():
    pass