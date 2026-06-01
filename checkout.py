from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Checkout Service Running on EKS</h1>
    <p>Available API: /checkout</p>
    """

@app.route("/checkout", methods=["POST"])
def checkout():

    return jsonify({
        "status": "SUCCESS",
        "order_id": "ORD10001",
        "message": "Checkout Completed"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)