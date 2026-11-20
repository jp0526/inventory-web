from flask import Flask, jsonify, request
from models import Item
from engine import Session

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello'

@app.route("/items")
def items():
    session = Session()
    rows = session.query(Item).all()
    output = []
    for row in rows:
        output.append({
            'id' : row.id,
            'product': row.product,
            'stock_qty': row.stock_qty
        })
    session.close()
    return jsonify(output)

@app.route("/items/<int:item_id>")
def get_items(item_id):
    session = Session()
    row = session.get(Item, item_id)
    session.close()
    if row is not None:
        item = {
            'id' : row.id,
            'product': row.product,
            'stock_qty': row.stock_qty
        }
        return jsonify(item)
    return jsonify({"error": "not found"}), 404

@app.route("/items", methods=['POST'])
def add_item():
    session = Session()
    data = request.get_json()
    item = Item(product = data['product'], stock_qty = data['stock_qty'])
    session.add(item)
    session.commit()
    result = {
        'id' : item.id,
        'product': item.product,
        'stock_qty': item.stock_qty
    }
    session.close()
    return(result), 201


if __name__ == "__main__":
    app.run(debug=True)