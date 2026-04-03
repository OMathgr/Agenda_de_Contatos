import csv
import re
import os

#Constantes
ARQUIVO = 'Contatos.csv'
CAMPOS = ['nome', 'telefone', 'email']
CABEÇALHO_ESPERADO = ','.join(CAMPOS)

#Verificação e correção de cabeçalho
def verificar_e_corrigir_cabecalho():
    if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
        return
    
    with open (ARQUIVO, mode= 'r', encoding= 'utf-8') as f:
        primeira_linha = f.readline().strip()
        resto = f.read()

    if primeira_linha != CABEÇALHO_ESPERADO:
        print("Cabeçalho incorreto detectado, corrigindo...")
        with open (ARQUIVO, mode= 'w', encoding= 'utf-8') as f:
            f.write(CABEÇALHO_ESPERADO + '\n')
            
            if not resto.startswith('\n'):
                f.write('\n')

            f.write(resto)
        print("Cabeçalho corrigido!")
verificar_e_corrigir_cabecalho()

#Ler Contatos
def ler_contatos():
    contatos = []

    try:
        with open (ARQUIVO, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                if linha.get('nome'):
                    contatos.append(linha)

    except FileNotFoundError:
        pass
    
    return contatos

#Listar Contatos
def listar_contatos():
    contatos = ler_contatos()

    if not contatos:
        print ("Nenhum contato encontrado.")
        return

    for contato in contatos:
        print (f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

#Salvar Contatos
def salvar_contatos(contatos):
    with open (ARQUIVO, mode='w', encoding= 'utf-8', newline='') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(contatos)

#Adicionar Contatos
def adicionar_contato():
    nome = input("Digite o nome: ").strip()
    telefone = input("Digite o telefone: ").strip()
    email = input("Digite o email: ").strip()

    telefone_limpo = re.sub(r'\D', '', telefone)

    #Validações
    if not nome or not telefone or not email:
        print("Erro: Todos os campos são obrigatórios!")

    elif len(telefone_limpo) < 10:
        print("Erro: Telefone inválido!")

    elif not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        print("Erro: Email inválido!")

    else:
        novo_contato = {
            'nome': nome,
            'telefone':telefone_limpo,
            'email':email
        }

        contatos=ler_contatos()

        contatos.append(novo_contato)

        salvar_contatos(contatos)

        print("Contato adicionado com sucesso!")