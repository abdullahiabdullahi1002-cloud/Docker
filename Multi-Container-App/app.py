from flask import Flask, render_template
import redis
import os

app = Flask(__name__)

# Redis connection using environment variables
r = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    decode_responses=True
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/count')
def count():
    visits = r.incr("visits")  # increment the counter
    return render_template('count.html', count=visits)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
