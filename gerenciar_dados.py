import json

def importar_dados_eventos():
    with open('banco.json','r') as banco: # estou abrindo o arquivo json em modo de leitura(r)
        dados  = json.load(banco) # estou carregando o conteudo do arquivo json para um dicionario dados
    eventos = dados["eventos"] # estou pegando o conteudo do dicionario dados e atribuindo a variavel evento
    return eventos

def importar_dados_participantes():
    with open('banco.json','r') as banco: 
        dados  = json.load(banco) 
    participantes = dados["participantes"] 
    return participantes

def salvar_dados():
    importar_dados_eventos()
    importar_dados_participantes()
    with open('banco.json','w') as banco: # estou abrindo o arquivo json em modo de escrita(w)
        json.dump({"eventos": importar_dados_eventos(), "participantes": importar_dados_participantes()}, banco, indent=4)

