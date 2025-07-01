import random
import os

def limpar_tela():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def calcula_digito_verificador(cpf_parcial, peso_inicial):
    soma = 0
    for i, digito in enumerate(cpf_parcial):
        soma += int(digito) * (peso_inicial - i)

    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def gerar_cpf_sintaticamente_valido():
    while True:
        nove_digitos = [random.randint(0, 9) for _ in range(9)]
        # Verifica se todos os dígitos são iguais
        if not all(d == nove_digitos[0] for d in nove_digitos):
            break
    
    # Converte a lista de dígitos para string
    cpf_base = "".join(map(str, nove_digitos))

    # Calcula o primeiro dígito verificador (D1)
    d1 = calcula_digito_verificador(cpf_base, 10)
    cpf_com_d1 = cpf_base + str(d1)

    # Calcula o segundo dígito verificador (D2)
    d2 = calcula_digito_verificador(cpf_com_d1, 11)

    # Monta o CPF completo
    cpf_completo = cpf_base + str(d1) + str(d2)

    # Formata o CPF para exibição
    cpf_formatado = f"{cpf_completo[0:3]}.{cpf_completo[3:6]}.{cpf_completo[6:9]}-{cpf_completo[9:11]}"
    
    return cpf_formatado

def gerar_nome_completo():
    nomes = ["João", "Moshi", "Juliano", "Maria", "Pedro", "Ana", "Lucas", "Laura", "Carlos", "Fernanda", "Rafael", "Camila","Marcos","Roberto",
                "Juliana","Eduardo","Patrícia","Gabriel","Sofia","Ricardo","Isabela","Thiago" ,"Larissa","Felipe","Mariana",
                "André","Aline","Bruno","Tatiane","Vinícius","Natália","Gustavo","Carolina","Diego","Beatriz","Rodrigo","Juliana",]

    sobrenomes = ["Silva", "Cavassini","Casagrande", "Souza", "Oliveira", "Santos", "Pereira", "Lima", "Costa", "Almeida", "Rocha", "Martins",
                "Gomes", "Ribeiro", "Barbosa", "Fernandes", "Cardoso", "Melo", "Teixeira", "Jacinto Pinto", "Nogueira", "Cavalcanti", "Araújo",
                "Dias", "Correia", "Mendes", "Castro", "Farias", "Monteiro", "Lopes", "Vieira", "Ramos", "Barros", "Campos",
                "Moreira", "Siqueira", "Pimentel", "Tavares", "Borges", "Cunha", "Freitas", "Machado", "Azevedo", "Gonçalves", "Lacerda"]
    nome_completo =  f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    return nome_completo

def gerar_email(nome_completo):
    nome, sobrenome = nome_completo.lower().split()
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "live.com"]
    email = f"{nome}.{sobrenome}@{random.choice(dominios)}"
    return email

# Gera e imprime um CPF sintaticamente válido
def gerar_perfil():
    limpar_tela()
    nome_completo = gerar_nome_completo()
    email = gerar_email(nome_completo)
    cpf = gerar_cpf_sintaticamente_valido()
    print(f"Nome: {nome_completo}")
    print(f"Email: {email}")
    print(f"CPF: {cpf}")
    input("Pressione Enter para continuar...")
    limpar_tela()

def gerar_evento():
    limpar_tela()
    nomes_evento = ["Hackathon", "Workshop de Python", "Seminário de IA", "Conferência de Tecnologia", "Encontro de Startups",
                    "Python para iniciantes", "Python avançado", "Desenvolvimento Web", "Machine Learning", "Data Science",
                    "Inteligência Artificial", "Desenvolvimento de Jogos", "Segurança da Informação", "Blockchain", "Desenvolvimento Móvel",
                    "Análise de Dados", "Big Data", "Cloud Computing", "DevOps", "Internet das Coisas", "Realidade Aumentada", 
                    "Realidade Virtual", "Robótica", "Automação", "Engenharia de Software",
                    "Design de Interface", "Experiência do Usuário", "Marketing Digital", "Gestão de Projetos", "Empreendedorismo Digital", 
                    "Inovação Tecnológica", "Transformação Digital", "Sustentabilidade em TI", "Ética em Tecnologia"]
    temas_evento = ["Tecnologia", "Inovação", "Desenvolvimento Pessoal", "Empreendedorismo", "Ciência de Dados","programação", "Aula",
                    "Palestra", "Workshop", "Seminário", "Conferência", "Hackathon", "Bootcamp", "Curso Online", "Treinamento", 
                    "Mentoria","Networking", "Feira de Tecnologia", "Exposição", "Fórum", "Simpósio", "Encontro", "Ciclo de Palestras",
                    "Masterclass", "Webinar", "Talk Show", "Painel de Discussão", "Mesa Redonda", "Rodada de Negócios", "Evento Corporativo",
                    "Evento Acadêmico", "Evento Social", "Evento Cultural", "Evento Esportivo", "Evento de Caridade", "Evento de Lançamento",
                    "Evento de Networking", "Evento de Confraternização", "Evento de Premiação"]
    data_evento = f"{random.randint(1, 31):02d}/{random.randint(1, 12):02d}/{random.randint(2025, 2028)}"
    palestrante = gerar_nome_completo()
    evento = {
        "nome": random.choice(nomes_evento),
        "data": data_evento,  
        "tema": random.choice(temas_evento),
        "palestrante": palestrante,
    }

    print(f"Evento: {evento['nome']}")
    print(f"Data: {evento['data']}")
    print(f"Tema: {evento['tema']}")
    print(f"Palestrante: {evento['palestrante']}")
    input("Pressione Enter para continuar...")  

while True:
    limpar_tela()
    print("Bem vindo ao gerador de informações de teste!") 
    print("1. Gerar perfil")
    print("2. Gerar evento")
    print("3. Sair")
    input_usuario = input("Escolha uma opção: ")
    if input_usuario == "1":
        perfil = gerar_perfil()
        limpar_tela()
    elif input_usuario == "2":
        gerar_evento()
        limpar_tela()
    elif input_usuario == "3":
        print("Saindo...")
        limpar_tela()
        break
    else:
        print("Opção inválida, tente novamente.")
        limpar_tela()
    
        
     
    