import requests
import json


def call_products_api():
    response = requests.get("http://localhost:5000/items")
    print(response.status_code)
    print(response.text)
    product = {
        "id": 901,
        "order_id": 801,
        "product_id": 301,
        "quantity": 3,
        "price": 1000.99,
        "created_at": "2023-07-16T14:00:00Z",
        "updated_at": "2023-07-16T14:30:00Z"
    }
    response = requests.post("http://localhost:5000/items", json=product)
    print(response.status_code)
    print(response.text)

    response = requests.put("http://localhost:5000/items/3", json=product)
    print(response.status_code)
    print(response.text)

    response = requests.delete("http://localhost:5000/items/2")
    print(response.status_code)
    print(response.text)

    response = requests.get("http://localhost:5000/items")
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    call_products_api()
