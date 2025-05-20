
# Use a slim Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside container
WORKDIR /app

# Copy your local files into the container
COPY . /app



# Install Python dependencies
RUN pip install -r requirements.txt

# Default command to run your script
CMD ["python", "main.py"]

