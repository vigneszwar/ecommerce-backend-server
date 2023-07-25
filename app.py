from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for payment transactions (for demonstration purposes)
payment_transactions = [
    {"id": 1, "amount": 100, "status": "paid"},
    {"id": 2, "amount": 50, "status": "pending"},
    {"id": 3, "amount": 200, "status": "paid"},
]
@app.route('/api/payments', methods=['GET'])
def get_payments():
    return jsonify(payment_transactions)
@app.route('/api/payments', methods=['POST'])
def add_payment():
    data = request.get_json()
    new_transaction = {
        "id": len(payment_transactions) + 1,
        "amount": data['amount'],
        "status": data['status'],
    }
    payment_transactions.append(new_transaction)
    return jsonify(new_transaction), 201
@app.route('/api/payments/<int:transaction_id>', methods=['PUT'])
def update_payment(transaction_id):
    data = request.get_json()
    for transaction in payment_transactions:
        if transaction['id'] == transaction_id:
            transaction['amount'] = data['amount']
            transaction['status'] = data['status']
            return jsonify(transaction)
    return jsonify({"message": "Transaction not found"}), 404
@app.route('/api/payments/<int:transaction_id>', methods=['DELETE'])
def delete_payment(transaction_id):
    global payment_transactions
    payment_transactions = [transaction for transaction in payment_transactions if transaction['id'] != transaction_id]
    return jsonify({"message": "Transaction deleted successfully"})
if __name__ == '__main__':
    app.run(debug=True)