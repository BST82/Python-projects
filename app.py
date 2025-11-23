from flask import Flask
from pymongo import MongoClient
from routes.shortener import shortener_bp

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["local"]

app.config["DB"] = db

app.register_blueprint(shortener_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "URL Shortener API is Running..."}

if __name__ == "__main__":
    app.run(debug=True)
