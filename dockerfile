# Dockerfile for Robot Controller

# Use official Python slim image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files
COPY . .

# Add src/ to PYTHONPATH
ENV PYTHONPATH="/app/src"

CMD ["python", "src/main.py"]
