from flask import Flask, request, Response

app = Flask(__name__)

products = [
  {
    "id": 1,
    "product_id": 1,
    "name": "Color: Red",
    "price": 1300.00,
    "created_at": "2023-07-16T08:30:00Z",
    "updated_at": "2023-07-16T09:00:00Z"
  },
  {
    "id": 2,
    "product_id": 1,
    "name": "Color: Blue",
    "price": 1350.00,
    "created_at": "2023-07-16T09:15:00Z",
    "updated_at": "2023-07-16T09:15:00Z"
  },
  {
    "id": 3,
    "product_id": 2,
    "name": "Size: 64GB",
    "price": 800.00,
    "created_at": "2023-07-16T10:30:00Z",
    "updated_at": "2023-07-16T10:45:00Z"
  }
]

@app.route('/products', methods=['GET'])
def get_products():
    return Response(str(products), status = 200, mimetype='application/json')


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return Response(str(product), status = 200, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')


@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'id': len(products) + 1,
        'name': request.json['name'],
        'price': request.json['price'],
        'product_id': request.json['product_id'],
        'created_at': request.json['created_at'],
        'updated_at': request.json['updated_at']
    }
    products.append(new_product)
    return Response(str(new_product), status = 201, mimetype='application/json')

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        product['name'] = request.json['name']
        product['price'] = request.json['price']
        product['product_id'] = request.json['product_id']
        product['created_at'] = request.json['created_at']
        product['updated_at'] = request.json['updated_at']
        return Response(str(product), status = 200, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        products.remove(product)
        return Response(str({'message': 'Product deleted'}), status = 204, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
