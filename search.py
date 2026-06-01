from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Search Service Running on EKS</h1>
    <p>Available API: /products</p>
    """

@app.route("/products")
def products():

    data = [
        {
            "id": 1,
            "name": "iPhone 16",
            "price": 85000
        },
        {
            "id": 2,
            "name": "Samsung S25",
            "price": 80000
        },
        {
            "id": 3,
            "name": "OnePlus 15",
            "price": 50000
        }
    ]

    return jsonify(data)

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)