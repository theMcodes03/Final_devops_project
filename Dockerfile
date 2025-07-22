FROM python:3.11-slim

WORKDIR /app

# Add required system dependencies for psycopg2-binary
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "app.app:app", "--bind", "0.0.0.0:5000"]

