from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Checkout Service Running"

@app.route("/checkout", methods=["POST"])
def checkout():

    return jsonify({
        "status": "SUCCESS",
        "order_id": "ORD-1001"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)