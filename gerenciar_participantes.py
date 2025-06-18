from gerenciar_dados import *
from validate_docbr import CPF
from datetime import datetime

def adicionar_participante():
    eventos,participantes = importar_dados()
    nome = input("Digite o nome do participante: ")
    while True:
        cpf = input("Digite o CPF do participante no formato XXX.XXX.XXX-XX: ").strip()
        if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
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
         
    while True:
        email = input("Digite o email do participante: ").lower().strip()
        if email != '' and '@' in email and '.' in email and email[0] != '@' and email[0] != '.' and " " not in email and '"' not in email and ',' not in email and '(' not in email and ')' not in email:
            if email in [p['email'] for p in participantes]:
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

def remover_participante():
    eventos, participantes = importar_dados()
    while True:
        cpf = input("Digite o CPF do participante a ser removido no formato XXX.XXX.XXX-XX: ").strip()
        if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
            break
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
            continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
            if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                print("Remoção cancelada.")
                return
            
    participante_encontrado = False
    for participante in participantes:
        if participante['cpf'] == cpf:
            participantes.remove(participante)
            participante_encontrado = True
            print(f"Participante {participante['nome']} removido com sucesso.")
            break
    
    if not participante_encontrado:
        print("Participante não encontrado.")
    
    salvar_dados(eventos, participantes)



def atualizar_email_participante():
    eventos, participantes = importar_dados()
    participante_encontrado = None
    while True:
        cpf = input("Digite o CPF do participante a ter seu email atualizado no formato XXX.XXX.XXX-XX: ").strip()
        if len(cpf) == 14 and (cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-'): 
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
    participantes = importar_dados() 
    
    while True:
        cpf = input("Digite o CPF do participante no formato XXX.XXX.XXX-XX: ").strip()
        if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-': 
            participante_encontrado = None 
            for p in participantes:
                if p['cpf'] == cpf: 
                    participante_encontrado = p
                    break 
            if participante_encontrado:
                print(f"Participante: {participante_encontrado['nome']}.")
                print(f"Email: {participante_encontrado['email']}.")
                preferencias = participante_encontrado['preferencias_tematicas']
                if preferencias:
                    print(f"Preferências temáticas: {', '.join(preferencias)}")
                else:
                    print("Preferências temáticas: Nenhuma informada.")
                    input("Presione Enter para continuar")
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
    cpf_participante = input("Digite o CPF do participante (apenas números): ").strip()

    if not cpf_validator.validate(cpf_participante):
        print("CPF inválido. Por favor, digite um CPF válido (apenas números).")
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

    if cpf_participante in evento_encontrado.get('participantes', []):
        print(f"O participante com CPF '{cpf_participante}' já está inscrito no evento '{nome_evento}'.")
        return

    if 'participantes' not in evento_encontrado:
        evento_encontrado['participantes'] = []
    evento_encontrado['participantes'].append(cpf_participante)

    if 'eventos_inscritos' not in participante_encontrado:
        participante_encontrado['eventos_inscritos'] = []
    if nome_evento not in participante_encontrado['eventos_inscritos']:
        participante_encontrado['eventos_inscritos'].append(nome_evento)

    salvar_dados(eventos, participantes)
    print(f"Participante '{participante_encontrado['nome']}' (CPF: {cpf_participante}) inscrito com sucesso no evento '{nome_evento}'.")


def listar_evento_por_participante():
    eventos, participantes = importar_dados()
    cpf_validator = CPF()

    print("\n--- Listar Eventos por Participante ---")
    cpf_procurado = input("Digite o CPF do participante (apenas números): ").strip()

    if not cpf_validator.validate(cpf_procurado):
        print("CPF inválido. Por favor, digite um CPF válido (apenas números).")
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
        print(f"Eventos em que '{participante_encontrado['nome']}' (CPF: {cpf_procurado}) está inscrito:")
        for nome_evento_inscrito in eventos_inscritos:
            evento_detalhes = next((e for e in eventos if e['nome'] == nome_evento_inscrito), None)
            if evento_detalhes:
                print(f"- Nome: {evento_detalhes['nome']}, Data: {evento_detalhes['data']}, Tema: {evento_detalhes.get('tema', 'N/A')}")
            else:
                print(f"- {nome_evento_inscrito} (Detalhes não encontrados, evento pode ter sido removido)")
    else:
        print(f"O participante '{participante_encontrado['nome']}' não está inscrito em nenhum evento.")

