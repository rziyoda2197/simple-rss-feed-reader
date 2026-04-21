import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock API endpointlari
api_endpoints = {
    '/users': {
        'GET': lambda: json.dumps([{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]),
        'POST': lambda: json.dumps({'id': 3, 'name': 'New User'})
    },
    '/products': {
        'GET': lambda: json.dumps([{'id': 1, 'name': 'Product 1'}, {'id': 2, 'name': 'Product 2'}]),
        'POST': lambda: json.dumps({'id': 3, 'name': 'New Product'})
    }
}

# API endpointlar uchun funksiyalar
def get_users():
    return api_endpoints['/users']['GET']()

def post_users():
    return api_endpoints['/users']['POST']()

def get_products():
    return api_endpoints['/products']['GET']()

def post_products():
    return api_endpoints['/products']['POST']()

# API endpointlar uchun routlar
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return get_users(), 200
    elif request.method == 'POST':
        return post_users(), 201

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return get_products(), 200
    elif request.method == 'POST':
        return post_products(), 201

if __name__ == '__main__':
    app.run(debug=True)
```

Kodni ishga tushirish uchun quyidagilarni amalga oshiring:

1. Kodni `server.py` nomli faylga saqlang.
2. Kompyuterida Python ni o'rnatgan bo'lsangiz, quyidagilarni amalga oshiring:
   ```bash
python server.py
```
3. API endpointlariga murojaat qilish uchun quyidagilarni amalga oshiring:
   ```bash
curl http://localhost:5000/users
curl -X POST http://localhost:5000/users
curl http://localhost:5000/products
curl -X POST http://localhost:5000/products
```

API endpointlariga murojaat qilish uchun quyidagilar ishlatiladi:

* `GET` - API endpointidan ma'lumotlarni olish uchun ishlatiladi.
* `POST` - API endpointiga yangi ma'lumotni yuborish uchun ishlatiladi.
* `http://localhost:5000` - API serverining URL-i.
* `users` - `/users` API endpointi.
* `products` - `/products` API endpointi.
