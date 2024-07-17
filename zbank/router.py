from zbank.api.root.router import router as root_router
from zbank.application import app


app.include_router(root_router)
