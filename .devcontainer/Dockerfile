# Use the alpine base image
FROM mcr.microsoft.com/devcontainers/base:alpine

# Install Python and other necessary packages
RUN apk add --no-cache python3 py3-pip

# Set the working directory
WORKDIR /workspaces/Ibotta-Offer-Recommendation-Engine1

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000

# Define default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
