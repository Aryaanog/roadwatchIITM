# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Install system dependencies required by OpenCV (cv2) and clear cache
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to leverage Docker caching layers
COPY ./requirements.txt /code/requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy all your backend application files into the container
COPY . .

# Set up global write permissions for the uploads directory (Hugging Face security rule)
RUN mkdir -p /code/uploads && chmod -R 777 /code/uploads

# Expose port 7860 (Hugging Face expects port 7860 by default)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]