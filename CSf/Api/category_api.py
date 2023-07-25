from flask import Flask, request, Response
from datetime import datetime
app = Flask(__name__)

# Sample data
categories = [
    {
        'id': 1,
        'name': 'Electronics',
        'description':'Electronic devices and gadgets',
        'parent_id': None,
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': None
    },
    {
        'id': 2,
        'name': 'Laptops',
        'description':'Various laptop models',
        'parent_id':1,
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': None
    },
    {
        'id': 3,
        'name': 'Smartphones',
        'description':'Smartphones devices',
        'parent_id': None,
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': None
    },
    {
        'id': 4,
        'name': 'TVs',
        'description':'Television sets',
        'parent_id': None,
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': None
    },
]

# Route to get all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    return Response(str(categories), status = 200, mimetype='application/json')


# Route to get a specific category
@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    if category:
        return Response(str(category), status = 200, mimetype='application/json')
    return Response(str({'message': 'category not found'}), status = 404, mimetype='application/json')


# Route to create a new category
@app.route('/categories', methods=['POST'])
def create_category():
    new_category = {
        'id': len(categories) + 1,
        'name': request.json['name'],
        'description': request.json['description'],
        'parent_id': request.json['parent_id'],
        'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': None
    }
    categories.append(new_category)
    return Response(str(new_category), status = 201, mimetype='application/json')


# Route to update an existing category
@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    if category:
        category['name'] = request.json['name']
        category['description'] = request.json['description']
        category['parent_id'] = request.json['parent_id']
        category['created_at'] = categories[category_id-1]['created_at']
        category['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return Response(str(category), status = 200, mimetype='application/json')
    return Response(str({'message': 'category not found'}), status = 404, mimetype='application/json')


# Route to delete a category
@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    if category:
        categories.remove(category)
        return Response(str({'message': 'category deleted'}), status = 204, mimetype='application/json')
    return Response(str({'message': 'category not found'}), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
    
    




