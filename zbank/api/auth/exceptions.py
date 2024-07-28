from fastapi import HTTPException, status


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неудается проверить учетные данные.",
    headers={"WWW-Authenticate": "Bearer"},
)
