FROM python:3.8.12-slim-buster

WORKDIR /server

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry==1.1.11

RUN poetry config virtualenvs.create false

RUN poetry install

COPY . .
