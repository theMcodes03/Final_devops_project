import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health_check():
    return jsonify({"status": "OK", "message": "Healthy"})

@app.route("/api/hello")
def api_hello():
    return jsonify({"message": "Hello from API!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
