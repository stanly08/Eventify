import pytest
from app import create_app, db

@pytest.fixture
def client(app):
    return app.test_client()

def test_admin_dashboard(client):
    # Assuming you have an admin login function for testing
    response = client.post('/admin/login', data={'username': 'admin', 'password': 'adminpass'})
    assert response.status_code == 200
    response = client.get('/admin/dashboard')
    assert b'Admin Dashboard' in response.data
