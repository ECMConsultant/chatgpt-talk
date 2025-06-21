from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Server is live!'

@app.route('/relay', methods=['POST'])
def relay():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        target_ai = data.get("target_ai")
        message = data.get("message")

        if not target_ai or not message:
            return jsonify({"error": "Both 'target_ai' and 'message' fields are required"}), 400

        response = f"{target_ai} says: 'Sure, here's my take on that: {message[::-1]}'"
        return jsonify({"reply": response})

    except Exception as e:
        return jsonify({"error": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)