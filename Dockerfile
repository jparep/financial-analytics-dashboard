# Multi-stage Dockerfile for a professional Dash app deployment

# Stage 1: Dependency installation and build
FROM python:3.11 AS builder

# Set environment variables for clean Python builds
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy only requirements to install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Stage 2: Lightweight runtime image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application files
COPY . .

# Expose the Dash app port
EXPOSE 8050

# Run the application with Gunicorn for better performance
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8050", "app:server"]
