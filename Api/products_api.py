from flask import Flask, request, Response

app = Flask(__name__)

# Sample data
products = [
    {
        'id': 1,
        'name': 'Product 1',
        'price': 10.99
    },
    {
        'id': 2,
        'name': 'Product 2',
        'price': 19.99
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
