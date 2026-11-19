from flask import Flask, jsonify

app = Flask(__name__)

inventory = [{
        'id': 1,
        'name': "Pen",
        'stock': 10
    },
    {
        'id': 2,
        'name': 'Bag',
        'stock': 5
    }
    ]

@app.route("/")
def home():
    return 'Hello'

@app.route("/items")
def items():

    return jsonify(inventory)

@app.route("/items/<int:item_id>")
def get_items(item_id):
    for product in inventory:
        if product['id'] == item_id:
            return jsonify(product)
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)