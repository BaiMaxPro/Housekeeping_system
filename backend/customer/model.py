from uuid import uuid4, UUID
from sqlalchemy_utils import UUIDType

from backend.db import db
from backend.session.model import User

from backend.view_utils import to_uuid

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(UUIDType(), db.ForeignKey(User.id), primary_key=True)
    user = db.relationship('User', backref=db.backref('info', uselist=False ,lazy=True))
    name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    tel = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    @staticmethod
    def new_customer(id, name, gender, tel, address, level=0) -> "Customer":
        user = User.get_by_id(id)
        return Customer(
            id = id,
            name = name,
            gender = gender,
            tel = tel,
            address = address,
            level = level,
        )

    @staticmethod
    def get_by_id(id) -> "Customer":
        id = to_uuid(id)

        query = Customer.query.filter_by(id=id)

        if query.count() == 0:
            raise ValueError(f"Customer {str(id)} not found.")
        
        return query.first()
    
    def json(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "gender": self.gender,
            "tel": self.tel,
            "address": self.address,
            "level": self.level,
        }
