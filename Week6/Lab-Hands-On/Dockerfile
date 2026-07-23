# Use a lightweight Python 3.10 base image.
FROM python:3.10-slim

# Enable immediate output in Python logs.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy dependency file and install packages.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container.
COPY . .

# Expose the Flask application port.
EXPOSE 5000

# Start the Flask application.
CMD ["python", "app.py"]