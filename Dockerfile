# Use the official Python image from Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8080

# Set the command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
