from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample initial product data
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 19.99}
]

# Routes for CRUD operations
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404


# Route for creating a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if 'name' not in data or 'price' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "price": data['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Route for updating an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    if 'name' in data:
        product['name'] = data['name']
    if 'price' in data:
        product['price'] = data['price']
    
    return jsonify(product)

# Route for deleting a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [item for item in products if item["id"] != product_id]
    return jsonify({"message": "Product deleted"}), 200


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
