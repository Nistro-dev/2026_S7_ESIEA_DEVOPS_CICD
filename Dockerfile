FROM python:3.11-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api.py db.py utils.py ./

ENV APP_DB_PATH=/data/app.db

RUN mkdir -p /data

EXPOSE 8000

CMD ["python", "api.py"]
