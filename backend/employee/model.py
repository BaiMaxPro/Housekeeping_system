from uuid import uuid4, UUID
from sqlalchemy_utils import UUIDType

from backend.db import db
from backend.session.model import User

from backend.view_utils import to_uuid

class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(UUIDType(), db.ForeignKey(User.id), primary_key=True)
    user = db.relationship('User')
    name = db.Column(db.String(45), nullable=False)
    gender = db.Column(db.String(45), nullable=False)
    tel = db.Column(db.String(45), nullable=False)
    # stat = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, nullable=False)

    @staticmethod
    def new_employee(id, name, gender, tel, level=0) -> "Employee":
        # Test that employee id exists in user table
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
    
    @staticmethod
    def id_exists(id) -> bool:
        id = to_uuid(id)

        query = Employee.query.filter_by(id=id)

        if query.count() > 0:
            return True
        return False

    def json(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "gender": self.gender,
            "tel": self.tel,
            "level": self.level,
        }
