FROM python:3.13-slim-bookworm as builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends libpq5 postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY alembic.ini .
COPY main.py .
COPY alembic ./alembic
COPY app ./app

ENV PYTHONPATH=/app
ENV ALEMBIC_CONFIG=/app/alembic.ini

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh
