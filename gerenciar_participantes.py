from gerenciar_dados import *

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
        cpf = input("Digite o CPF do participante a ser removido no formato XXX.XXX.XXX-XX: ").strip().strip()
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
    eventos, participantes = importar_dados()
    
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
    pass

def listar_evento_por_participante():
    pass

def buscar_remover_participante_duplicado_evento():
    pass

buscar_participante_por_cpf()