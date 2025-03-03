# Use lightweight base image
FROM python:3.9-slim

# Set working directory
WORKDIR /home

# Copy project files into the container
COPY scripts.py /home/
COPY data /home/data/

# Install required packages
RUN pip install --no-cache-dir requests

# Run the script automatically
CMD ["python", "scripts.py"]
