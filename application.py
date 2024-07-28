from uvicorn import run


# FIXME: подвязать на переменные среды
if __name__ == "__main__":
    run("zbank.main:app", host="localhost", port=8000)
