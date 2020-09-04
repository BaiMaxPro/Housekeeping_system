from backend.test_utils import full_url
from backend.tests.utils import login
import requests

def _valid_customer(customer) -> bool:
    assert "id" in customer.keys()
    assert "name" in customer.keys()
    assert "gender" in customer.keys()
    assert "tel" in customer.keys()
    assert "address" in customer.keys()
    assert "level" in customer.keys()
    return True

def test_byid_api_customer_access():
    # Login
    sessid, sess = login("customer", "pass")

    # Get customer info
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}/{sess['user']['id']}"
    resp = requests.get(url, headers=headers)
    info = resp.json()

    assert _valid_customer(info)

def test_byid_api_admin_access():
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

    assert _valid_customer(info)

def test_byid_api_other_customer_no_access():
    # Login
    sessid, sess = login("admin", "pass")

    # Get last customer id
    headers = {"session-id": sessid}
    url = f"{full_url('customer')}"
    resp = requests.get(url, headers=headers)
    customer = resp.json()[-1]

    assert _valid_customer(customer)

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

def test_root_api_admin_access():
    # Login
    sessid, sess = login("admin", "pass")
    print(sess)

    headers = {"session-id": sessid}
    url = f"{full_url('customer')}"
    resp = requests.get(url, headers=headers)
    customers = resp.json()
    assert len(customers) > 0

    assert _valid_customer(customers[0])

def test_root_api_non_admin_access():
    for user in ("customer", "employee"):
        # Login
        sessid, sess = login(user, "pass")
        print(f"User {user}: {sess}")

        headers = {"session-id": sessid}
        url = f"{full_url('customer')}"
        resp = requests.get(url, headers=headers)
        customers = resp.json()

        assert "error" in resp.json().keys()
        assert resp.status_code == 401
