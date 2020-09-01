from backend.session.model import User

users = [
    ("admin", "pass", "admin"),
    ("customer", "pass", "customer"),
    ("employee", "pass", "employee"),
]

UsersGenerator = (User.new_user(name, pwd, role) for name, pwd, role in users)