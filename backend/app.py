from flask import Flask, Blueprint
from flask_restful import Api

# Patch PYTHONPATH
from sys import path
path.append(".")

from backend import config
from backend.db import db
from backend.create_db import create_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app=app)

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

from backend.session.view import UserRootAPI, UserAPI, LoginAPI
api.add_resource(LoginAPI, "/login")
api.add_resource(UserRootAPI, "/user")
api.add_resource(UserAPI, "/user/<string:id>")

from backend.customer.view import CustomerRootAPI, CustomerAPI, CustomerOrdersAPI
api.add_resource(CustomerRootAPI, "/customer")
api.add_resource(CustomerAPI, "/customer/<string:id>")
api.add_resource(CustomerOrdersAPI, "/customer/<string:id>/orders")

from backend.employee.view import EmployeeRootAPI, EmployeeAPI, EmployeeOrdersAPI
api.add_resource(EmployeeRootAPI, "/employee")
api.add_resource(EmployeeAPI, "/employee/<string:id>")
api.add_resource(EmployeeOrdersAPI, "/employee/<string:id>/orders")

from backend.order.view import OrderRootAPI, OrderAPI
api.add_resource(OrderRootAPI, "/order")
api.add_resource(OrderAPI, "/order/<string:id>")

app.register_blueprint(blueprint, url_prefix='/api')

if __name__ == '__main__':
    if config.INIT_DATABASE:
        create_db(app, db)

    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG, use_reloader=config.DEBUG)