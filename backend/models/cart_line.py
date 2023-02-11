from db import db


class CartLine(db.Model):
    __tablename__ = 'cart_lines'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    total = db.Column(db.Float)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'total': self.total,
            'product': self.product.id,
            'cart': self.cart.id
        }
