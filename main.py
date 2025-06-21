from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def index():
    return "ChatGPT Relay Server is live!"

@app.route("/relay", methods=["POST"])
def relay():
    data = request.json
    message = data.get("message")
    if not message:
        return jsonify({"error": "Missing 'message'"}), 400

    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are the assistant responding to another AI."},
                {"role": "user", "content": message}
            ]
        )
        reply = resp.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
