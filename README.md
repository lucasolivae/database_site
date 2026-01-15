# Database Site - Flask

🇧🇷 Projeto web simples desenvolvido em Python usando Flask.  
Permite cadastrar, buscar e excluir clientes em um banco de dados SQLite.  

🇺🇸 Simple web project developed in Python using Flask.  
Allows registering, searching and deleting clients in a SQLite database.

---

## Funcionalidades | Features

🇧🇷
- Cadastro de clientes (nome, data de nascimento e telefone)
- Geração automática de ID alfanumérico único (não se repete)
- Listagem de todos os clientes cadastrados
- Página individual para cada cliente
- Busca por nome ou ID
- Retorna múltiplos resultados para nomes iguais
- Exclusão de clientes com botão (delete)
- Confirmação antes de deletar
- Armazenamento em banco SQLite

🇺🇸
- Client registration (name, birth date and phone)
- Automatic unique alphanumeric ID generation (never repeats)
- List all registered clients
- Individual client page
- Search by name or ID
- Returns multiple results for duplicate names
- Delete clients with button
- Delete confirmation
- Data stored in SQLite database

---

## Como usar | How to use

Requisitos | Requirements  
- Python 3.x  
- Flask  

Instalação | Installation  
pip install flask  

Executando o projeto | Running the project  
python codigo.py  

Abra no navegador | Open in browser  
http://127.0.0.1:5000  

---

## Estrutura do projeto | Project structure

database_site/  
│  
├─ codigo.py  
├─ database.db  
└─ templates/  
   ├─ index.html  
   ├─ cliente.html  
   └─ resultado.html  

---

## Objetivo | Purpose

🇧🇷  
Projeto de estudo em backend para portfólio.  
Inclui operações reais com banco de dados, sistema de busca e exclusão de registros.

🇺🇸  
Backend study project for portfolio.  
Includes real database operations, search system and record deletion.

---

## Autor | Author

Lee  
GitHub: https://github.com/lucasolivae  

Desenvolvedor Brasileiro | Python & C# | Inglês (Intermediário)  
Brazilian Developer | Python & C# | English (Intermediate)
