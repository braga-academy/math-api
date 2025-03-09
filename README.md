# Calc API

API RESTful para realizar operações matemáticas de soma e média.

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Configuração do Projeto](#configuração-do-projeto)
- [Executando a Aplicação](#executando-a-aplicação)
- [Testes](#testes)
- [Documentação da API](#documentação-da-api)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

A Calc API é uma aplicação RESTful desenvolvida em Python com FastAPI. Ela realiza operações matemáticas básicas, como somar números e calcular a média de uma lista de números. A aplicação utiliza Redis para cache e Docker para facilitar a execução em diferentes ambientes.

## Funcionalidades

- **Somar números**: Recebe uma lista de números inteiros e retorna a soma.
- **Calcular média**: Recebe uma lista de números inteiros e retorna a média aritmética.
- **Cache com Redis**: Armazena resultados de operações para melhorar o desempenho.
- **Health Check**: Endpoint para verificar o status da API.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework para construção da API.
- **Redis**: Banco de dados em memória para cache.
- **Docker**: Containerização da aplicação.
- **Pydantic**: Validação de dados.
- **Pytest**: Testes unitários e de integração.
- **GitHub Actions**: CI/CD para execução automática de testes.

## Pré-requisitos

- **Docker**: Instale o Docker
- **Docker Compose**: Instale o Docker Compose
- **Python 3.9** (opcional, apenas para execução local sem Docker).

## Configuração do Projeto

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/calc-api.git
cd calc-api
```

Crie um arquivo `.env` (opcional):

Se precisar configurar variáveis de ambiente, crie um arquivo `.env` na raiz do projeto:

```bash
REDIS_URL=redis://redis:6379
```

## Executando a Aplicação

### Usando Docker Compose

Construa e execute os containers:

```bash
docker-compose up --build
```

Acesse a aplicação:

A API estará disponível em [http://localhost:8000](http://localhost:8000).

### Executando Localmente (sem Docker)

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn app.main:app --reload
```

Acesse a aplicação:

A API estará disponível em [http://localhost:8000](http://localhost:8000).

## Testes

### Testes Unitários e de Integração

Execute os testes:

```bash
docker-compose exec web pytest tests/
```

### Cobertura de Testes

Para verificar a cobertura de testes, execute:

```bash
docker-compose exec web pytest --cov=app tests/
```

### CI/CD com GitHub Actions

Os testes são executados automaticamente em cada push ou pull request para o repositório. O workflow está configurado no arquivo `.github/workflows/ci.yml`.

## Documentação da API

A documentação da API é gerada automaticamente pelo FastAPI e pode ser acessada nos seguintes links:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### 1. Somar Números

- **Método**: POST
- **URL**: `/api/v1/sum/`
- **Descrição**: Recebe uma lista de números e retorna a soma.

**Exemplo de Requisição**:

```json
{
    "numbers": [1, 2, 3]
}
```

**Exemplo de Resposta**:

```json
{
    "sum": 6
}
```

#### 2. Calcular Média

- **Método**: POST
- **URL**: `/api/v1/average/`
- **Descrição**: Recebe uma lista de números e retorna a média aritmética.

**Exemplo de Requisição**:

```json
{
    "numbers": [1, 2, 3]
}
```

**Exemplo de Resposta**:

```json
{
    "average": 2.0
}
```

#### 3. Health Check

- **Método**: GET
- **URL**: `/api/v1/health/`
- **Descrição**: Verifica o status da API.

**Exemplo de Resposta**:

```json
{
    "status": "ok",
    "message": "API está funcionando corretamente."
}
```

## Estrutura do Projeto

```plaintext
calc-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── math.py          # Rotas para operações matemáticas
│   │   └── health.py        # Rota para health check
│   ├── models/
│   │   ├── __init__.py
│   │   └── numbers.py       # Modelos de dados
│   ├── services/
│   │   ├── __init__.py
│   │   └── math_operations.py  # Lógica de negócio
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_numbers_request.py
│   │   ├── test_numbers_class.py
│   │   └── test_number_class.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api_endpoints.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

## Contribuição

Faça um fork do repositório.

Crie uma nova branch:

```bash
git checkout -b feature/nova-feature
```

Faça commit das suas alterações:

```bash
git commit -m "Adiciona nova feature"
```

Envie as alterações:

```bash
git push origin feature/nova-feature
```

Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Se precisar de mais ajustes ou tiver dúvidas, estou à disposição! 😊
