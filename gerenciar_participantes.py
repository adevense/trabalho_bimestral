from gerenciar_dados import *
from validate_docbr import CPF
from datetime import datetime

def adicionar_participante():
    eventos, participantes = importar_dados() 
    nome = input("Digite o nome do participante: ")
    while True:
        cpf = input("Digite o CPF do participante no formato XXX.XXX.XXX-XX: ").strip()
        cpf_validador = CPF() 
        if cpf_validador.validate(cpf):
            if cpf in [p['cpf'] for p in participantes]:
                print("Participante já cadastrado com este CPF.")
                continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
                if continuar == 's' or continuar == 'sim':
                    print('')
                else:
                    return print("Cadastro cancelado.")
            else:
                break
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar != 's' and continuar != 'sim':
                print("Cadastro cancelado.")
                return

    while True:
        email = input("Digite o email do participante: ").lower().strip()
        if email != '' and '@' in email and '.' in email and email[0] != '@' and email[0] != '.' and " " not in email and '"' not in email and ',' not in email and '(' not in email and ')' not in email:
            if email in [p['email'] for p in participantes if 'email' in p]: 
                print("Participante já cadastrado com este email.")
                continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
                if continuar == 's' or continuar == 'sim':
                    print('')
                else:
                    print("Cadastro cancelado.")
                    return
            else:
                break
        else:
            print("Email inválido. Certifique-se de que o formato está correto e tente novamente.")
    if nome == '' or cpf == '' or email == '': 
        print("Nome, CPF e/ou email do participante não podem ser vazios. Cadastro cancelado.")
        return
    novo_participante = {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "preferencias_tematicas":[] 
    }
    
    participantes.append(novo_participante)
    salvar_dados(eventos,participantes)
    print(f"Participante '{nome}' (CPF: {cpf}) adicionado com sucesso!") 

def remover_participante():
    eventos, participantes = importar_dados() 
    while True:
        cpf_remover = input("Digite o CPF do participante a ser removido no formato XXX.XXX.XXX-XX: ").strip()
        cpf_validador = CPF() 
        if cpf_validador.validate(cpf_remover):
            break
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Remoção cancelada.")
                return
            
    participante_encontrado = False
    novos_participantes = []
    participante_nome = ""

    for participante in participantes:
        if participante['cpf'] == cpf_remover: 
            participante_encontrado = True
            participante_nome = participante['nome']
        else:
            novos_participantes.append(participante)
    
    if participante_encontrado:
        
        for evento in eventos:
            if 'participantes' in evento and cpf_remover in evento['participantes']:
                evento['participantes'].remove(cpf_remover)
                print(f"Participante '{participante_nome}' removido do evento '{evento['nome']}'.") 
        
        salvar_dados(eventos, novos_participantes) 
        print(f"Participante '{participante_nome}' (CPF: {cpf_remover}) removido com sucesso do sistema.")
    else:
        print("Participante não encontrado.")


def atualizar_email_participante():
    eventos, participantes = importar_dados() 
    participante_encontrado = None
    while True:
        cpf = input("Digite o CPF do participante a ter seu email atualizado no formato XXX.XXX.XXX-XX: ").strip()
        cpf_validador = CPF() 
        if cpf_validador.validate(cpf):
            for p_dict in participantes:
                if p_dict['cpf'] == cpf:
                    participante_encontrado = p_dict
                    break
            if participante_encontrado is None:
                print("Participante não encontrado com este CPF.")
                continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
                if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                    print("Atualização cancelada.")
                    return
            else:
                print(f"Participante encontrado: {participante_encontrado['nome']}.")
                print(f"Email atual: {participante_encontrado.get('email', 'N/A')}")
                break
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Atualização cancelada.")
                return
    while True:
        email = input("Digite o novo email do participante: ").strip().lower()
        if email != '' and '@' in email and '.' in email and email[0] != '@' and email[0] != '.' and " " not in email and '"' not in email and ',' not in email and '(' not in email and ')' not in email:
            email_ja_em_uso = False
            for p_in_list in participantes:
                if 'email' in p_in_list and 'cpf' in p_in_list:
                    if p_in_list['email'] == email and p_in_list['cpf'] != participante_encontrado['cpf']:
                        email_ja_em_uso = True
                        break
            if email_ja_em_uso:
                print("Já existe outro participante cadastrado com este email.")
                continuar_email_input = input("Deseja tentar novamente o email? (s/n): ").lower().strip()
                if continuar_email_input == 's' or continuar_email_input == 'sim':
                    print('')
                else:
                    print("Atualização de email cancelada. O email original foi mantido.")
                    return
            else:
                participante_encontrado['email'] = email
                print("Email do participante atualizado com sucesso.")
                salvar_dados(eventos, participantes)
                break
        else:
            print("Formato de e-mail inválido. Por favor, digite um e-mail válido.")

