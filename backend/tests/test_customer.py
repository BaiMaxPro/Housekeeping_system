from backend.test_utils import full_url
from backend.tests.utils import login
import requests

def test_customer_access():
    # Login
    sessid, sess = login("customer", "pass")

    # Get customer info
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}/{sess['user']['id']}"
    resp = requests.get(url, headers=headers)
    info = resp.json()

    assert "id" in info.keys()
    assert "name" in info.keys()
    assert "gender" in info.keys()
    assert "tel" in info.keys()
    assert "address" in info.keys()
    assert "level" in info.keys()

def test_admin_access():
    # Login
    sessid, sess = login("admin", "pass")
    print(sess)

    # Get last customer id
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}"
    resp = requests.get(url, headers=headers)
    customer = resp.json()[-1]
    print(sess)

    # Get last customer info
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}/{customer['id']}"
    resp = requests.get(url, headers=headers)
    info = resp.json()

    assert "id" in info.keys()
    assert "name" in info.keys()
    assert "gender" in info.keys()
    assert "tel" in info.keys()
    assert "address" in info.keys()
    assert "level" in info.keys()

def test_other_customer_no_access():
    # Login
    sessid, sess = login("admin", "pass")

    # Get last customer id
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}"
    resp = requests.get(url, headers=headers)
    customer = resp.json()[-1]

    # Login as another customer
    sessid, sess = login("customer", "pass")
    if sess["user"]["id"] == customer["id"]:
        print("Not enough customers in database")
        return

    # Get last customer info
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}/{customer['id']}"
    resp = requests.get(url, headers=headers)

    assert "error" in resp.json().keys()
    assert resp.status_code == 401
