import requests
import json

def call_products_api():
    response = requests.get("http://localhost:5000/categories/3")
    print(response.status_code)
    print(response.text)
    # product = {
    #     'name': 'Product 3',
    #     'price': 100.99
    # }
    # response = requests.post("http://localhost:5000/products", json = product)
    # print(response.status_code)
    # print(response.text)

if __name__ == "__main__":
    call_products_api()