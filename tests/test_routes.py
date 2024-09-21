import pytest
from app import create_app, db

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Event Registration System' in response.data
