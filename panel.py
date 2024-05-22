import firebase_admin
from firebase_admin import db
from flask import Flask, request, jsonify
import uuid

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Khởi tạo kết nối đến Firebase Realtime Database
cred = firebase_admin.credentials.Certificate("ServiceAccount.json")  
firebase_admin.initialize_app(cred, {'databaseURL': 'https://btl-python-de2-default-rtdb.firebaseio.com/'})
firebase_db = db.reference('/')

@app.route('/add', methods=['POST'])
def add_product():
    try:
        id = str(uuid.uuid4())
        firebase_db.child('products').child(id).set(request.json)
        return jsonify({"success": True, "id": id}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/list', methods=['GET'])
def list_products():
    try:
        all_products = firebase_db.child('products').get()
        return jsonify(all_products), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/update/<string:id>', methods=['PUT'])
def update_product(id):
    try:
        firebase_db.child('products').child(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/delete/<string:id>', methods=['DELETE'])
def delete_product(id):
    try:
        firebase_db.child('products').child(id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/search', methods=['GET'])
def search_products():
    try:
        search_query = request.args.get('title')
        if search_query:
            search_results = []
            products = firebase_db.child('products').get()
            for key, value in products.items():
                if search_query.lower() in value['title'].lower():
                    value['id'] = key
                    search_results.append(value)
            return jsonify(search_results), 200
        else:
            return jsonify({"success": False, "error": "No search query provided"}), 400
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
