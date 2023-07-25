from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25},
]

# Endpoint to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Web page to display the user data
@app.route('/')
def index():
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
