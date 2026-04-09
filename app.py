from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "SpamSense API Running"

@app.route('/api/classify', methods=['POST'])
def classify():
    data = request.json
    text = data.get("text", "")

    spam_keywords = ["win", "free", "money", "urgent"]
    score = sum(1 for k in spam_keywords if k in text.lower())

    spam_prob = min(95, score * 20)
    ham_prob = 100 - spam_prob

    return jsonify({
        "is_spam": spam_prob > 50,
        "spam_probability": spam_prob,
        "ham_probability": ham_prob,
        "confidence": max(spam_prob, ham_prob),
        "confidence_label": "High",
        "signals": [],
        "model_used": "Basic Model"
    })

if __name__ == '__main__':
    app.run(debug=True)
