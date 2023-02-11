from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from db import db

from controllers import carts, products
from models import Cart, CartLine, Product


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
cors = CORS(app, resources={r'*': {'origins': '*'}})
migrate = Migrate(app, db)

app.register_blueprint(carts)
app.register_blueprint(products)

# shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Product=Product, CartLine=CartLine, Cart=Cart)
