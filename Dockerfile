# Multi-stage Dockerfile for a professional Dash app deployment

# Stage 1: Dependency installation and build
FROM python:3.11 AS builder

# Set environment variables for clean Python builds
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install necessary build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements to install dependencies
COPY requirements.txt ./
RUN python -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Lightweight runtime image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Copy virtual environment and application files with correct ownership
COPY --chown=appuser:appgroup --from=builder /app/venv /app/venv
COPY --chown=appuser:appgroup . .

# Expose the Dash app port (default: 8050)
EXPOSE 8050

# Run the application with Gunicorn for better performance
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8050", "app:server"]
