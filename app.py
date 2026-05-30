from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Python backend running on EKS!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)