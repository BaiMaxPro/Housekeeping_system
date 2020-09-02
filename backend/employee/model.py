from uuid import uuid4, UUID
from sqlalchemy_utils import UUIDType

from backend.db import db
from backend.session.model import User

class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(UUIDType(), db.ForeignKey(User.id), primary_key=True)
    user = db.relationship('User', backref=db.backref('info', uselist=False ,lazy=True))
    name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    tel = db.Column(db.String(45), nullable=False)
    # stat = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    @staticmethod
    def new_Employee(id, name, gender, tel, level=0) -> "Employee":
        user = User.get_by_id(id)
        return Employee(
            id = id,
            name = name,
            gender = gender,
            tel = tel,
            level = level,
            # stat = stat
        )

    @staticmethod
    def get_by_id(id) -> "Employee":
        if type(id) != UUID:
            try:
                id = UUID(id)
            except:
                raise AttributeError("Invalid UUID")

        query = Employee.query.filter_by(id=id)

        if query.count() == 0:
            raise ValueError(f"Employee {str(id)} not found.")
        
        return query.first()
    
    def json(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "gender": self.gender,
            "tel": self.tel,
            "level": self.level,
        }
