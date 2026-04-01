# EPS-Desafio-1

## Descrição

Este projeto é parte do primeiro desafio da disciplina de Engenharia de Produto de Software da Universidade de
Brasília (UnB).

## Dependências

- Python 3.12
- Poetry
- Docker
- Docker Compose

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter instalado:

- [Docker](https://docs.docker.com/get-docker/) (versão 20.10 ou superior)
- [Docker Compose](https://docs.docker.com/compose/install/) (versão 1.29 ou superior)

## Como Executar

### Modo Desenvolvimento com Docker

Para subir o ambiente em modo de desenvolvimento, execute o seguinte comando na raiz do projeto:

```bash
docker-compose -f docker-compose.dev.yml up --build
```