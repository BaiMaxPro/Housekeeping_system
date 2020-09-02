import pytest
import os

@pytest.fixture(scope="session")
def setup():
    from backend.app import app, db, create_db
    create_db(app, db)
    return db

@pytest.fixture()
def client():
    from backend.app import app
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture()
def app():
    from backend.app import app
    return app

# Base URL config  
port = os.environ.get("FLASK_TEST_PORT")
server = os.environ.get("FLASK_TEST_SERVER")

if port == None:
    port = 5000

if server == None:
    server = "localhost"

base_url = f"http://{server}:{port}/api/"