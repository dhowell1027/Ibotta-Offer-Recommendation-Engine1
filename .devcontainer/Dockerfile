# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install any necessary system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Install pip and necessary Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the Kaggle API credentials directory exists and set proper permissions
RUN mkdir -p /root/.kaggle && chmod 600 /root/.kaggle

# Expose port 8000 to be used by FastAPI
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
