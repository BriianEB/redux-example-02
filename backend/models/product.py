from db import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(64))
    price = db.Column(db.Float)

    cart_lines = db.relationship('CartLine',
        backref=db.backref('product'),
        lazy='dynamic'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'cart_lines': [line.id for line in self.cart_lines.all()]
        }
