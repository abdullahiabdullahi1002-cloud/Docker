# app.py
from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection settings from environment variables
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(
    host=redis_host,
    port=redis_port,
    decode_responses=True
)

@app.route('/')
def home():
    return "Welcome to the Flask + Redis app!"

@app.route('/count')
def count():
    visits = r.incr("visits")
    return f"Visit count: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
