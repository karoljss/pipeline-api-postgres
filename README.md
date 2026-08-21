# 🚀 Pipeline ETL de Cotação de Moedas (API ➔ PostgreSQL + Docker)


Este projeto consiste na construção de um pipeline de engenharia de dados de ponta a ponta que realiza a extração de cotações financeiras em tempo real via API REST, transforma os dados com **Pandas** e realiza a carga automatizada em um banco de dados relacional **PostgreSQL** rodando em container **Docker**.


## 🏗️ Arquitetura da Solução


- **Extração (Extract):** Consumo de dados via requisição HTTP (`requests`) da API AwesomeAPI.

- **Transformação (Transform):** Limpeza, tipagem de dados e estruturação temporal com `Pandas`.

- **Carga (Load):** Mapeamento objeto-relacional e persistência no PostgreSQL usando `SQLAlchemy`.

- **Infraestrutura:** Containerização do banco de dados com `Docker` e `Docker Compose`.

- **Ambiente de Dev:** Isolamento de dependências no Linux via `venv`.


---


## 🛠️ Tecnologias Utilizadas


- **Linguagem:** Python 3.12

- **Bibliotecas:** Pandas, SQLAlchemy, Psycopg2, Requests

- **Banco de Dados:** PostgreSQL 15 (Alpine)

- **DevOps & Infra:** Docker, Docker Compose, Linux Bash, Git


---


## 💻 Como Rodar o Projeto Localmente


### Pré-requisitos

- Docker e Docker Compose instalados.

- Python 3.x e ambiente `venv`.


### Passo a Passo


1. **Clonar o repositório:**

   ```bash

   git clone [https://github.com/seu-usuario/pipeline-api-postgres.git](https://github.com/karoljss/pipeline-api-postgres.git)

   cd pipeline-api-postgres 