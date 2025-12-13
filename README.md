# Schiphol ETL Pipeline

## ✈️ Visão Geral

O **Schiphol ETL** é um projeto de engenharia de dados desenvolvido em Python com o objetivo de **extrair, transformar e carregar (ETL)** dados públicos do **Aeroporto de Schiphol (Amsterdam Airport Schiphol)** para um banco de dados relacional, seguindo **boas práticas de arquitetura, separação por camadas e validação de dados**.

O projeto foi pensado para ser **modular, extensível e profissional**, simulando um cenário real de pipeline de dados utilizado em ambientes corporativos.

---

## 🌍 O que é o Aeroporto de Schiphol?

O **Amsterdam Airport Schiphol (AMS)** é um dos maiores e mais importantes aeroportos da Europa, servindo como hub internacional para voos comerciais, cargas e conexões globais.

A API pública do Schiphol disponibiliza informações como:

* ✈️ Voos (chegadas e partidas)
* 🛫 Tipos de aeronaves
* 🏢 Companhias aéreas
* 🌎 Destinos

Esses dados são ideais para estudos de **ETL, modelagem de dados, validação, observabilidade e persistência**.

---

## 🧠 Arquitetura do Projeto

O projeto segue uma **arquitetura inspirada em Clean Architecture / DDD**, separando responsabilidades em camadas bem definidas:

```text
src/
├── app/                # Ponto de entrada da aplicação
├── domain/             # Regras de negócio e entidades
├── pipeline/           # Orquestração do ETL (extract, transform, load)
├── infrastructure/     # Banco de dados, ORM, schemas e conexões
├── settings/           # Configurações, logging e observabilidade
```

### 🔹 Domain

Camada mais importante do projeto.

* **Entities**: modelos de domínio (não dependem de banco ou framework)
* **Interfaces**: contratos para extract / transform / load
* **Exceptions**: exceções específicas do pipeline

> Aqui está a regra de ouro: **o domínio não conhece infraestrutura**.

---

## 📦 Tecnologias Utilizadas

O projeto utiliza um conjunto de bibliotecas modernas e amplamente usadas em **engenharia de dados** e **back-end em Python**:

### 🐍 Python 3.12

Linguagem principal do projeto.

---

### 🐼 Pandas

Utilizado principalmente para:

* Exploração inicial dos dados
* Prototipação do ETL (notebooks)
* Manipulação e normalização de dados tabulares

> O uso de Pandas está concentrado na fase exploratória, evitando dependência excessiva no pipeline final.

---

### 📘 Pydantic

Utilizado para:

* Validação rigorosa dos dados vindos da API do Schiphol
* Garantia de tipagem forte
* Conversão segura de dados externos

Responsabilidades principais:

* Garantir que campos obrigatórios não sejam `None`
* Validar estruturas complexas (dicts, listas, datas)
* Evitar dados inconsistentes chegando ao banco

---

### 🗄️ SQLAlchemy

Responsável pela **camada de persistência**:

* Mapeamento ORM (models)
* Definição de entidades de banco
* Criação e gerenciamento de sessões
* Integração com PostgreSQL

A separação é clara:

* **Schemas**: representação dos dados
* **Models**: mapeamento ORM
* **Connections**: conexão com o banco

---

### 🧬 Alembic *(não aplicado ainda)*

A biblioteca **Alembic** já está incluída no projeto, com o objetivo de:

* Versionamento de schema
* Controle de migrações de banco de dados

> ⚠️ No estado atual do projeto, **as migrações ainda não foram implementadas**. A criação de tabelas é feita via script Python.

---

### 🌐 Requests

Utilizado para:

* Consumo da API pública do Schiphol
* Comunicação HTTP de forma simples e explícita

Bibliotecas auxiliares:

* **types-requests** → tipagem estática

---

### 🧪 Tipagem e Qualidade de Código

* **pandas-stubs** → tipagem estática para DataFrames
* Tipagem explícita em entidades, schemas e interfaces

