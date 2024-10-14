tags_metadata = [
    {
        "name": "health",
        "description": "Проверяет работспособность API",
    },
    {
        "name": "auth",
        "description": "Авторизация",
    },
]


app_config = dict(
    title='Zbank API',
    description='Система банковского учета zoonk',
    version='1.0.0',
    openapi_tags=tags_metadata,
)
