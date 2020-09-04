from uuid import uuid4, UUID
from sqlalchemy_utils import UUIDType

from backend.db import db
from backend.employee.model import Employee
from backend.customer.model import Customer

from backend.view_utils import to_uuid

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(UUIDType(), primary_key=True)
    service_items = db.Column(db.String(45), nullable=False)
    
    customer_id = db.Column(UUIDType(), db.ForeignKey(Customer.id), nullable=False)
    employee_id = db.Column(UUIDType(), db.ForeignKey(Employee.id), nullable=False)
    
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    employee = db.relationship('Employee', backref=db.backref('orders', lazy=True))
    
    order_time = db.Column(db.String(45), nullable=False)
    star_rating = db.Column(db.Integer, nullable=True)
    stat = db.Column(db.Integer, nullable=False)


    @staticmethod
    def new_Order(id, service_items, customer_id, employee_id, order_time, stat, star_rating=None) -> "Order":
        # Test that customer & employee ids are valid
        customer = Customer.get_by_id(customer_id)
        employee = Employee.get_by_id(employee_id)
        
        return Order(
            id = id,
            service_items = service_items,
            customer_id = customer_id,
            employee_id = employee_id,
            order_time = order_time,
            star_rating = star_rating,
            stat = stat
        )

    @staticmethod
    def get_by_id(id) -> "Order":
        id = to_uuid(id)

        query = Order.query.filter_by(id=id)

        if query.count() == 0:
            raise ValueError(f"Order {str(id)} not found.")
        
        return query.first()
    
    def json(self) -> dict:
        return {
            "id": str(self.id),
            "service_items": service_items,
            "customer_id": self.customer_id,
            "employee_id": self.employee_id,
            "order_time": self.order_time,
            "star_rating": self.star_rating,
            "stat": self.stat,
        }

    @staticmethod
    def get_by_participant_id(role, id) -> list:
        id = to_uuid(id)

        if role =='customer':
            query = Order.query.filter_by(customer_id=id)
        elif role == 'employee':
            query = Order.query.filter_by(employee_id=id)
        else:
            raise AttributeError(f"Role {role} not valid for order {str(id)}")

        return query.all()

