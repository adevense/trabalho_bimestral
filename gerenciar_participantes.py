from gerenciar_dados import *

def adicionar_participante():
    eventos,participantes = importar_dados()
    nome = input("Digite o nome do participante: ")
    while True:
        cpf = input("Digite o CPF do participante no formato XXX.XXX.XXX-XX: ")
        if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
            if cpf in [p['cpf'] for p in participantes]:
                print("Participante já cadastrado com este CPF.")
                continuar = input("Deseja tentar novamente? (s/n): ").lower()
                if continuar == 's':
                    print('')
                    
                else:
                    print("Cadastro cancelado.")
                    return
            else:
                break
        else:
            print("CPF inválido. Certifique-se de que o formato está correto (XXX.XXX.XXX-XX) e tente novamente.")
         

        
    email = input("Digite o email do participante: ")
    novo_participante = {
        "cpf": cpf,
        "nome": nome,
        "email": email,
        "preferencias_tematicas":[]
    }
    
    participantes.append(novo_participante)
    salvar_dados(eventos,participantes)

def remover_participante():
    pass

def atualizar_email_participante():
    pass

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

adicionar_participante()