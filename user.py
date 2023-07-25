import sqlite3
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database schema (create the 'users' table)
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        ''')
        conn.commit()


# Initialize the database when the app starts
init_db()

# Routes for CRUD operations
@app.route('/users', methods=['GET'])
def get_users():
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM users')
        users = [dict(row) for row in cursor.fetchall()]
        return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    with get_db_connection() as conn:
        cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify(dict(user))
        return jsonify({"message": "User not found"}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"message": "Name and email fields are required"}), 400

    current_time = datetime.datetime.utcnow().isoformat()

    with get_db_connection() as conn:
        cursor = conn.execute('INSERT INTO users (name, email, created_at, updated_at) VALUES (?, ?, ?, ?)',
                              (name, email, current_time, current_time))
        conn.commit()

        user_id = cursor.lastrowid
        new_user = {"id": user_id, "name": name, "email": email, "created_at": current_time, "updated_at": current_time}
        return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"message": "Name and email fields are required"}), 400

    current_time = datetime.datetime.utcnow().isoformat()

    with get_db_connection() as conn:
        conn.execute('UPDATE users SET name = ?, email = ?, updated_at = ? WHERE id = ?', (name, email, current_time, user_id))
        conn.commit()

    return jsonify({"message": "User updated successfully"}), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()

    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