def buscar_participante_por_cpf():
    eventos, participantes = importar_dados() 
    
    while True:
        cpf = input("Digite o CPF do participante no formato XXX.XXX.XXX-XX: ").strip()
        cpf_validador = CPF() 
        if cpf_validador.validate(cpf):
            participante_encontrado = None
            for p in participantes:
                if p['cpf'] == cpf:
                    participante_encontrado = p
                    break
            if participante_encontrado:
                print(f"\n--- Detalhes do Participante ---") 
                print(f"Nome: {participante_encontrado['nome']}.")
                print(f"CPF: {participante_encontrado['cpf']}.") 
                print(f"Email: {participante_encontrado['email']}.")
                preferencias = participante_encontrado.get('preferencias_tematicas', []) 
                if preferencias:
                    print(f"Preferências temáticas: {', '.join(preferencias)}")
                else:
                    print("Preferências temáticas: Nenhuma informada.")
                return 
            else:
                print("Participante não encontrado com este CPF.")
                continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
                if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                    print("Busca cancelada.")
                    return
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Busca cancelada.")
                return


def inscrever_participante_evento():
    eventos, participantes = importar_dados()
    cpf_validator = CPF()

    print("\n--- Inscrever Participante em Evento ---")
    nome_evento = input("Digite o nome do evento: ").strip()
    data_evento = input("Digite a data do evento (DD/MM/AAAA): ").strip()
    
    while True:
        cpf_participante_input = input("Digite o CPF do participante (apenas números ou no formato XXX.XXX.XXX-XX): ").strip()
        
        if len(cpf_participante_input) == 11 and cpf_participante_input.isdigit():
            cpf_formatado = f"{cpf_participante_input[:3]}.{cpf_participante_input[3:6]}.{cpf_participante_input[6:9]}-{cpf_participante_input[9:]}"
        else:
            cpf_formatado = cpf_participante_input

        if cpf_validator.validate(cpf_formatado):
            cpf_participante = cpf_formatado
            break
        else:
            print("CPF inválido. Por favor, digite um CPF válido no formato XXX.XXX.XXX-XX ou apenas com 11 números.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar != 's' and continuar != 'sim':
                print("Inscrição cancelada.")
                return

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

    participante_encontrado = None
    for participante in participantes:
        if participante['cpf'] == cpf_participante: 
            participante_encontrado = participante
            break

    if not participante_encontrado:
        print(f"Participante com CPF '{cpf_participante}' não encontrado.")
        return

    if 'participantes' in evento_encontrado and participante_encontrado['cpf'] in evento_encontrado['participantes']:
        print(f"O participante com CPF '{participante_encontrado['cpf']}' já está inscrito no evento '{nome_evento}'.")
        return

    if 'participantes' not in evento_encontrado:
        evento_encontrado['participantes'] = []
    evento_encontrado['participantes'].append(participante_encontrado['cpf']) 

    if 'eventos_inscritos' not in participante_encontrado:
        participante_encontrado['eventos_inscritos'] = []
    
    if nome_evento not in participante_encontrado['eventos_inscritos']:
        participante_encontrado['eventos_inscritos'].append(nome_evento)

    salvar_dados(eventos, participantes)
    print(f"Participante '{participante_encontrado['nome']}' (CPF: {participante_encontrado['cpf']}) inscrito com sucesso no evento '{nome_evento}'.")


def listar_evento_por_participante():
    eventos, participantes = importar_dados() 
    cpf_validator = CPF()

    print("\n--- Listar Eventos por Participante ---")
    
    while True: 
        cpf_procurado = input("Digite o CPF do participante (formato XXX.XXX.XXX-XX ou apenas números): ").strip()
        if cpf_validator.validate(cpf_procurado) or (len(cpf_procurado) == 11 and cpf_procurado.isdigit() and cpf_validator.validate(cpf_procurado)): 
            if '-' not in cpf_procurado and '.' not in cpf_procurado: 
                cpf_procurado = f"{cpf_procurado[:3]}.{cpf_procurado[3:6]}.{cpf_procurado[6:9]}-{cpf_procurado[9:]}"
            break
        else:
            print("CPF inválido. Por favor, digite um CPF válido (formato XXX.XXX.XXX-XX ou apenas números).")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar != 's' and continuar != 'sim':
                print("Busca cancelada.")
                return

    participante_encontrado = None
    for participante in participantes:
        if participante['cpf'] == cpf_procurado:
            participante_encontrado = participante
            break

    if not participante_encontrado:
        print(f"Participante com CPF '{cpf_procurado}' não encontrado.")
        return

    eventos_inscritos = participante_encontrado.get('eventos_inscritos', [])

    if eventos_inscritos:
        print(f"\nEventos em que '{participante_encontrado['nome']}' (CPF: {cpf_procurado}) está inscrito:")
        for nome_evento_inscrito in eventos_inscritos:
            evento_detalhes = next((e for e in eventos if e['nome'] == nome_evento_inscrito), None)
            if evento_detalhes:
                print(f"- Nome: {evento_detalhes['nome']}, Data: {evento_detalhes['data']}, Tema: {evento_detalhes.get('tema', 'N/A')}")
            else:
                print(f"- {nome_evento_inscrito} (Detalhes não encontrados, evento pode ter sido removido)")
    else:
        print(f"O participante '{participante_encontrado['nome']}' não está inscrito em nenhum evento.")