# Use a small official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy app code
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]

