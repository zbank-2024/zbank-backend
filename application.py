from uvicorn import run

from zbank.config.main import settings


# FIXME: подвязать на переменные среды
if __name__ == "__main__":
    run("zbank.main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
