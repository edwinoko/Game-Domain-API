FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install Python, pip, and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements.txt if it exists
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --upgrade pip && \
    if [ -f requirements.txt ]; then pip3 install -r requirements.txt; fi

# Copy the rest of the application code
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Default command to run FastAPI app (update main:app if needed)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]