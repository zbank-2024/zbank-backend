# "Проект банковской системы zbank"

## Содержание
- [Технологии](#технологии)
- [Установка и Запуск](#Установка-и-запуск)
- [Разработка](#Разработка)
- [Тестирование](#тестирование)
- [Deploy и CI/CD](#Deploy-и-CICD)

## Технологии
- [Python 3.11](https://www.python.org/)
- [FastApi](https://fastapi.tiangolo.com/ru/)
- [SqlAlchemy 2.0](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)

## Установка и запуск
### Локально
Установите и активируйте виртуальное окружение с помощью команд:
```sh
$ python3.11 -m venv venv
$ source venv/bin/activate
```

Установите зависимости:
```sh
$ pip install -r requirements.txt
```

Создайте в корне приложения файл .env и определите в нем все переменные, указанные в [.env.example](./.env.example).

Прогоните миграции с помощью команды:
```sh
$ alembic upgrade head
```

Запустите приложение с помощью [uvicorn](https://www.uvicorn.org/):
```sh
$ uvicorn kpp.main:app
```
### Через docker-compose
Создайте в корне приложения файл .env и определите в нем все переменные, указанные в [.env.example](./.env.example).

Соберите и запустите приложение с помощью [docker-compose](https://docs.docker.com/compose/):
```sh
$ docker-compose build
$ docker-compose up
```
## Разработка

### Добавление зависимостей
При добавлении новой библиотеки необходимо указать ее в файле [pyproject.toml](./pyproject.toml)

Затем пересобрать файл [requirements.txt](./requirements.txt) с помощью команды:
```sh
$ pip-compile
```

### Отправка МРа на код ревью
Перед тем, как залить коммит на гитлаб необходимо локально прогнать линтеры с помощью команды:
```sh
$ pre-commit run --all-files
```

## Тестирование
В разработке

## Deploy и CI/CD
В разработке