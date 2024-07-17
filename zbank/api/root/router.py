from fastapi import APIRouter


root_router = APIRouter(prefix="/")


root_router.get("/")


async def root():
    return {"message": "root page here"}
