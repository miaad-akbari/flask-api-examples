# First Stage: Build
FROM python:3.9-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Second Stage: Production
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the application's port
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
