from datetime import datetime, timedelta
import pytest

from backend.session.model import Session, User
from backend.session.generator import users

from backend.test_utils import setup

def test_new_session(setup):
    username = users[0][0]
    session = Session.new_session(username)
    assert session.user.username == username
    assert not session.expired()

    setup.session.add(session)
    setup.session.commit()

    session = Session.get_by_id(session.id)
    assert session.user.username == username

def test_expired_session(setup):
    username = users[1][0]
    time = datetime.now() - timedelta(hours=2)
    session = Session.new_session(username, time)
    setup.session.add(session)
    setup.session.commit()

    with pytest.raises(ValueError):
        assert session.get_by_id(session.id)

def test_user_backref(setup):
    username = users[2][0]
    session = Session.new_session(username)
    setup.session.add(session)
    setup.session.commit()
    
    user = User.get_by_username(username)
    ids = [session.id for session in user.sessions]

    assert session.id in ids

def test_session_role(setup):
    sess_admin = Session.new_session("admin")
    setup.session.add(sess_admin)

    sess_customer = Session.new_session("customer")
    setup.session.add(sess_customer)

    sess_employee = Session.new_session("employee")
    setup.session.add(sess_employee)

    setup.session.commit()

    assert sess_admin.user.role == "admin"
    assert sess_customer.user.role == "customer"
    assert sess_employee.user.role == "employee"