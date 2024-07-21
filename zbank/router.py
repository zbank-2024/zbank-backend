from fastapi import APIRouter

from zbank.api.health.router import health_router


router = APIRouter(prefix='/v1')
router.include_router(health_router)
