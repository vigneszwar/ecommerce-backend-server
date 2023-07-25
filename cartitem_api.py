from flask import Flask, request, Response

app = Flask(__name__)

# Sample data
cartitems = [
  {
    "id": 1,
    "user_id": 101,
    "product_id": 201,
    "quantity": 2,
    "created_at": "2023-07-16T16:00:00Z",
    "updated_at": "2023-07-16T16:00:00Z"
  },
  {
    "id": 2,
    "user_id": 101,
    "product_id": 202,
    "quantity": 1,
    "created_at": "2023-07-16T16:30:00Z",
    "updated_at": "2023-07-16T16:30:00Z"
  },
  {
    "id": 3,
    "user_id": 102,
    "product_id": 201,
    "quantity": 3,
    "created_at": "2023-07-16T17:00:00Z",
    "updated_at": "2023-07-16T17:00:00Z"
  }
]

# Route to get all cartitems
@app.route('/cartitems', methods=['GET'])
def get_cartitems():
    return Response(str(cartitems), status = 200, mimetype='application/json')

# Route to get a specific cartiem
@app.route('/cartitems/<int:cartitem_id>', methods=['GET'])
def cartitem_id(cartitem_id):
    cartitem = next((cartitem for cartitem in cartitems if cartitem['id'] == cartitem_id), None)
    if cartitem:
        return Response(str(cartitem), status = 200, mimetype='application/json')
    return Response(str('cartitem not found'), status = 404, mimetype='application/json')

# Route to add a new cartitems
@app.route('/cartitems', methods=['POST'])
def add_cartitems():
    new_cartitem = {
        'id': len(cartitems) + 1,
        'user_id': request.json['user_id'],
        'created_at': request.json['created_at'],
    }
    cartitems.append(new_cartitem)
    return Response(str(new_cartitem), status = 201, mimetype='application/json')

# Route to update an existing cartitem
@app.route('/cartitems/<int:cartitem_id>', methods=['PUT'])
def update_cartitem(cartitem_id):
    cartitem = next((cartitem for cartitem in cartitems if cartitem['id'] == cartitem_id), None)
    if cartitem:
        cartitem['user_id'] = request.json['user_id']
        cartitem['updated_at'] = request.json['updated_at']
        return Response(str(cartitem), status = 200, mimetype='application/json')
    return Response(str('Cartitem not found'), status = 404, mimetype='application/json')

# Route to delete a Cartitem
@app.route('/cartitems/<int:cartitem_id>', methods=['DELETE'])
def delete_cartitem(cartitem_id):
    cartitem = next((cartitem for cartitem in cartitems if cartitem['id'] == cartitem_id), None)
    if cartitem:
        cartitems.remove(cartitem)
        return Response(str('Cartitem deleted'), status = 204, mimetype='application/json')
    return Response(str('Cartitem not found'), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
