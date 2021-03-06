from datetime import datetime, timedelta
import pytest
import flask

from backend.session.model import Session, User
from backend.session.view import authenticated

from backend.test_utils import setup, app

def test_new_session(setup):
    username = "admin"
    session = Session.new_session(username)
    assert session.user.username == username
    assert not session.expired()

    setup.session.add(session)
    setup.session.commit()

    session = Session.get_by_id(session.id)
    assert session.user.username == username

def test_expired_session(setup):
    username = "customer"
    time = datetime.now() - timedelta(hours=2)
    session = Session.new_session(username, time)
    setup.session.add(session)
    setup.session.commit()

    with pytest.raises(ValueError):
        assert session.get_by_id(session.id)

def test_user_backref(setup):
    username = "employee"
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

def test_auth_success(setup, app, mocker):
    username = "admin"
    role = "admin"
    sess = Session.new_session("admin")

    setup.session.add(sess)
    setup.session.commit()

    with app.test_request_context():
        request = mocker.patch.object(flask, "request")
    request.headers = {"session-id":sess.id}
    
    def inner_func(username, expected_role, expected_sessid, **kwargs):
        sess = kwargs["session"]
        assert sess.user.username == username
        assert sess.user.role == expected_role
        assert sess.id == expected_sessid
        return "Success", 200
    
    wrapped_func = authenticated(inner_func)
    resp, code = wrapped_func(username, role, sess.id, 
        testing_request=request
    )

    assert resp == "Success"
    assert code == 200
    
def test_auth_faliure(setup, app, mocker):
    username = "admin"
    role = "admin"
    expire = datetime.now() + timedelta(hours=-3)
    sess = Session.new_session("admin", expire)

    setup.session.add(sess)
    setup.session.commit()

    with app.test_request_context():
        request = mocker.patch.object(flask, "request")
    request.headers = {"session-id":sess.id}
    
    def inner_func(**kwargs):
        assert not 1 == 1  #This inner func should not be called

    wrapped_func = authenticated(inner_func)
    resp, code, headers = wrapped_func(username, role, sess.id, 
        testing_request=request
    )

    assert "error" in resp.keys()
    assert code == 401
