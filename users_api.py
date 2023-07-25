# Users Api
from flask import Flask, request, Response
from datetime import datetime
import argon2
app = Flask(__name__)

# Sample data
users=[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "created_at": "2023-07-16T08:00:00Z",
    "updated_at": "2023-07-16T08:30:00Z"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "created_at": "2023-07-15T09:15:00Z",
    "updated_at": "2023-07-16T09:45:00Z"
  }
]
# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return Response(str(users), status = 200, mimetype='application/json')

# Route to get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return Response(str(user), status = 200, mimetype='application/json')
    return Response(str({'message': 'User not found'}), status = 404, mimetype='application/json')

# Route to create a new user

#hashing password using argon2  : pip install argon2-cffi
@app.route('/users', methods=['POST'])
def create_user():
    new_user = {
        'id': len(users) + 1,
        'name': request.json['name'],
        'email': request.json['email'],
        'password':argon2.hash_password(request.json['password'].encode()),
        'created_at':str(datetime.now()),
        'updated_at':str(datetime.now()),
    }
    users.append(new_user)
    return Response(str(new_user), status = 201, mimetype='application/json')

# Route to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user['name'] = request.json['name']
        user['email'] = request.json['email']
        user['updated_at'] = str(datetime.now())
        return Response(str(user), status = 200, mimetype='application/json')
    return Response(str({'message': 'user not found'}), status = 404, mimetype='application/json')

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users.remove(user)
        return Response(str({'message': 'user deleted'}), status = 204, mimetype='application/json')
    return Response(str({'message': 'user not found'}), status = 404, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
