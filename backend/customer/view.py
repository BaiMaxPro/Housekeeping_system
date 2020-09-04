from flask_restful import Resource, reqparse

from backend.customer.model import Customer
from backend.order.model import Order
from backend.db import db

from backend.view_utils import error, to_uuid

from backend.session.view import authenticated

def _acl_same_customer_id_or_admin(request_id, auth_user) -> bool:
    if auth_user.role == "customer" and auth_user.id == request_id:
        return True

    if auth_user.role == "admin":
        return True

    return False

def _parse_full_user_request(update_level = False):
    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help="Name is required")
    parser.add_argument("gender", required=True, help="Gender is required")
    parser.add_argument("tel", required=True, help="Tel is required")
    parser.add_argument("address", required=True, help="Address is required")

    if update_level:
        parser.add_argument("level", required=True, help="Name is required")

    return parser.parse_args()

class CustomerRootAPI(Resource):
    @authenticated
    def get(self, **kwargs):
        auth_user = kwargs["user"]
        if auth_user.role != "admin":
            return error("Not authorized", 401)

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

        if _acl_same_customer_id_or_admin(id, auth_user):
            try:
                return Customer.get_by_id(id).json()
            except AttributeError as e:
                return error(e, 400)
            except ValueError as e:
                return error(e, 404)
        return error("Not authorized", 401)
        
    @authenticated
    def post(self, id, **kwargs):
        try:
            id = to_uuid(id)
        except AttributeError as e:
            return error(e, 400)

        auth_user = kwargs["user"]

        if not _acl_same_customer_id_or_admin(id, auth_user):
            return error("Not authorized", 401)
        
        args = _parse_full_user_request()
        
        if Customer.id_exists(id):
            return error("Customer ID exists", 400)

        cust = Customer.new_customer(
            id = id,
            name = args["name"],
            gender = args["gender"],
            tel = args["tel"],
            address = args["address"],
        )

        db.session.add(cust)
        db.session.commit()

        return cust.json(), 201
        
class CustomerOrdersAPI(Resource):
    @authenticated
    def get(self, id, **kwargs):
        try:
            id = to_uuid(id)
        except AttributeError as e:
            return error(e, 400)

        auth_user = kwargs["user"]

        if _acl_same_customer_id_or_admin(id, auth_user):
            try:
                orders = Order.get_by_participant_id("customer", id)
                return [order.json() for order in orders]
            except AttributeError as e:
                return error(e, 400)
            except ValueError as e:
                return error(e, 404)
        else:
            return error("Not authorized", 401)
