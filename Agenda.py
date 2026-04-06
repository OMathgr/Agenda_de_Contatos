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
            f.write(resto.lstrip('\n'))
        print("Cabeçalho corrigido!")

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

#Remover Contatos
def remover_contato():
    contatos = ler_contatos()

    if not contatos:
        print("Nenhum contato disponível.")
        return
    
    print("\n--- Lista de contatos: ---")
    for i, c in enumerate(contatos):
        print(f"{i} - {c['nome']} | {c['telefone']} | {c['email']}")

    try:
        indice = int(input("\nDigite o número do contato que deseja remover: "))

        if indice < 0 or indice >= len(contatos):
            print("Número inválido.")
            return
        
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return
    
    contato_escolhido = contatos[indice]

    while True:
        confirmar = input(f"Tem certeza que deseja remover '{contato_escolhido['nome']}'? (s/n): ").strip().lower()
        if confirmar in ['s', 'sim']:
            break
        elif confirmar in ['n', 'nao', 'não']:
            print("Remoção cancelada.")
            return
        else:
            print("Digite apenas 's' ou 'n'.")

    contato_removido = contatos.pop(indice)
    salvar_contatos(contatos)
    print(f"Contato '{contato_removido['nome']}' removido com sucesso!")

#Buscar Contatos
def buscar_contato(nome):
    contatos = ler_contatos()

    contatos_filtrados = [
        c for c in contatos if nome.lower() in c['nome'].lower()
    ]

    if not contatos_filtrados:
        print("Contato não encontrado.")
        return
    
    print("\nContatos correspondentes: ")
    for i, c in enumerate(contatos_filtrados):
        print(f"{i} - {c['nome']} | {c['telefone']} | {c['email']}")

def main():
    verificar_e_corrigir_cabecalho()

    while True:
        print("\n--- Menu: ---")
        print("1 - Listar contatos")
        print("2 - Adicionar Contato")
        print("3 - Buscar Contato")
        print("4 - Remover Contato")
        print("5 - Sair")

        try:
            escolha = int(input("Digite o número da opção desejada: ").strip())
            if escolha <= 0 or escolha > 5:
                print("Número inválido.")
                continue
            
            if escolha == 1:
                listar_contatos()
            
            elif escolha == 2:
                adicionar_contato()
            
            elif escolha == 3:
                nome = input("Digite o nome para a busca: ").strip()
                buscar_contato(nome)
            
            elif escolha == 4:
                remover_contato()
            
            elif escolha == 5:
                print("Saindo...")
                break

        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

#Main
if __name__ == "__main__":
    main()