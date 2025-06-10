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
                    print("Cadastro cancelado.")
                    return
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
        if len(cpf) == 14 and (cpf[3] == '.' or cpf[7] == '.' or cpf[11] == '-'):
            for participante in participantes:
                if participante['cpf'] == cpf:
                    participante_encontrado = participante
                    break
                else:
                    print("Participante não encontrado com este CPF.")
                    continuar = input("Deseja tentar novamente? (s/n): ").lower().strip()
                    if continuar == 'n' or continuar == 'nao' or continuar == 'não':
                        print("Atualização cancelada.")
                        return

  
    while True:
        email = input("Digite o novo email do participante: ").strip().lower()
            
        if   email != '' and '@' in email and '.' in email and email[0] != '@' and email[0] != '.' and " " not in email and '"' not in email and ',' not in email and '(' not in email and ')' not in email:

                email_ja_em_uso = False
                if email in [p['email'] for p in participantes]:
                    email_ja_em_uso = True
                    break
                    
                if email_ja_em_uso:
                    print("Já existe um participante cadastrado com este email.")
                    continuar = input("Deseja tentar novamente o email? (s/n): ").lower().strip()
                    if continuar == 's' or continuar == 'sim': 
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
    
    
    

def buscar_participante_por_id():
    pass

def verificar_participante_duplicado():
    pass

def remover_participante_duplicado():
    pass

def inscrever_participante_evento():
    pass

def listar_evento_por_participante():
    pass

def buscar_remover_participante_duplicado_evento():
    pass

atualizar_email_participante()