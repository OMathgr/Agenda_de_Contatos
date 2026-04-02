import csv
import re
import os

#Verificação de Arquivo
Arquivo_Existe = os.path.exists('Contatos.csv')
Arquivo_Vazio = not Arquivo_Existe or  os.path.getsize('Contatos.csv') == 0

#Ler Contatos
try:
    with open ('Contatos.csv', mode='r', encoding='utf-8') as Contatos:
        leitor = csv.DictReader(Contatos)

        for linha in leitor:
            if linha.get('nome'):
                print(f"Nome: {linha['nome']}, Telefone: {linha['telefone']}, Email: {linha['email']}")

except FileNotFoundError:
    print("Arquivo ainda não existe.")

#Verificar Cabeçalho
if Arquivo_Existe and not Arquivo_Vazio:
    with open ('Contatos.csv', mode='r', encoding='utf-8') as f:
        primeira_linha = f.readline().strip()

    if primeira_linha != "nome,telefone,email":
        print ("Cabeçalho incorreto!")

#Adicionar Contatos
with open ('Contatos.csv', mode='a', encoding='utf-8', newline='') as Contatos:
    campos = ['nome', 'telefone', 'email']
    adicionar = csv.DictWriter(Contatos, fieldnames=campos)

    if Arquivo_Vazio:
        adicionar.writeheader()


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
            'telefone':telefone,
            'email':email
        }

        adicionar.writerow(novo_contato)
        print("Contato adicionado com sucesso!")