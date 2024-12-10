FROM python:3.9-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
