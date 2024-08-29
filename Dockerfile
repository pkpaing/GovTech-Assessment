# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define an entry point to use CMD to pass arguments
ENTRYPOINT ["python", "main.py"]
