from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "AI Relay Server is live!"

@app.route("/relay", methods=["POST"])
def relay():
    data = request.json

    # Extract fields
    target_ai = data.get("target_ai", "another AI")
    message = data.get("message")

    if not message:
        return jsonify({"error": "Missing 'message' in request"}), 400

    # Simulated response logic (for now)
    reply = f"{target_ai} says: 'Sure, here's my take: {message[::-1]}'"

    return jsonify({"response": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
