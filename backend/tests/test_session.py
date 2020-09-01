from backend.test_utils import base_url
import requests
from requests.compat import urljoin

def test_not_logged_in():
    url = urljoin(base_url, "login")
    resp = requests.get(url)

    assert resp.status_code == 401
    assert "error" in resp.json().keys()

def test_admin_login():
    url = urljoin(base_url, "login")
    headers = {"username": "admin", "password": "pass"}
    resp = requests.post(url, headers=headers)

    assert resp.status_code == 200
    assert "id" in resp.json().keys()

    headers = {"session-id": resp.json()["id"]}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    
    user = resp.json()["user"]

    assert user["username"] == "admin"
    assert user["role"] == "admin"

def test_admin_logout():
    url = urljoin(base_url, "login")
    headers = {"username": "admin", "password": "pass"}
    resp = requests.post(url, headers=headers)  # Login
    assert resp.status_code == 200
    assert "id" in resp.json().keys()

    headers = {"session-id": resp.json()["id"]}
    resp = requests.delete(url, headers=headers)    # Logout
    assert resp.status_code == 204
    
    resp = requests.get(url, headers=headers)   # Test logged in
    assert resp.status_code == 401
    assert "error" in resp.json().keys()