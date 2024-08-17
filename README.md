# Anime API

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Anime API criada utilizando o framework FastAPI

## Especificações

- [FastAPI](https://fastapi.tiangolo.com/) como framework
- [MongoDB](https://www.mongodb.com/) como database
- [Pydantic](https://pydantic-docs.helpmanual.io/) como validator/formatador de dados da API
- [Flake8](https://flake8.pycqa.org/en/latest/) como linter
- [Black](https://black.readthedocs.io/en/stable/) como formatador de código
- [Pytest](https://docs.pytest.org/en/6.2.x/) como framework de testes
- [Poetry](https://python-poetry.org/) como workflow de dev e gerenciador dos pacotes

## Running

Requerimentos:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Após isso é só utilizar o comando do Makefile para iniciar o container do Docker:

```sh
make docker/start
```
