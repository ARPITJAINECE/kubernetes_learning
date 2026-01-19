# Stage 1: Builder

FROM python:3.13-alpine AS builder

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure logs are flushed immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY todo_app/requirements.txt ./todo_app/requirements.txt

# Install dependencies into a temporary directory
RUN pip install --no-cache-dir --prefix=/install -r todo_app/requirements.txt


# Stage 2: Secoind Stage

FROM python:3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local

COPY todo_app ./todo_app/

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["todo_app/main.py"]