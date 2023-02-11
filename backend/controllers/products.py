from flask import Blueprint, request

from db import db
from models import Product


products = Blueprint('products', __name__)

@products.route('/products')
def index():
    products = Product.query.all()

    return [product.to_dict() for product in products]

@products.route('/products', methods=['POST'])
def create():
    product = request.get_json()

    if not product:
        return 'error'

    o_product = Product(name=product['name'], description=product['description'], price=product['price'])
    db.session.add(o_product)
    db.session.commit()
    db.session.refresh(o_product)

    return o_product.to_dict()

@products.route('/products/<id>')
def show(id):
    product = Product.query.get(int(id))

    return product.to_dict()
