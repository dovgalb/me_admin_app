pyenv install 3.11.5

pyenv local 3.11.5

poetry shell

это структура моего проекта
.
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── src
    ├── admin
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── __init__.py

это мой docker=compose.yml файл
version: '3.8'

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8000:8000
    volumes:
      - .:/app

это мой Dockerfile
FROM python:3.11.5
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD 'cd /app/src && python manage.py runserver 0.0.0.0:8000'


это ошибка, которая падает в конейнере
/bin/sh: 1: cd /app/src && python manage.py runserver 0.0.0.0:8000: not found

в чем проблема?
