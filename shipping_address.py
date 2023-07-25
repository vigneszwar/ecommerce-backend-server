from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

shipping_addresses = [
    {
        "id": 1,
        "user_id": 1,
        "address_line1": "123 Main Street",
        "address_line2": "Apt 4",
        "city": "Cityville",
        "state": "Stateville",
        "country": "Countryland",
        "postal_code": "12345",
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
]


def find_shipping_address_by_id(shipping_address_id):
    for address in shipping_addresses:
        if address["id"] == shipping_address_id:
            return address
    return None


@app.route('/shipping_addresses', methods=['GET'])
def get_all_shipping_addresses():
    return jsonify(shipping_addresses)


@app.route('/shipping_addresses/<int:shipping_address_id>', methods=['GET'])
def get_shipping_address(shipping_address_id):
    address = find_shipping_address_by_id(shipping_address_id)
    if address:
        return jsonify(address)
    else:
        return jsonify({"message": "Shipping address not found"}), 404


@app.route('/shipping_addresses', methods=['POST'])
def create_shipping_address():
    data = request.get_json()
    new_address = {
        "id": len(shipping_addresses) + 1,
        "user_id": data["user_id"],
        "address_line1": data["address_line1"],
        "address_line2": data.get("address_line2", ""),
        "city": data["city"],
        "state": data["state"],
        "country": data["country"],
        "postal_code": data["postal_code"],
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    shipping_addresses.append(new_address)
    return jsonify(new_address), 201

@app.route('/shipping_addresses/<int:shipping_address_id>', methods=['PUT'])
def update_shipping_address(shipping_address_id):
    address = find_shipping_address_by_id(shipping_address_id)
    if not address:
        return jsonify({"message": "Shipping address not found"}), 404
    
    data = request.get_json()
    address["user_id"] = data["user_id"]
    address["address_line1"] = data["address_line1"]
    address["address_line2"] = data.get("address_line2", "")
    address["city"] = data["city"]
    address["state"] = data["state"]
    address["country"] = data["country"]
    address["postal_code"] = data["postal_code"]
    address["updated_at"] = datetime.now()
    
    return jsonify(address)

@app.route('/shipping_addresses/<int:shipping_address_id>', methods=['DELETE'])
def delete_shipping_address(shipping_address_id):
    address = find_shipping_address_by_id(shipping_address_id)
    if address:
        shipping_addresses.remove(address)
        return jsonify({"message": "Shipping address deleted successfully"}), 200
    else:
        return jsonify({"message": "Shipping address not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
