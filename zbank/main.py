from uvicorn import run

from zbank.application import app


if __name__ == "__main__":
    run(app, host="localhost", port=8000)
