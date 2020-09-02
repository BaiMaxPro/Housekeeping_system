from uuid import uuid4, UUID
from sqlalchemy_utils import UUIDType

from backend.db import db
from backend.employee.model import Employee
from backend.customer.model import Customer

class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(UUIDType(), db.ForeignKey(Customer.id,Employee.id), primary_key=True)
    service_items = db.Column(db.String(45), nullable=False)
    customer_id = db.relationship('Customer', backref=db.backref('info', uselist=False ,lazy=True))
    employee_id = db.relationship('Employee', backref=db.backref('info', uselist=False ,lazy=True))
    order_time = db.Column(db.String(45), nullable=False)
    star_rating = db.Column(db.Integer, nullable=True)


    @staticmethod
    def new_Order(id, service_items, customer_id, employee_id, order_time, star_rating) -> "Order":
        order = Order.get_by_id(id)
        return Order(
            id = id,
            service_items = service_items,
            customer_id = customer_id,
            employee_id = employee_id,
            order_time = order_time,
            star_rating = star_rating
        )

    def get_by_id(id) -> "Order":
        if type(id) != UUID:
            try:
                id = UUID(id)
            except:
                raise AttributeError("Invalid UUID")

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
        }

    def get_id(role,id) -> "UUID_List":
        if type(id) != UUID:
            try:
                id = UUID(id)
            except:
                raise AttributeError("Invalid UUID")

        if role =='customer':
            query = Order.query.filter_by(customer_id=id)
        elif role == 'employee':
            query = Order.query.filter_by(employee_id=id)
        
        if query.count() == 0:
            raise ValueError(f"Order by {str(role)}id {str(id)} not found.")
        
        return query

