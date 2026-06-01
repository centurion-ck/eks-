from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Telecom Payment Service</title>
    </head>
    <body>
        <h1>Payment Service Running on AWS EKS</h1>

        <h2>MuleSoft to Kong Migration Demo</h2>

        <p>Available APIs:</p>

        <ul>
            <li>/payment</li>
            <li>/health</li>
        </ul>

    </body>
    </html>
    """

@app.route("/payment")
def payment():
    return jsonify({
        "status": "SUCCESS",
        "service": "payment-service",
        "message": "Payment Processed Successfully"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)