import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_add_and_get_transaction(client):
    # Get transactions
    res = client.get('/transactions')
    data = res.get_json()
    assert len(data) == 2
    assert data[0]['amount'] == 30.0
    assert data[1]['amount'] == 70.0