---

### 🐘 PostgreSQL

Banco de dados relacional utilizado para persistência dos dados.

Driver:

* **psycopg2-binary**

---

### 🔐 python-dotenv

Utilizado para:

* Gerenciamento de variáveis de ambiente
* Separação entre código e credenciais sensíveis

---

### 📊 Logfire (Pydantic)

O projeto utiliza **Logfire** para observabilidade:

* Rastreamento de execuções
* Logs estruturados
* Monitoramento do pipeline

Ao rodar o projeto, um link de observabilidade é gerado automaticamente:

```text
Logfire project URL: https://logfire-us.pydantic.dev/deezinn/schiphol-etl
```

---

### 🚫 Apache Airflow *(não utilizado)*

Embora o projeto tenha uma estrutura **compatível com orquestração**, o **Apache Airflow ainda não foi aplicado**.

A arquitetura atual facilita uma futura integração com:

* DAGs
* Schedulers
* Observabilidade avançada

---

### 🗄️ SQLAlchemy

Responsável pela **camada de persistência**:

* Mapeamento ORM (models)
* Criação de tabelas
* Conexão com PostgreSQL

A separação é clara:

* **Schemas**: representação dos dados
* **Models**: mapeamento ORM
* **Connections**: conexão com o banco

---

### 📊 Logfire (Pydantic)

O projeto utiliza **Logfire** para observabilidade:

* Rastreamento de execuções
* Logs estruturados
* Monitoramento do pipeline

Ao rodar o projeto, um link de observabilidade é gerado automaticamente:

```text
Logfire project URL: https://logfire-us.pydantic.dev/deezinn/schiphol-etl
```

---

### 🐳 Docker & Docker Compose

O projeto já está preparado para execução em containers:

* Banco de dados PostgreSQL
* Ambiente isolado
* Facilidade de deploy

---

## 🔄 Pipeline ETL

O pipeline segue o fluxo clássico:

1. **Extract**

   * Consome dados da API do Schiphol

2. **Transform**

   * Normalização
   * Conversão de tipos
   * Validação com Pydantic
   * Mapeamento domínio → persistência

3. **Load**

   * Inserção no PostgreSQL via SQLAlchemy

---

## 🧪 Notebooks

A pasta `notebooks/` contém **prototipações iniciais do ETL**, usadas para:

* Explorar os dados da API
* Testar transformações
* Validar modelos

Eles serviram como base para a implementação final do pipeline.

---

## ⚙️ Como Rodar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone <repo-url>
cd Schiphol-etl
```

---

### 2️⃣ Crie e ative o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure as credenciais

Edite o arquivo:

```text
src/infrastructure/security/credentials.py
```

Inclua:

* Credenciais da API do Schiphol
* Dados de conexão com o PostgreSQL

---

### 5️⃣ Suba os serviços com Docker (opcional)

```bash
docker-compose up -d
```

---

### 6️⃣ Crie as tabelas no banco

```bash
python3 -m src.settings.create_table
```

---

### 7️⃣ Execute o pipeline

```bash
python3 -m src.app.main
```

---

## 📁 Logs

Os logs são armazenados em:

```text
logs/
└── teste.log
```

Além disso, toda a execução pode ser acompanhada pelo **Logfire**.

---

## 🚀 Objetivos do Projeto

Este projeto foi desenvolvido com foco em:

* Engenharia de Dados profissional
* Arquitetura limpa
* Validação forte de dados
* Observabilidade
* Escalabilidade

É um excelente exemplo de pipeline realista para:

* Portfólio
* Estudos avançados de ETL
* Base para orquestração com Airflow futuramente

---

## 📜 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Projeto desenvolvido por **André Luiz**, com foco em boas práticas de engenharia de dados, Python moderno e arquitetura de software.

---

Se quiser evoluir este projeto para **Airflow, CI/CD ou Data Lake**, ele já está pronto estruturalmente para isso.
