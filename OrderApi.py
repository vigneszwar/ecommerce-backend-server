from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (temporary, replace this with a database later)
orders = [
    {
        "id": 701,
        "user_id": 101,
        "status": "completed",
        "total_amount": 2999.70,
        "created_at": "2023-07-16T14:00:00Z",
        "updated_at": "2023-07-16T14:30:00Z"
    },
    {
        "id": 702,
        "user_id": 102,
        "status": "pending",
        "total_amount": 1599.95,
        "created_at": "2023-07-15T16:30:00Z",
        "updated_at": "2023-07-16T09:45:00Z"
    }
]

# Get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

# Get a specific order by ID
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({'message': 'Order not found'}), 404

# Create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    new_order = {
        "id": data['id'],
        "user_id": data['user_id'],
        "status": data['status'],
        "total_amount": data['total_amount'],
        "created_at": data['created_at'],
        "updated_at": data['updated_at']
    }
    orders.append(new_order)
    return jsonify(new_order), 201

# Update an existing order
@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        order.update(data)
        return jsonify(order)
    else:
        return jsonify({'message': 'Order not found'}), 404

# Delete an order
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [order for order in orders if order['id'] != order_id]
    return jsonify({'message': 'Order deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
