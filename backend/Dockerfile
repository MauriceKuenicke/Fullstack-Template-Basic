FROM python:3.9-slim

# Set environment variables for Python.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install build dependencies and system packages if needed.
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000