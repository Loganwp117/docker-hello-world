from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from a Dockerized app!"

if __name__ == "__main__":
    # 0.0.0.0 = listen on all interfaces so Docker can map the port
    app.run(host="0.0.0.0", port=5000)

