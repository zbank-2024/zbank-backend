from fastapi import APIRouter

from zbank.api.auth.router import router as auth_router
from zbank.api.health.router import router as health_router


router = APIRouter(prefix='/v1')

routers_to_include = [
    auth_router,
    health_router,
]

for router_to_add in routers_to_include:
    router.include_router(router_to_add)
