from flask import request, jsonify
from flask import current_app as app
from . import db
from .models import Transaction


@app.route("/health")
def health():
    return "OK", 200


@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()

    transaction = Transaction(
        type=data.get('type'),
        amount=data.get('amount'),
        description=data.get('description'),
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        'id': transaction.id,
        'type': transaction.type,
        'amount': transaction.amount,
        'description': transaction.description,
        'date': transaction.date.isoformat()
    }), 201


@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()

    return jsonify([{
        'id': transaction.id,
        'type': transaction.type,
        'amount': transaction.amount,
        'description': transaction.description,
        'date': transaction.date.isoformat()
    } for transaction in transactions])
