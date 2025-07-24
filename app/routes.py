from flask import jsonify
from flask import current_app as app

@app.route("/health")
def health():
    return "OK", 200

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = [
        {"name": "dinner", "amount": 30.0},
        {"name": "supermarket", "amount": 70.0}
    ]

    return jsonify(transactions)