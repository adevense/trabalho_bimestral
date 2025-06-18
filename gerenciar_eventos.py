from gerenciar_dados import *


def adicionar_evento():
    eventos, participantes = importar_dados() 
    nome = input("Digite o nome do evento: ")
    while True:
        data = input("Digite a data do evento no formato DD/MM/AAAA: ").strip()
        if not verificar_data(data, data_formato="%d/%m/%Y"):
            print("Data inválida. Certifique-se de que o formato está correto (DD/MM/AAAA) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Cadastro cancelado.")
                return
        else:
            break
    
    tema = input("Digite o tema do evento: ")

   
    for evento_existente in eventos:
        if evento_existente['nome'].lower() == nome.lower() and evento_existente['data'] == data:
            print(f"Já existe um evento com o nome '{nome}' na data '{data}'. Cadastro cancelado.")
            return

    if not nome or not tema: 
        print("Nome e tema do evento não podem ser vazios. Cadastro cancelado.")
        return
    
    novo_evento = {
        "nome": nome,
        "data": data,
        "tema": tema,
        "participantes": []
    }
    
    eventos.append(novo_evento)
    salvar_dados(eventos, participantes)
    print(f"Evento '{nome}' adicionado com sucesso!") 
      
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
        if evento['nome'].lower() == nome.lower() and evento['data'] == data: 
            evento_removido = True
            print(f"Evento '{evento['nome']}' na data '{evento['data']}' removido com sucesso.") 
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
    
    evento_encontrado_obj = None
    for evento in eventos:
        if evento['nome'].lower() == nome.lower() and evento['data'] == data: 
            evento_encontrado_obj = evento
            break
    
    if evento_encontrado_obj:
        novo_tema = input("Digite o novo tema do evento: ").strip()
        if novo_tema:
            evento_encontrado_obj['tema'] = novo_tema
            print(f"Tema do evento '{nome}' atualizado para '{novo_tema}'.")
            salvar_dados(eventos, participantes) 
        else:
            print("Tema não pode ser vazio. Atualização cancelada.")
    else: 
        print(f"Evento '{nome}' na data '{data}' não encontrado.")
    
def listar_eventos():
    eventos, _ = importar_dados() 
    if not eventos:
        print("Nenhum evento cadastrado.")
        return
    print("\n--- Lista de Eventos ---") 
    for evento in eventos:
        print(f"Nome: {evento['nome']}, Data: {evento['data']}, Tema: {evento['tema']}, Participantes: {len(evento.get('participantes', []))}") 
    
def agrupar_eventos_por_tema():
    eventos, _ = importar_dados() 
    if not eventos:
        print("Não há eventos cadastrados para agrupar.")
        return

    tema_procurado = input("Digite o tema para agrupar os eventos: ").strip()
    if not tema_procurado:
        print("O tema para agrupar não pode ser vazio.")
        return

    eventos_filtrados = [evento for evento in eventos if 'tema' in evento and evento['tema'].lower() == tema_procurado.lower()] 

    if eventos_filtrados:
        print(f"\n--- Eventos com o tema '{tema_procurado}' ---") 
        for evento_formatado in map(lambda evento: f"Nome: {evento['nome']}, Data: {evento['data']}, Participantes: {len(evento.get('participantes', []))}", eventos_filtrados):
            print(evento_formatado)
    else:
        print(f"Nenhum evento encontrado com o tema '{tema_procurado}'.")
    

def contar_eventos_por_tema():
    eventos, _ = importar_dados() 
    if not eventos: 
        print("Não há eventos cadastrados para contar.")
        return

    tema_procurado = input("Digite o tema para contar os eventos: ").strip()
    if not tema_procurado: 
        print("O tema de busca não pode ser vazio.")
        return
        
    eventos_com_tema = [evento for evento in eventos if 'tema' in evento and evento['tema'].lower() == tema_procurado.lower()] 

    quantidade = len(eventos_com_tema)
    if quantidade > 0:
        print(f"Foi(ram) encontrado(s) {quantidade} evento(s) com o tema '{tema_procurado}'.")
    else:
        print(f"Nenhum evento encontrado com o tema: '{tema_procurado}'.") 

def identificar_eventos_poucos_participantes():
    eventos, _ = importar_dados() 

    if not eventos:
        print("Não há eventos cadastrados.")
        return

    try:
        limite_participantes = int(input("Digite o número máximo de participantes para considerar um evento com 'poucos participantes': ").strip())
        if limite_participantes < 0:
            print("O limite de participantes não pode ser negativo.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o limite.")
        return

    eventos_com_poucos = []
    for evento in eventos:
        num_participantes = len(evento.get('participantes', []))
        if num_participantes < limite_participantes:
            eventos_com_poucos.append(evento)

    if eventos_com_poucos:
        print(f"\n--- Eventos com Menos de {limite_participantes} Participantes ---")
        for evento in eventos_com_poucos:
            print(f"Nome: {evento['nome']}, Data: {evento['data']}, Tema: {evento.get('tema', 'N/A')}, Participantes: {len(evento.get('participantes', []))}")
    else:
        print(f"Nenhum evento encontrado com menos de {limite_participantes} participantes.")

