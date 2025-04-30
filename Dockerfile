# Use a full base image with Java
FROM openjdk:11

# Install Linux tools + Python3 + pip + procps (for ps)
RUN apt-get update && \
    apt-get install -y python3 python3-pip procps wget curl lsb-release && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python libraries
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variables for Spark
ENV PYSPARK_PYTHON=python3

# Expose Streamlit default port
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "dashboard_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
