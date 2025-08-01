import requests

def test_create_item():
    response = requests.post("http://localhost:5000/items", json={"name": "Test Item"})
    assert response.status_code == 201

def test_get_items():
    response = requests.get("http://localhost:5000/items")
    assert response.status_code == 200