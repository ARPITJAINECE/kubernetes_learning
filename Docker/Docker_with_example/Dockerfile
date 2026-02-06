# ---------- Stage 1: Build stage ----------
# Used only to install dependencies
FROM python:3.13-alpine AS builder

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies into a temporary location
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: Runtime stage ----------
# Final image used to run the application
FROM python:3.13-alpine

# Set working directory
WORKDIR /app

# Copy only installed dependencies from build stage
COPY --from=builder /install /usr/local

# Copy application source code
COPY app.py .

# Document the port the Flask app listens on
EXPOSE 5000

# Start the Python application
CMD ["python", "app.py"]
