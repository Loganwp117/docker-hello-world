from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis container (hostname = redis)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def hello():
    # Increment a counter in Redis
    count = r.incr("hits")
    return f"Hello from Docker! This page has been visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

