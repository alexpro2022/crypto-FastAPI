# Crypto Deribit



[![Crypto Deribit Test Suite](https://github.com/alexpro2022/crypto-FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/crypto-FastAPI/actions/workflows/main.yml)



## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![APScheduler](https://img.shields.io/badge/-APScheduler-464646?logo=APScheduler)](https://apscheduler.readthedocs.io/en/stable/index.html)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)
[![asyncpg](https://img.shields.io/badge/-asyncpg-464646?logo=PostgreSQL)](https://pypi.org/project/asyncpg/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-v2.0-blue?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Alembic](https://img.shields.io/badge/-Alembic-464646?logo=alembic)](https://alembic.sqlalchemy.org/en/latest/)
[![Pytest-asyncio](https://img.shields.io/badge/-Pytest--asyncio-464646?logo=Pytest)](https://pypi.org/project/pytest-asyncio/)
[![docker_compose](https://img.shields.io/badge/-Docker%20Compose-464646?logo=docker)](https://docs.docker.com/compose/)
[![GitHub_Actions](https://img.shields.io/badge/-GitHub_Actions-464646?logo=GitHub)](https://docs.github.com/en/actions)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?logo=NGINX)](https://nginx.org/ru/)

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:

Задание
1 Написать для криптобиржи Deribit асинхронный клиент на aiohhtp.
Клиент должен каждую минуту забирать с биржи текущую цену BTC и ETH, после
чего сохранять в базу данных тикер валюты, текущую цену и время в UNIX.
2 Написать внешнее API для обработки сохраненных данных на FastAPI.
Должны быть следующие методы:
1 Получение всех сохраненных данных по указанной валюте
2 Получение последней цены валюты
3 Получение цены валюты с фильтром по дате
Все методы должны быть GET и у каждого метода дожен быть обязятельный query-
параметр "ticker".

[⬆️Оглавление](#оглавление)

<br>

## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).
#### Предварительные условия:
<details><summary>Подробнее</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или на удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:

    ```bash
    docker --version && docker-compose --version
    ```
</details>

<details><summary>Локальный запуск: Docker Compose</summary>
<h1></h1>
1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```bash
git clone https://github.com/alexpro2022/<REPOSITORY_NAME>.git && \
cd <REPOSITORY_NAME> && \
cp env_example .env && \
nano .env
```
2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах `db, web, nginx` по адресу http://localhost.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```
<h1></h1>
</details>

[⬆️Оглавление](#оглавление)

<br>

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr <REPOSITORY_NAME> && deactivate
```
  
[⬆️Оглавление](#оглавление)

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Проект)