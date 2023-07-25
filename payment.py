from flask import Flask, jsonify, request

app = Flask(__name__)
# Author : Saurav Kumar Singh
# data for payment transactions (for demonstration purposes)
payment_transactions = [
   {
    "id": 1001,
    "order_id": 701,
    "amount": 2999.70,
    "currency": "USD",
    "status": "completed",
    "transaction_id": 123456,
    "created_at": "2023-07-16T14:00:00Z",
    "updated_at": "2023-07-16T14:30:00Z"
  },
  {
    "id": 1002,
    "order_id": 702,
    "amount": 1599.95,
    "currency": "EUR",
    "status": "completed",
    "transaction_id": 789018,
    "created_at": "2023-07-15T16:30:00Z",
    "updated_at": "2023-07-16T09:45:00Z"
  },
   {
    "id": 1002,
    "order_id": 702,
    "amount": 1599.95,
    "currency": "EUR",
    "status": "completed",
    "transaction_id": 789082,
    "created_at": "2023-07-15T16:30:00Z",
    "updated_at": "2023-07-16T09:45:00Z"
  },
   {
    "id": 1004,
    "order_id": 703,
    "amount": 159.95,
    "currency": "EUR",
    "status": "completed",
    "transaction_id": 789016,
    "created_at": "2023-07-15T16:30:00Z",
    "updated_at": "2023-07-16T09:45:00Z"
  }
  
  
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
