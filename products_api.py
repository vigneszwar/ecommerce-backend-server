from flask import Flask, request, Response

app = Flask(__name__)

# Sample data
products = [
  {
    "id": 1,
    "name": "Electronics",
    "description": "Electronic devices and gadgets",
    "parent_id": null,
    "created_at": "2023-07-14T12:30:00Z",
    "updated_at": "2023-07-14T12:30:00Z"
  },
  {
    "id": 2,
    "name": "Laptops",
    "description": "Various laptop models",
    "parent_id": 1,
    "created_at": "2023-07-14T12:45:00Z",
    "updated_at": "2023-07-14T12:45:00Z"
  },
  {
    "id": 3,
    "name": "Smartphones",
    "description": "Smartphone devices",
    "parent_id": 1,
    "created_at": "2023-07-14T12:50:00Z",
    "updated_at": "2023-07-14T12:50:00Z"
  },
  {
    "id": 4,
    "name": "TVs",
    "description": "Television sets",
    "parent_id": 1,
    "created_at": "2023-07-14T13:00:00Z",
    "updated_at": "2023-07-14T13:00:00Z"
  }
]

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return Response(str(products), status = 200, mimetype='application/json')

# Route to get a specific product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return Response(str(product), status = 200, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'id': len(products) + 1,
        'name': request.json['name'],
        'price': request.json['price']
    }
    products.append(new_product)
    return Response(str(new_product), status = 201, mimetype='application/json')

# Route to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        product['name'] = request.json['name']
        product['price'] = request.json['price']
        return Response(str(product), status = 200, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        products.remove(product)
        return Response(str({'message': 'Product deleted'}), status = 204, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
