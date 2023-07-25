from flask import Flask, request, Response

app = Flask(__name__)

# Sample data
order_items = [
    {
        "id": 801,
        "order_id": 701,
        "product_id": 201,
        "quantity": 2,
        "price": 999.99,
        "created_at": "2023-07-16T14:00:00Z",
        "updated_at": "2023-07-16T14:30:00Z"
    },
    {
        "id": 802,
        "order_id": 701,
        "product_id": 202,
        "quantity": 1,
        "price": 799.99,
        "created_at": "2023-07-16T14:15:00Z",
        "updated_at": "2023-07-16T14:15:00Z"
    },
    {
        "id": 803,
        "order_id": 702,
        "product_id": 201,
        "quantity": 3,
        "price": 999.99,
        "created_at": "2023-07-15T16:30:00Z",
        "updated_at": "2023-07-15T16:30:00Z"
    }
]


# Route to get all products
@app.route('/items', methods=['GET'])
def get_products():
    return Response(str(order_items), status=200, mimetype='application/json')


# Route to get a specific product
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in order_items if item['id'] == item_id), None)
    if item:
        return Response(str(item), status=200, mimetype='application/json')
    return Response(str({'message': 'Item not found'}), status=404, mimetype='application/json')


# Route to create a new product
@app.route('/items', methods=['POST'])
def create_item():
    new_item = {
        'id': len(order_items) + 1,
        'order_id': request.json['order_id'],
        'product_id': request.json['product_id'],
        'quantity': request.json['quantity'],
        'price': request.json['price'],
        'created_at': request.json['created_at'],
        'updated_at': request.json['updated_at']
    }
    order_items.append(new_item)
    return Response(str(new_item), status=201, mimetype='application/json')


# Route to update an existing product
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_product(item_id):
    item = next((item for item in order_items if item['id'] == item_id), None)
    if item:
        item['order_id'] = request.json['order_id']
        item['product_id'] = request.json['product_id']
        item['quantity'] = request.json['quantity']
        item['price'] = request.json['price']
        item['created_at'] = request.json['created_at']
        item['updated_at'] = request.json['updated_at']
        return Response(str(item), status=200, mimetype='application/json')
    return Response(str({'message': 'Item not found'}), status=404, mimetype='application/json')


# Route to delete a product
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_product(item_id):
    item = next((item for item in order_items if item['id'] == item_id), None)
    if item:
        order_items.remove(item)
        return Response(str({'message': 'Item will be deleted'}), status=204, mimetype='application/json')
    return Response(str({'message': 'Order item not found'}), status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)

# This is order_client file
#
# import requests
# import json
#
#
# def call_products_api():
#     response = requests.get("http://localhost:5000/items")
#     print(response.status_code)
#     print(response.text)
#     product = {
#         "id": 901,
#         "order_id": 801,
#         "product_id": 301,
#         "quantity": 3,
#         "price": 1000.99,
#         "created_at": "2023-07-16T14:00:00Z",
#         "updated_at": "2023-07-16T14:30:00Z"
#     }
#     response = requests.post("http://localhost:5000/items", json=product)
#     print(response.status_code)
#     print(response.text)
#
#     response = requests.put("http://localhost:5000/items/3", json=product)
#     print(response.status_code)
#     print(response.text)
#
#     response = requests.delete("http://localhost:5000/items/2")
#     print(response.status_code)
#     print(response.text)
#
#     response = requests.get("http://localhost:5000/items")
#     print(response.status_code)
#     print(response.text)
#
#
