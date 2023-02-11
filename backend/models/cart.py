from db import db


class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    total_quantity = db.Column(db.Integer)

    cart_lines = db.relationship('CartLine',
        backref=db.backref('cart'),
        lazy='dynamic'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'total_quantity': self.total_quantity,
            'cart_lines': [line.id for line in self.cart_lines.all()]
        }
