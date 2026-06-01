from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Search Service Running"

@app.route("/products")
def products():
    return jsonify([
        {
            "id": 1,
            "name": "iPhone 16",
            "price": 85000
        },
        {
            "id": 2,
            "name": "Samsung S25",
            "price": 75000
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)