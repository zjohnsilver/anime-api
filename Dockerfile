FROM python:3.12.0-slim

WORKDIR /server

ENV PYTHONUNBUFFERED=1 

COPY requirements.lock requirements-dev.lock ./

RUN sed '/-e/d' requirements.lock > requirements.txt && \
    sed '/-e/d' requirements-dev.lock > requirements.dev.txt && \
    pip install --no-cache-dir -r requirements.txt -r requirements.dev.txt && \
    rm requirements.txt requirements.dev.txt
