# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent .pyc files
ENV PYTHONUNBUFFERED 1        # Ensure logs are output directly

# Set the working directory in the container
WORKDIR /app

# Install dependencies in a single layer for smaller image size
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the Dash default port
EXPOSE 8050

# Specify the command to run the application
CMD ["python", "app.py"]
