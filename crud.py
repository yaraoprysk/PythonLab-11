import copy
import json

from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from models.abstract_product import AbstractProduct

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartAbstractProduct(AbstractProduct, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String(32), unique=False)
    capacity_in_mL = db.Column(db.Integer, unique=False)
    packing = db.Column(db.String(32), unique=False)
    producer = db.Column(db.String(32), unique=False)
    coffee_roasting = db.Column(db.String(32), unique=False)
    price_in_UAH = db.Column(db.Integer(), unique=False)
    customer = db.Column(db.String(32), unique=False)
    add_ons = db.Column(db.String(32), unique=False)

    def __init__(self, variety, capacity_in_mL, packing, producer,
                 coffee_roasting, price_in_UAH, customer, add_ons):
        super().__init__(variety, capacity_in_mL, packing, producer,
                         coffee_roasting, price_in_UAH)
        self.customer = customer
        self.add_ons = add_ons


class SmartAbstractProductSchema(ma.Schema):
    class Meta:
        fields = ('variety', 'capacity_in_mL',
                  'packing', 'producer',
                  'coffee_roasting', 'price_in_UAH',
                  'customer', 'add_ons')


smart_abstract_product_schema = SmartAbstractProductSchema()
smart_abstract_products_schema = SmartAbstractProductSchema(many=True)


@app.route("/smart_abstract_product", methods=["POST"])
def add_smart_abstract_product():
    smart_abstract_product = SmartAbstractProduct(request.json['variety'],
                                                  request.json['capacity_in_mL'],
                                                  request.json['packing'],
                                                  request.json['producer'],
                                                  request.json['coffee_roasting'],
                                                  request.json['price_in_UAH'],
                                                  request.json['customer'],
                                                  request.json['add_ons'])

    db.session.add(smart_abstract_product)
    db.session.commit()
    return smart_abstract_product_schema.jsonify(smart_abstract_product)


@app.route("/smart_abstract_product", methods=["GET"])
def get_smart_abstract_product():
    all_smart_abstract_product = SmartAbstractProduct.query.all()
    result = smart_abstract_products_schema.dump(all_smart_abstract_product)
    return jsonify({'smart_abstract_product': result})


@app.route("/smart_abstract_product/<id>", methods=["GET"])
def smart_abstract_product_detail(id):
    smart_abstract_product = SmartAbstractProduct.query.get(id)
    if not smart_abstract_product:
        abort(404)
    return smart_abstract_product_schema.jsonify(smart_abstract_product)


@app.route("/smart_abstract_product/<id>", methods=["PUT"])
def smart_abstract_product_update(id):
    smart_abstract_product = SmartAbstractProduct.query.get(id)
    if not smart_abstract_product:
        abort(404)
    old_smart_abstract_product = copy.deepcopy(smart_abstract_product)
    smart_abstract_product.variety = request.json['variety']
    smart_abstract_product.capacity_in_mL = request.json['capacity_in_mL']
    smart_abstract_product.packing = request.json['packing']
    smart_abstract_product.producer = request.json['producer']
    smart_abstract_product.coffee_roasting = request.json['coffee_roasting']
    smart_abstract_product.price_in_UAH = request.json['price_in_UAH']
    smart_abstract_product.customer = request.json['customer']
    smart_abstract_product.add_ons = request.json['add_ons']
    db.session.commit()
    return smart_abstract_product_schema.jsonify(old_smart_abstract_product)


@app.route("/smart_abstract_product/<id>", methods=["DELETE"])
def smart_abstract_product_delete(id):
    smart_abstract_product = SmartAbstractProduct.query.get(id)
    if not smart_abstract_product:
        abort(404)
    db.session.delete(smart_abstract_product)
    db.session.commit()
    return smart_abstract_product_schema.jsonify(smart_abstract_product)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='127.0.0.1')
