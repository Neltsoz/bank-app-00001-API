# Bank App API

Простое банковское API на Python (FastAPI) с возможностями:
- Просмотр счетов и платежей пользователя.
- Управление пользователями для администраторов.
- Обработка webhook-уведомлений от платежных систем.

## Установка и запуск
1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Neltsoz/bank-app-00001-API.git
    cd bank-app-00001-API
    ```
2. Создайте файл .env в корне проекта с переменными:
    ```ini
    DB_USER=your_db_user
    DB_NAME=your_db_name
    DB_PASSWORD=your_db_password
    SECRET_KEY=your_secret_key
    ADMIN_NAME=admin
    ADMIN_PASSWORD=strong_password
    ADMIN_EMAIL=admin@example.com
    ```
3. Запуск через Docker:
    ```bash
    docker compose up -d --build
    ```

## Первоначальная настройка
Инициализируйте администратора:
    ```bash
    curl -X POST http://localhost:8000/api/v1/admin/init
    ```

## Документация API
После запуска документация будет доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Технологии
1. Backend:
    - Python 3.13
    - FastAPI
    - SQLAlchemy
    - Pydantic
    - Alembic
2. Базы данных:
    - PostgreSQL
3. Инфраструктура:
    - Docker
    - Docker Compose
