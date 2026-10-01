# Use a lightweight official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ .

# Expose port 8080 to allow web traffic in/out of the container
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "main.py"]