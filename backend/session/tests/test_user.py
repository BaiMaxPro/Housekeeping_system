from backend.session.model import User
from backend.test_utils import setup

def test_new_user():
    username = "test-new"
    password = "test-password"
    role = "admin"
    user = User.new_user(username, password, role)
    assert user.username == "test-new"
    assert user.check_password(password)
    assert user.json()["username"] == username
    assert user.role == role

def test_salt():
    a = User.new_user("a", "pass")
    b = User.new_user("b", "pass")
    assert a.hash != b.hash