from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "description": "High-performance laptop for professionals",
        "price": 1200.00,
        "brand_id": 1,
        "category_id": 2,
        "created_at": "2023-07-15T10:30:00Z",
        "updated_at": "2023-07-15T12:45:00Z",
        "reviews": []
    },
    {
        "id": 2,
        "name": "Smartphone",
        "description": "Latest smartphone with advanced features",
        "price": 800.00,
        "brand_id": 2,
        "category_id": 3,
        "created_at": "2023-07-15T11:15:00Z",
        "updated_at": "2023-07-15T11:30:00Z",
        "reviews": []
    },
    {
        "id": 3,
        "name": "TV",
        "description": "Ultra HD TV with a large display",
        "price": 1500.00,
        "brand_id": 3,
        "category_id": 4,
        "created_at": "2023-07-15T09:45:00Z",
        "updated_at": "2023-07-15T10:00:00Z",
        "reviews": []
    }
]

reviews = [
    {
        "id": 6001,
        "user_id": 101,
        "product_id": 1,
        "rating": 4.5,
        "title": "Great Product!",
        "comment": "I'm very satisfied with this product. It works perfectly.",
        "created_at": "2023-07-16T14:00:00Z",
        "updated_at": "2023-07-16T14:30:00Z"
    },
    {
        "id": 6002,
        "user_id": 102,
        "product_id": 2,
        "rating": 3.8,
        "title": "Decent Product",
        "comment": "The product is good, but I expected better performance.",
        "created_at": "2023-07-15T16:30:00Z",
        "updated_at": "2023-07-16T09:45:00Z"
    }
]

# Helper function to get reviews for a product by its ID
def get_reviews_for_product(product_id):
    return [review for review in reviews if review['product_id'] == product_id]

# Route to get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products), 200

# Route to get a specific product with its reviews
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_with_reviews(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        product_with_reviews = product.copy()
        product_with_reviews['reviews'] = get_reviews_for_product(product_id)
        return jsonify(product_with_reviews), 200
    return jsonify({'message': 'Product not found'}), 404

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = {
        'id': len(products) + 1,
        'name': request.json['name'],
        'description': request.json['description'],
        'price': request.json['price'],
        'brand_id': request.json['brand_id'],
        'category_id': request.json['category_id'],
        'created_at': request.json['created_at'],
        'updated_at': request.json['updated_at'],
        'reviews': []
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Route to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        product['name'] = request.json['name']
        product['description'] = request.json['description']
        product['price'] = request.json['price']
        product['brand_id'] = request.json['brand_id']
        product['category_id'] = request.json['category_id']
        product['updated_at'] = request.json['updated_at']
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

# Route to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        products.remove(product)
        return jsonify({'message': 'Product deleted'}), 204
    return jsonify({'message': 'Product not found'}), 404

# Route to add a review to a product
@app.route('/products/<int:product_id>/reviews', methods=['POST'])
def add_product_review(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        new_review = {
            'id': len(reviews) + 1,
            'user_id': request.json['user_id'],
            'product_id': product_id,
            'rating': request.json['rating'],
            'title': request.json['title'],
            'comment': request.json.get('comment', ''),
            'created_at': request.json['created_at'],
            'updated_at': request.json['updated_at']
        }
        reviews.append(new_review)
        product['reviews'].append(new_review)
        return jsonify(new_review), 201
    return jsonify({'message': 'Product not found'}), 404

# Route to delete a review from a product
@app.route('/products/<int:product_id>/reviews/<int:review_id>', methods=['DELETE'])
def delete_product_review(product_id, review_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        review = next((review for review in product['reviews'] if review['id'] == review_id), None)
        if review:
            product['reviews'].remove(review)
            reviews.remove(review)
            return jsonify({'message': 'Review deleted'}), 204
        return jsonify({'message': 'Review not found'}), 404
    return jsonify({'message': 'Product not found'}), 404

# Route to get all reviews
@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    return jsonify(reviews), 200

if __name__ == '__main__':
    app.run(debug=True)