# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в рабочую директорию
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Запускаем скрипт
CMD ["python", "main.py"]