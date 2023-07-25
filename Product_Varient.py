from flask import Flask, request, jsonify
app = Flask(__name__)
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

# Get all products with variants
@app.route('/', methods=['GET'])
def home():
    return """Welome and test the api as follows :<br>
    To get all products with variants, send a GET request to http://localhost:5000/api/products.<br>
    To get a specific product by ID, send a GET request to http://localhost:5000/api/products/1.<br>
    To add a new variant to a product with ID 1, send a POST request to http://localhost:5000/api/products/1/variants with the variant data in the request body, like {'color' : 'Yellow', 'size': 'M', 'price': 27.99}.<br>
    To update a product variant, send a PUT request to http://localhost:5000/api/products/<product_id>/variants/<variant_id> with the updated variant data in the request body.<br>
    To delete a product variant, send a DELETE request to http://localhost:5000/api/products/<product_id>/variants/<variant_id>.<br>
    To delete a complete product, send a DELETE request to http://localhost:5000/api/products/<product_id>.<br>

    To get all variants with a specific color, you can send a GET request to http://localhost:5000/api/variants?color=Red.<br>
    OR<br>
    To get all variants with a specific color for Product 1, you can send a GET request to http://localhost:5000/api/products/1/variants?color=Red.<br>

    name: Filter variants by product name.<br>
    variant_id: Filter variants by variant ID.<br>
    color: Filter variants by color.<br>
    size: Filter variants by size.<br>
    price: Filter variants by price.<br>"""

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

# Add a new variant to a product
@app.route('/api/products/<int:product_id>/variants', methods=['POST'])
def add_variant(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    data = request.get_json()
    if not data or 'color' not in data or 'size' not in data or 'price' not in data:
        return jsonify({"message": "Missing required data"}), 400

    new_variant = {
        "id": data['id'] + 1,
        "name": data['name'],
        "description": data['discripition'],
        "price": data['price'],
        "brand_id": data['brand_id'],
        "category_id": data['category_id'],
        "created_at": data['created_at'],
        "updated_at": data['updated_at'],
    }
    product['variants'].append(new_variant)

    return jsonify(new_variant), 201

# Update a product variant
@app.route('/api/products/<int:product_id>/variants/<int:variant_id>', methods=['PUT'])
def update_variant(product_id, variant_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    variant = next((v for v in product['variants'] if v['id'] == variant_id), None)
    if not variant:
        return jsonify({"message": "Variant not found"}), 404
    
    data = request.get_json()
    if not data or 'name' not in data or 'descripition' not in data or 'price' not in data or 'brand_id' not in data or 'category_id' not in data or 'created_at' not in data or 'updated_at' not in data:
        return jsonify({"message": "Missing required data"}), 400

    variant['name'] = data['name']
    variant['description'] = data['discription']
    variant['price'] = data['price']
    variant['brand_id'] = data['brand_id']
    variant['category_id'] = data['category_id']
    variant['created_at'] = data['created_at']
    variant['updated_at'] = data['updated_at']

    return jsonify(variant)

# Delete a product variant
@app.route('/api/products/<int:product_id>/variants/<int:variant_id>', methods=['DELETE'])
def delete_variant(product_id, variant_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    variant = next((v for v in product['variants'] if v['id'] == variant_id), None)
    if not variant:
        return jsonify({"message": "Variant not found"}), 404
    
    product['variants'].remove(variant)
    return jsonify({"message": "Variant deleted successfully"})

# Delete a complete product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    products.remove(product)
    return jsonify({"message": "Product deleted successfully"})

# Get product variants by name, variant ID, color, size, or price
@app.route('/api/variants', methods=['GET'])
def get_variants():
    product_name = request.args.get('name')
    variant_id = request.args.get('variant_id', type=int)
    name = request.args.get('name')
    description = request.args.get('description')
    price = request.args.get('price', type=float)
    brand_id = request.args.get('brand_id', type=int)
    category_id = request.args.get('category_id', type=int)
    created_at = request.args.get('created_at', type=datetime.datetime)
    update_product = request.args.get('update_product', type=datetime.datetime)
    
    filtered_variants = []
    for product in products:
        if product_name and product['name'] != product_name:
            continue
        
        for variant in product['variants']:
            if (variant_id is not None and variant['id'] != variant_id) or \
               (name and variant['name'] != name) or \
               (description and variant['description'] != description) or \
               (price is not None and variant['price'] != price):
                continue
            
            filtered_variants.append({
                "product_name": product['name'],
                "variant_id": variant['id'],
                "color": variant['color'],
                "size": variant['size'],
                "price": variant['price'],
            })

    return jsonify(filtered_variants)


# Get product variants by name, variant ID, color, size, or price for a specific product
@app.route('/api/products/<int:product_id>/variants', methods=['GET'])
def get_product_variants(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    name = request.args.get('name')
    variant_id = request.args.get('variant_id', type=int)
    color = request.args.get('color')
    size = request.args.get('size')
    price = request.args.get('price', type=float)
    
    filtered_variants = []
    for variant in product['variants']:
        if (name and product['name'] != name) or \
           (variant_id is not None and variant['id'] != variant_id) or \
           (color and variant['color'] != color) or \
           (size and variant['size'] != size) or \
           (price is not None and variant['price'] != price):
            continue
        
        filtered_variants.append({
            "product_name": product['name'],
            "variant_id": variant['id'],
            "color": variant['description'],
            "size": variant['size'],
            "price": variant['price'],
            "category_id": variant['category_id'],
            "created_at": variant['created_at'],
            "updated_at" : variant['updated_at'],
        })

    return jsonify(filtered_variants)


# Add a new product
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or 'name' not in data or 'variants' not in data or 'descripition' not in data or 'price' not in data or 'brand_id' not in data or 'category_id' not in data or 'created_at' not in data or 'updated_at' not in data:
        return jsonify({"message": "Missing required data"}), 400

    new_product = {
        "id": len(products) + 1,
        "name": data['name'],
        "variants": data['variants'],
    }
    products.append(new_product)

    return jsonify(new_product), 201

# Update a complete product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'variants' not in data:
        return jsonify({"message": "Missing required data"}), 400

    product['name'] = data['name']
    product['variants'] = data['variants']

    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)