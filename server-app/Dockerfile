# Use a base image with Python and CUDA if GPU processing is required
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY . /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

# Command to run the application
CMD ["python", "model_server.py"]
