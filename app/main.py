from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def dashboard():
    # Simulate real-time cloud service health checks
    services = [
        {"name": "Auth Service API", "status": "Operational", "latency": f"{random.randint(40, 120)}ms"},
        {"name": "Payment Gateway", "status": "Operational", "latency": f"{random.randint(80, 200)}ms"},
        {"name": "PostgreSQL RDS Database", "status": "Operational", "latency": f"{random.randint(10, 30)}ms"},
        {"name": "S3 Asset Storage", "status": "Degraded Performance", "latency": f"{random.randint(300, 500)}ms"}
    ]
    return render_template("index.html", services=services)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)