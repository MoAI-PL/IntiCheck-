# Use a lightweight Python 3.11 base image to keep the container size minimal
FROM python:3.11-slim

# Set environment variables for Python optimization
# 1. Prevent Python from writing .pyc files to disk
# 2. Ensure logs are sent straight to the terminal without buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker's layer caching
# This speeds up subsequent builds if dependencies haven't changed
COPY requirements.txt .

# Install dependencies without caching the index to save space
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project (Model, Frontend, Backend) into the container
COPY . .

# Create a temporary directory for file handling
# Note: Even with in-memory processing, Flask/Werkzeug may require a temp buffer
RUN mkdir -p /app/uploads && chmod 777 /app/uploads

# Expose port 7860 - the default requirement for Hugging Face Spaces
EXPOSE 7860

# Run the Flask server
# Binding to 0.0.0.0 ensures the app is accessible from outside the container
CMD ["python", "server.py"]