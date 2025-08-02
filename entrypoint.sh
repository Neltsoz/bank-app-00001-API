#!/bin/bash

set -e

until PGPASSWORD=$DB_PASSWORD psql -h "postgres_db" -U "$DB_USER" -d "$DB_NAME" -c "\q"; do
    >&2 echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done

>&2 echo "PostgreSQL is up - executing migrations"

alembic upgrade head

exec uvicorn main:app --host 0.0.0.0 --port 8000
