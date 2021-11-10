# Anime API

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Application to try out FastAPI and RabbitMQ

## Before Running

- Create and start a virtual environment

```sh
poetry shell
```

- Install requirements

```sh
poetry install
```

## Running

Requerimentos:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Após isso é só utilizar o comando do Makefile para iniciar o container do Docker:

```sh
make docker/start
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
    "python.formatting.blackArgs": [
        "--line-length",
        "79"
    ],
    "[python]": {
      "editor.rulers": [79, 79],
      "editor.formatOnSave": true,
      "editor.formatOnPaste": false,
      "editor.formatOnSaveMode": "file"
    }
  }

```
