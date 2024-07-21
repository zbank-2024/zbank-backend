from fastapi import FastAPI

from zbank.config.swagger import app_config
from zbank.router import router


app = FastAPI(**app_config)
app.include_router(router)


# Middlewares or something #
