import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_cars(client):
    response = client.get('/car_list')
    assert response.status_code == 200
    assert b'Carro A' in response.data
    assert b'Carro B' in response.data