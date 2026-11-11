from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({'message': 'Welcome to the home page', 'resource_endpoint': '/products'}), 200

@app.route("/products", methods = ['GET'])
def get_products():
    if request.args.get("category"):
        filtered = [item for item in products if item['category'] == request.args.get("category")]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200
    return jsonify({"message": 'Product not found'}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)
