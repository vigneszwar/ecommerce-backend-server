from flask import Flask, request, Response
from datetime import datetime


app = Flask(__name__)

# Sample data
suppliers =[
  {
    "id": 10001,
    "name": "ABC Electronics",
    "email": "abc@example.com",
    "created_at": "2023-07-16T14:00:00Z",
    "updated_at": "2023-07-16T14:30:00Z"
  },
  {
    "id": 10002,
    "name": "XYZ Supplies",
    "email": "xyz@example.com",
    "created_at": "2023-07-15T16:30:00Z",
    "updated_at": "2023-07-16T09:45:00Z"
  }
]



# Route to get all suppliers
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    return Response(str(suppliers), status = 200, mimetype='application/json')



# Route to get a specific supply
@app.route('/suppliers/<int:supplier_id>', methods=['GET'])
def get_supply(supplier_id):
    supply = next((supply for supply in suppliers if supply['id'] == supplier_id), None)
    if supply:
        return Response(str(supply), status = 200, mimetype='application/json')
    return Response(str({'message': 'supply not found'}), status = 404, mimetype='application/json')



# Route to create a new supply
@app.route('/suppliers', methods=['POST'])
def create_supply():
    date = datetime.now()
    new_supply = {
        'id': 10000+ len(suppliers) + 1,
        'name': request.json['name'],
        'email': request.json['email'],
        'created_at': str(date),
        'updated_at': str(date)
    }
    suppliers.append(new_supply)
    return Response(str(new_supply), status = 201, mimetype='application/json')



# Route to update an existing supply
@app.route('/suppliers/<int:supplier_id>', methods=['PUT'])
def update_supply(supplier_id):
    date = datetime.now()
    supply = next((supply for supply in suppliers if supply['id'] == supplier_id), None)
    if supply:
        supply['name'] = request.json['name']
        supply['email']= request.json['email'],
        supply['updated_at']= str(date)
        return Response(str(supply), status = 200, mimetype='application/json')
    return Response(str({'message': 'supply not found'}), status = 404, mimetype='application/json')



# Route to delete a supply
@app.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
def delete_supply(supplier_id):
    supply = next((supply for supply in suppliers if supply['id'] == supplier_id), None)
    if supply:
        suppliers.remove(supply)
        return Response(str({'message': 'supply deleted'}), status = 204, mimetype='application/json')
    return Response(str({'message': 'supply not found'}), status = 404, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)
