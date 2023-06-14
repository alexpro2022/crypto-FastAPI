# Crypto Deribit 
[![Crypto Deribit Test Suite](https://github.com/alexpro2022/crypto-FastAPI/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/crypto-FastAPI/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/alexpro2022/crypto-FastAPI/branch/main/graph/badge.svg?token=3JF5rKLnyD)](https://codecov.io/gh/alexpro2022/crypto-FastAPI)

### aiohttp-клиент для криптобиржи Deribit

[Тестовое задание](https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FNpKZnE3wuH7Stfm0GV0uDrURjfsXOmlJG5b847EUZFVt4FeMNp77zr2rYYv4qmPHq%2FJ6bpmRyOJonT3VoXnDag%3D%3D&name=%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_junior_back_end_%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA.pdf&nosw=1)

<br>

## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:
<details><summary>Подробнее</summary><br>
    
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
<h1></h1>

[⬆️Оглавление](#оглавление)
</details>

<br>

## Описание работы:
Приложение состоит из:
  1. `aiohttp`-клиента для криптобиржи **Deribit**
        - каждую минуту клиент забирает с биржи текущую цену `BTC` и `ETH` и сохраняет в базу данных тикер валюты, текущую цену и время в `UNIX`.
  3. API-сервиса для обработки сохраненных данных на `FastAPI` - реализует следующие GET-методы:
        - Получение всех сохраненных данных по указанной валюте
        - Получение последней цены валюты
        - Получение цены валюты с фильтром по дате
У каждого метода есть обязятельный query-параметр __ticker__, обозначающий трехсимвольный код валюты, например `BTC` или `ETH`

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
<h1></h1>
<details><summary>Локальный запуск: Docker Compose</summary>

1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, но их можно оставить):
```bash
git clone https://github.com/alexpro2022/crypto-FastAPI.git && \
cd crypto-FastAPI && \
cp env_example .env && \
nano .env
```
2. Из корневой директории проекта выполните команду:
```bash
docker compose -f infra/local/docker-compose.yml up -d --build
```
Проект будет развернут в трех docker-контейнерах `db, web, nginx` по адресу http://localhost. 

Администрирование приложения может быть осуществлено через Swagger доступный по адресу http://localhost/docs.

3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:
```bash
docker compose -f infra/local/docker-compose.yml down
```
Если также необходимо удалить тома базы данных, статики и медиа:
```bash
docker compose -f infra/local/docker-compose.yml down -v
```
<h1></h1>

[⬆️Оглавление](#оглавление)
</details>
 
<br>

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr crypto-FastAPI
```
  
[⬆️Оглавление](#оглавление)

<br>
    
## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#crypto-deribit)
