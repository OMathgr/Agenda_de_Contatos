# 📇 Sistema de Gerenciamento de Contatos

Um sistema simples de gerenciamento de contatos desenvolvido em Python, com persistência em arquivo CSV e interface via terminal.

---

## 🚀 Funcionalidades

* 📋 Listar contatos cadastrados
* ➕ Adicionar novos contatos
* 🔍 Buscar contatos por nome (busca parcial)
* ❌ Remover contatos com confirmação
* ✅ Validação de dados (telefone e email)
* 💾 Armazenamento em arquivo CSV

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Módulos padrão:

  * `csv`
  * `re`
  * `os`

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/OMathgr/Agenda_de_Contatos.git
```

2. Acesse a pasta do projeto:

```bash
cd Agenda_de_Contatos
```

3. Execute o programa:

```bash
python Agenda.py
```

---

## 💻 Exemplo de uso

```text
--- Menu ---
1 - Listar contatos
2 - Adicionar contato
3 - Buscar contato
4 - Remover contato
5 - Sair
```

---

## 🧪 Validações implementadas

* 📞 Telefone:

  * Remove caracteres não numéricos
  * Aceita apenas números com 10 ou 11 dígitos

* 📧 Email:

  * Validação básica com expressão regular

* 🧾 Campos obrigatórios:

  * Nome, telefone e email não podem estar vazios

---

## 📁 Estrutura do projeto

```text
📦 projeto
 ┣ 📄 Agenda.py
 ┣ 📄 Contatos.csv
 ┗ 📄 README.md
```

---

## 📌 Melhorias futuras

* ✏️ Editar contatos
* 🔍 Buscar e remover diretamente pelos resultados
* 🚫 Evitar contatos duplicados
* 🎨 Interface gráfica (GUI)
* 🌐 Integração com banco de dados

---

## 👨‍💻 Autor

Desenvolvido por **Matheus Graciano Ribeiro**

---

## 📄 Licença

Este projeto está sob a licença MIT.
