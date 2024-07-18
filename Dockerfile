FROM python:3.10

# Установка зависимостей
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода
COPY . /app

# Запуск FastAPI сервера по умолчанию, если не указана другая команда
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
