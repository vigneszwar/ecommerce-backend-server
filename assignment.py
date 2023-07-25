from flask import Flask, request, jsonify
app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane.smith@example.com"
    }
]

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# Get a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"message": "Invalid data"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    user = next((user for user in users if user["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"message": "Invalid data"}), 400

    user["name"] = data["name"]
    user["email"] = data["email"]
    return jsonify(user)

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)

