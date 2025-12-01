FROM python:3.11-slim

# Set environment variables
#ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code (including .env)
COPY . .

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]