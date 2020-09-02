import requests
from backend.test_utils import full_url

def login(username: str, password: str) -> (str, dict):
    headers = {"username": username, "password": password}
    sess = requests.post(full_url("login"), headers=headers)
    sess = sess.json()
    return sess["id"], sess