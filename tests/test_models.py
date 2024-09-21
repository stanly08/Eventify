import pytest
from app import create_app, db
from app.models import User, Admin, Event

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_user_model(app):
    user = User(username='testuser', password='password')
    db.session.add(user)
    db.session.commit()
    assert user.username == 'testuser'
