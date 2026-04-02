import csv
import re
import os

#Constantes
ARQUIVO = 'Contatos.csv'
CAMPOS = ['nome', 'telefone', 'email']
CABEÇALHO_ESPERADO = ','.join(CAMPOS)

#Verificação de Arquivo
arquivo_existe = os.path.exists(ARQUIVO)
arquivo_vazio = not arquivo_existe or  os.path.getsize(ARQUIVO) == 0

#Verificação e correção de cabeçalho
def verificar_e_corrigir_cabecalho():
    if not arquivo_existe or arquivo_vazio:
        return ("Arquivo novo, o cabeçalho será criado na hora de adicionar")
    
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
try:
    with open (ARQUIVO, mode='r', encoding='utf-8') as Contatos:
        leitor = csv.DictReader(Contatos)

        for linha in leitor:
            if linha.get('nome'):
                print(f"Nome: {linha['nome']}, Telefone: {linha['telefone']}, Email: {linha['email']}")

except FileNotFoundError:
    print("Arquivo ainda não existe.")

#Adicionar Contatos
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

    with open (ARQUIVO, mode='a', encoding='utf-8', newline='') as Contatos:
        adicionar = csv.DictWriter(Contatos, fieldnames=CAMPOS)

        if arquivo_vazio:
            adicionar.writeheader()

        adicionar.writerow(novo_contato)
        print("Contato adicionado com sucesso!")