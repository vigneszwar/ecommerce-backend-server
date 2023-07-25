from flask import Flask, request,jsonify

app = Flask(__name__)

# product data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop for professionals",
        "price": 1200.00,
        "brand_id": 1,
        "category_id": 2,
        "created_at": "2023-07-15T10:30:00Z",
        "updated_at": "2023-07-15T12:45:00Z"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "description": "Latest smartphone with advanced features",
        "price": 800.00,
        "brand_id": 2,
        "category_id": 3,
        "created_at": "2023-07-15T11:15:00Z",
        "updated_at": "2023-07-15T11:30:00Z"
    },
    {
        "id": 3,
        "name": "TV",
        "description": "Ultra HD TV with a large display",
        "price": 1500.00,
        "brand_id": 3,
        "category_id": 4,
        "created_at": "2023-07-15T09:45:00Z",
        "updated_at": "2023-07-15T10:00:00Z"
    }
]

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404
    
    # Route to add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"message": "Bad request"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "price": data['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Route to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"message": "Bad request"}), 400

    product["name"] = data['name']
    product["price"] = data['price']
    return jsonify(product)

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [item for item in products if item["id"] != product_id]
    return jsonify({"message": "Product deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)