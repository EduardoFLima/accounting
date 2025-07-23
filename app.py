from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    
    transactions = [
        { "name": "dinner", "value": 30.0 },
        { "name": "supermarkets", "value": 70.0 }
    ]
    
    return jsonify (transactions)

if __name__ == '__main__':
    app.run(debug=True)
