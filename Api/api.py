from flask import Flask, jsonify, request, Response

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
    return jsonify(products)


    
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return Response(str(product), status = 200, mimetype='application/json')
    return Response(str({'message': 'Product not found'}), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)