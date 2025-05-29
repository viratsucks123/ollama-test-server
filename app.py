from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/rogue/xxx", methods=["GET"])
def malicious_model():
    return jsonify({"status": "Fake Model Pulled", "info": "You hit the controlled test server"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
