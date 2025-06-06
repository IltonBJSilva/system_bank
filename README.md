# 🏦 Sistema Bancário com Flask e PostgreSQL

Este projeto é uma implementação de um sistema bancário básico, desenvolvido em Python utilizando o framework Flask para a interface web e o PostgreSQL para persistência de dados. Ele oferece funcionalidades essenciais de banco, como depósitos, saques e consulta de extrato, com todos os dados sendo armazenados de forma robusta em um banco de dados relacional.

Ideal para servir como um projeto de portfólio, demonstrando habilidades em desenvolvimento web com Python, integração com banco de dados (SQLAlchemy) e resolução de problemas comuns de persistência e tipagem de dados.

## ✨ Funcionalidades

A versão atual do sistema bancário implementa as seguintes operações:

1.  **Depósito:** Permite adicionar valores positivos à conta.
2.  **Saque:** Possibilita realizar até 3 saques diários, com limite máximo de R$ 500,00 por saque, e validação de saldo suficiente.
3.  **Extrato:** Exibe o histórico de todas as transações (depósitos e saques) realizadas na conta, com o saldo atual.
4.  **Geração de Extrato em Arquivo:** Permite baixar o extrato completo da conta em um arquivo de texto para referência futura.

**Observação:** Esta versão do sistema é simplificada e trabalha com uma única conta para demonstração, sem a necessidade de identificação de agência ou conta bancária por parte do usuário.

## 🚀 Tecnologias Utilizadas

* **Python 3.x**
* **Flask:** Microframework web para Python.
* **Flask-SQLAlchemy:** Extensão do Flask para uso de SQLAlchemy, facilitando a interação com o banco de dados.
* **SQLAlchemy:** ORM (Object-Relational Mapper) para manipulação de dados.
* **Psycopg2:** Adaptador PostgreSQL para Python.
* **PostgreSQL:** Sistema de Gerenciamento de Banco de Dados Relacional (SGBDR).
* **HTML/CSS:** Para a interface do usuário.

## ⚙️ Configuração e Instalação

Para rodar este projeto em sua máquina local, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter instalado em seu sistema:

* [**Python 3.x**](https://www.python.org/downloads/)
* [**PostgreSQL**](https://www.postgresql.org/download/) (e o pgAdmin 4 para gerenciamento, recomendado)

### 2. Configuração do Banco de Dados PostgreSQL

1.  **Acesse o terminal do PostgreSQL (`psql`) ou o pgAdmin 4.**
2.  **Crie um novo usuário (role) para o sistema** (ou utilize o usuário `postgres` padrão). É altamente recomendado usar um usuário com senha forte e **apenas caracteres ASCII** para evitar problemas de codificação.
    ```sql
    CREATE USER system_bank WITH PASSWORD 'sua_senha_segura';
    ```
3.  **Crie um banco de dados dedicado para o projeto** e atribua o usuário criado como proprietário:
    ```sql
    CREATE DATABASE system_bank OWNER system_bank;
    ```
4.  **Conceda todos os privilégios** ao usuário no banco de dados (para desenvolvimento):
    ```sql
    GRANT ALL PRIVILEGES ON DATABASE system_bank TO system_bank;
    ```
    *Se você optar por usar o banco de dados `postgres` e o usuário `postgres`, pule os passos 2, 3 e 4, mas ajuste a string de conexão nos passos a seguir.*

### 3. Configuração do Projeto Python

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/system_bank.git](https://github.com/seu-usuario/system_bank.git) # Substitua pelo seu repositório
    cd system_bank
    ```
2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/macOS:
    source venv/bin/activate
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install Flask Flask-SQLAlchemy psycopg2-binary
    ```
4.  **Configure a Conexão com o Banco de Dados:**
    * Abra o arquivo `Models/database.py`.
    * Atualize a linha `app.config["SQLALCHEMY_DATABASE_URI"]` com suas credenciais do PostgreSQL.
        * **Exemplo (se você criou o usuário e banco de dados `system_bank`):**
            ```python
            app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://system_bank:sua_senha_segura@localhost:5432/system_bank"
            ```
        * **Exemplo (se você está usando o usuário e banco de dados padrão `postgres`):**
            ```python
            app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:sua_senha_do_postgres@localhost:5432/postgres"
            ```
        * **ATENÇÃO:** Certifique-se de que `sua_senha_segura` (ou `sua_senha_do_postgres`) contenha **apenas caracteres ASCII básicos** (letras, números, símbolos como `!@#$%`). Caracteres acentuados podem causar erros de codificação.
    * Salve o arquivo `Models/database.py`.

## ▶️ Como Rodar

Com todas as configurações feitas, execute o arquivo `main.py`:

```bash
python main.py