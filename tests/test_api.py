import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_and_get_transaction(client):
    res = client.post('/transactions', json={
        'type': 'income',
        'amount': 30.0,
        'description': 'Salary'
    })
    assert res.status_code == 201

    # Get transactions
    res = client.get('/transactions')
    data = res.get_json()
    assert len(data) == 1
    assert data[0]['amount'] == 30.0
    assert data[0]['type'] == 'income'
    assert data[0]['description'] == 'Salary'
