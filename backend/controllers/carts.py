from flask import Blueprint, request

from db import db
from models import Cart, CartLine, Product


carts = Blueprint('carts', __name__)

@carts.route('/carts')
def index():
    carts = Cart.query.all()

    return [cart.to_dict() for cart in carts]

@carts.route('/carts', methods=['POST'])
def create():
    cart = request.get_json()

    if not cart:
        return 'error'

    o_cart = Cart(total_quantity=cart['totalQuantity'])

    for line in cart['items']:
        product = Product.query.get(line['id'])
        o_line = CartLine(quantity=line['quantity'], total=line['totalPrice'], product=product)
        db.session.add(o_line)
        o_cart.cart_lines.append(o_line)

    db.session.add(o_cart)
    db.session.commit()
    db.session.refresh(o_cart)

    return o_cart.to_dict()

@carts.route('/carts/<id>')
def show(id):
    cart = Cart.query.get(int(id))
    cart_dict = cart.to_dict()

    if request.args.get('full'):
        full_lines = []
        for line in cart_dict['cart_lines']:
            full_line = CartLine.query.get(line).to_dict()
            full_line['product'] = Product.query.get(full_line['product']).to_dict()
            full_lines.append(full_line)

        cart_dict['cart_lines'] = full_lines

    return cart_dict

@carts.route('/carts/<id>', methods=['PUT'])
def update(id):
    cart = Cart.query.get(int(id))

    if not cart:
        return 'error'

    cart_data = request.get_json()

    if not cart_data:
        return 'error'

    cart.total_quantity = cart_data['totalQuantity']
    cart.cart_lines.delete()

    for line in cart_data['items']:
        product = Product.query.get(line['id'])
        o_line = CartLine(quantity=line['quantity'], total=line['totalPrice'], product=product)
        db.session.add(o_line)
        cart.cart_lines.append(o_line)

    db.session.add(cart)
    db.session.commit()
    db.session.refresh(cart)

    return cart.to_dict()
