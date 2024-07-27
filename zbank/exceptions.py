from fastapi import status
from fastapi.responses import JSONResponse


def http_not_found_exception_handler(*_):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Запрашиваемый ресурс не найден."},
    )
