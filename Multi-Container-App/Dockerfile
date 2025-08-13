FROM python:3.8-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y gcc python3-dev

# Copy your app
COPY . .

# Install Python packages
RUN pip install --no-cache-dir flask redis

EXPOSE 5001

CMD ["python", "app.py"]
