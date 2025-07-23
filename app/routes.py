from flask import jsonify
from flask import current_app as app

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = [
        {"name": "dinner", "value": 30.0},
        {"name": "supermarket", "value": 70.0}
    ]

    return jsonify(transactions)