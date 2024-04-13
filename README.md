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

## Setup locally

Create a .venv on the project

```sh
poetry config virtualenvs.in-project true
```

Use the version in .python-version (if pyenv is installed and configured on shell)

```sh
poetry config virtualenvs.prefer-active-python true
```

## Settings

- Settings to use in VS Code:

```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--ignore=E24,W504,W503,E203",
    "--select=C,E,F,W,B,B9",
    "--exclude=.git,__pycache__,__init__.py,.mypy_cache,.pytest_cache",
    "--indent-size=4",
    "--max-doc-length=79",
    "--max-line-length=79",
    "--verbose"
  ],
  "files.trimFinalNewlines": true,
  "files.trimTrailingWhitespace": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length", "79"],
  "[python]": {
    "editor.rulers": [79, 79],
    "editor.formatOnSave": true,
    "editor.formatOnPaste": false,
    "editor.formatOnSaveMode": "file"
  }
}
```
