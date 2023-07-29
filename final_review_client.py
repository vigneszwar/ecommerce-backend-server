import requests
import json

def get_products():
    response = requests.get("http://localhost:5000/products")
    print(response.status_code)
    print(response.json())

def get_product(product_id):
    response = requests.get(f"http://localhost:5000/products/{product_id}")
    print(response.status_code)
    print(response.json())

def create_product(name, description, price, brand_id, category_id, created_at, updated_at):
    product = {
        'name': name,
        'description': description,
        'price': price,
        'brand_id': brand_id,
        'category_id': category_id,
        'created_at': created_at,
        'updated_at': updated_at
    }
    response = requests.post("http://localhost:5000/products", json=product)
    print(response.status_code)
    print(response.json())

def update_product(product_id, name, description, price, brand_id, category_id, updated_at):
    product = {
        'name': name,
        'description': description,
        'price': price,
        'brand_id': brand_id,
        'category_id': category_id,
        'updated_at': updated_at
    }
    response = requests.put(f"http://localhost:5000/products/{product_id}", json=product)
    print(response.status_code)
    print(response.json())

def delete_product(product_id):
    response = requests.delete(f"http://localhost:5000/products/{product_id}")
    print(response.status_code)
    print(response.json())


def add_product_review(product_id, user_id, rating, title, comment, created_at, updated_at):
    review = {
        'user_id': user_id,
        'rating': rating,
        'title': title,
        'comment': comment,
        'created_at': created_at,
        'updated_at': updated_at
    }
    response = requests.post(f"http://localhost:5000/products/{product_id}/reviews", json=review)
    print(response.status_code)
    print(response.json())

def delete_product_review(product_id, review_id):
    response = requests.delete(f"http://localhost:5000/products/{product_id}/reviews/{review_id}")
    print(response.status_code)
    print(response.json())

if __name__ == "__main__":
    get_products()
    get_product(2)
    create_product("New Product", "A new product description.", 25.99, 1, 2, "2023-07-18T10:00:00Z", "2023-07-18T10:00:00Z")
    update_product(2, "Updated Product", "Updated product description.", 29.99, 2, 3, "2023-07-18T11:30:00Z")
    delete_product(1)
    # get_product_reviews(2)
    add_product_review(2, 101, 4.5, "Great product!", "I'm very satisfied.", "2023-07-18T14:00:00Z", "2023-07-18T14:00:00Z")
    delete_product_review(2, 6001)