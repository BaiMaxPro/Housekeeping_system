from backend.test_utils import full_url
import requests

def test_default_users():
    url = full_url("user")
    resp = requests.get(url).json()
    usernames = [u["username"] for u in resp]
    assert "admin" in usernames
    assert "customer" in usernames
    assert "employee" in usernames

def test_create_user():
    url = full_url("user")
    resp = requests.post(url, 
        data={"username": "a", "password": "pass"},
    )
    data = resp.json()
    assert data["username"] == "a"
    assert resp.status_code == 201
    assert data["id"] != None

    url = f"{url}/{data['id']}"
    resp = requests.get(url)
    data = resp.json()
    assert resp.status_code == 200
    assert data["username"] == "a"