FROM python:3.11-slim

# Устанавливаем переменную среды, чтобы не создавать файлы pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Устанавливаем переменную среды, чтобы выключить буферизацию вывода
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "zbank.main:app", "--host", "0.0.0.0", "--port", "8000"]