def buscar_eventos_por_tema():
    eventos, _ = importar_dados() 

    if not eventos:
        print("Não há eventos cadastrados para buscar por tema.")
        return

    tema_busca = input("Digite o tema a ser buscado: ").strip()
    if not tema_busca:
        print("O tema de busca não pode ser vazio.")
        return

    eventos_encontrados = [evento for evento in eventos if 'tema' in evento and evento['tema'].lower() == tema_busca.lower()]

    if eventos_encontrados:
        print(f"\n--- Eventos Encontrados com o Tema '{tema_busca}' ---")
        for evento in eventos_encontrados:
            print(f"Nome: {evento['nome']}, Data: {evento['data']}, Tema: {evento.get('tema', 'N/A')}, Participantes: {len(evento.get('participantes', []))}")  
    else:
        print(f"Nenhum evento encontrado com o tema '{tema_busca}'.")


def buscar_eventos_por_faixa_data():
    eventos, _ = importar_dados() 

    if not eventos:
        print("Não há eventos cadastrados para buscar por faixa de data.")
        return

    print("\n--- Buscar Eventos por Faixa de Data ---")
    data_inicio_str = input("Digite a data de início (DD/MM/AAAA): ").strip()
    data_fim_str = input("Digite a data de fim (DD/MM/AAAA): ").strip()

    formato_data = "%d/%m/%Y"

    if not verificar_data(data_inicio_str, data_formato=formato_data):
        print("Data de início inválida. Formato esperado: DD/MM/AAAA.")
        return
    if not verificar_data(data_fim_str, data_formato=formato_data):
        print("Data de fim inválida. Formato esperado: DD/MM/AAAA.")
        return

    data_inicio = datetime.strptime(data_inicio_str, formato_data)
    data_fim = datetime.strptime(data_fim_str, formato_data)

    if data_inicio > data_fim:
        print("A data de início não pode ser posterior à data de fim.")
        return

    eventos_na_faixa = []
    for evento in eventos:
        if 'data' in evento:
            try:
                data_evento = datetime.strptime(evento['data'], formato_data)
                if data_inicio <= data_evento <= data_fim:
                    eventos_na_faixa.append(evento)
            except ValueError:
                continue

    if eventos_na_faixa:
        print(f"\n--- Eventos entre {data_inicio_str} e {data_fim_str} ---")
        for evento in eventos_na_faixa:
            print(f"Nome: {evento['nome']}, Data: {evento['data']}, Tema: {evento.get('tema', 'N/A')}, Participantes: {len(evento.get('participantes', []))}")
    else:
        print(f"Nenhum evento encontrado na faixa de datas de {data_inicio_str} a {data_fim_str}.")

def listar_participantes_por_evento():
    eventos, participantes = importar_dados() 

    print("\n--- Listar Participantes por Evento ---")
    nome_evento = input("Digite o nome do evento: ").strip()
    data_evento = input("Digite a data do evento (DD/MM/AAAA): ").strip()

    if not verificar_data(data_evento, data_formato="%d/%m/%Y"):
        print("Data do evento inválida. Formato esperado: DD/MM/AAAA.")
        return

    evento_encontrado = None
    for evento in eventos:
        if evento['nome'].lower() == nome_evento.lower() and evento['data'] == data_evento:
            evento_encontrado = evento
            break

    if not evento_encontrado:
        print(f"Evento '{nome_evento}' na data '{data_evento}' não encontrado.")
        return

    cpfs_participantes_evento = evento_encontrado.get('participantes', [])

    if cpfs_participantes_evento:
        print(f"\n--- Participantes do Evento '{evento_encontrado['nome']}' em '{evento_encontrado['data']}' ---") 
        for cpf in cpfs_participantes_evento:
            participante_detalhes = next((p for p in participantes if p['cpf'] == cpf), None)
            if participante_detalhes:
                print(f"- Nome: {participante_detalhes.get('nome', 'N/A')}, CPF: {cpf}, Email: {participante_detalhes.get('email', 'N/A')}") 
            else:
                print(f"- CPF: {cpf} (Detalhes do participante não encontrados, pode ter sido removido)") 
    else:
        print(f"O evento '{nome_evento}' na data '{data_evento}' não possui participantes inscritos.")