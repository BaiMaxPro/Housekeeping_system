from flask_restful import Resource, reqparse
from uuid import uuid4

from backend.employee.model import Employee
from backend.order.model import Order
from backend.db import db

from backend.view_utils import error, to_uuid

from backend.session.view import authenticated

def _acl_create_order_same_customer_or_admin(request_id, auth_user) -> bool:
    if auth_user.role == "customer" and auth_user.id == request_id:
        return True

    if auth_user.role == "admin":
        return True

    return False

def _acl_get_order_same_participant_or_admin(order: Order, auth_user) -> bool:
    if auth_user.role == "customer" and auth_user.id == order.customer_id:
        return True
    
    if auth_user.role == "employee" and auth_user.id == order.employee_id:
        return True
    
    if auth_user.role == "admin":
        return True

    return False
        

def _parse_full_order_request():
    parser = reqparse.RequestParser()
    parser.add_argument("customer_id", required=True, help="Customer ID is required")
    parser.add_argument("employee_id", required=True, help="Employee ID is required")
    parser.add_argument("order_time", required=True, help="Order time is required")
    parser.add_argument("item", required=True, help="Item is required")

    return parser.parse_args()

class OrderRootAPI(Resource):
    @authenticated
    def get(self, **kwargs):
        auth_user = kwargs["user"]
        if auth_user.role != "admin":
            return error("Not authorized", 401)

        orders = Order.query.all()
        resp = [order.json() for order in orders]
        return resp
    
    @authenticated
    def post(self, **kwargs):
        auth_user = kwargs["user"]
        args = _parse_full_order_request()

        if not _acl_create_order_same_customer_or_admin(args['customer_id'], auth_user):
            return error("Not authorized", 401)
        
        order = Order.new_order(
            id = uuid4(),
            item = args["item"],
            customer_id = args["customer_id"],
            employee_id = args["employee_id"],
            order_time = args["order_time"],
        )

        db.session.add(order)
        db.session.commit()

        return order.json(), 201

class OrderAPI(Resource):
    @authenticated
    def get(self, id, **kwargs):
        try:
            id = to_uuid(id)
        except AttributeError as e:
            return error(e, 400)

        auth_user = kwargs["user"]

        try:
            order = Order.get_by_id(id)
            if _acl_get_order_same_participant_or_admin(order, auth_user):
                return order.json(), 201
            return error("Not authorized", 401)

        except AttributeError as e:
            return error(e, 400)
        except ValueError as e:
            if auth_user.role == "admin":
                return error(e, 404)

            # For regular users: they shouldn't know if an order id exists
            return error("Not authorized", 401)
        
        # It should not reach here
        return error("Not authorized", 401)
        
