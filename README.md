# "Проект банковской системы zbank"

## Содержание
- [Технологии](#технологии)
- [Установка и Запуск](#Установка-и-запуск)
- [Разработка](#Разработка)
- [Deploy и CI/CD](#Deploy-и-CICD)
- [Тестирование](#тестирование)

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

### Отправка PR на код ревью
Перед тем, как залить коммит на гитлаб необходимо локально прогнать линтеры с помощью команды:
```sh
$ pre-commit run --all-files
```

## Deploy и CI/CD
### Обновление статуса на 'Ревью'
Когда изменения пушатся в репозиторий, статус задачи в Yandex Tracker автоматически меняется на 'Ревью'.
Для функционирования необходимо:
1. Выполнять задачу в ветке с именем, представляющим из себя код задачи.
2. В описании (коммит-месседже) первого заливаемого коммита также обязательно указать код задачи.

### Обновление статуса на 'Тестируется'
После успешного слияния PR в ветку main, статус задачи в Yandex Tracker обновляется на 'Тестируется'.
Для функционирования необходимо:
1. Слить PR ветки с именем, представляющим из себя код задачи в главную ветку.

## Тестирование
В разработке
