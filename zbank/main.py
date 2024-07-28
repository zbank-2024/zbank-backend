from fastapi import FastAPI
from sqlalchemy.exc import NoResultFound

from zbank.config.swagger import app_config
from zbank.exceptions import http_not_found_exception_handler
from zbank.router import router


app = FastAPI(**app_config)
app.include_router(router)

app.add_exception_handler(NoResultFound, http_not_found_exception_handler)


# Middlewares or something #
