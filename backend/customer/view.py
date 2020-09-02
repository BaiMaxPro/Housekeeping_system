from flask_restful import Resource, reqparse

from backend.customer.model import Customer
from backend.db import db

from backend.view_utils import error, to_uuid

from backend.session.view import authenticated

class CustomerRootAPI(Resource):
    def get(self):
        customers = Customer.query.all()
        resp = [customer.json() for customer in customers]
        return resp

class CustomerAPI(Resource):
    @authenticated
    def get(self, id, **kwargs):
        try:
            id = to_uuid(id)
        except AttributeError as e:
            return error(e, 400)

        auth_user = kwargs["user"]

        def get_customer_info(id):
            try:
                return Customer.get_by_id(id).json()
            except AttributeError as e:
                return error(e, 400)
            except ValueError as e:
                return error(e, 404)

        if auth_user.role == "customer" and auth_user.id == id:
            return get_customer_info(id)
        
        if auth_user.role == "admin":
            return get_customer_info(id)
        
        return error("Not authorized", 401)
        
        
