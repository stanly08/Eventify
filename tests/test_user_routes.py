import pytest
from app import create_app, db

@pytest.fixture
def client(app):
    return app.test_client()

def test_user_registration(client):
    response = client.post('/register', data={'username': 'newuser', 'password': 'newpassword'})
    assert response.status_code == 200
    assert b'Registration successful!' in response.data

def test_event_registration(client):
    # Assuming there's a function to create an event first
    response = client.post('/register_event', data={'event_id': 1})
    assert response.status_code == 200
    assert b'Registration for event successful!' in response.data
