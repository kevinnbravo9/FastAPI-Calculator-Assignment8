from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_add_endpoint():
    response = client.post("/add", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_subtract_endpoint():
    response = client.post("/subtract", json={"a": 10, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 5, "b": 4})

    assert response.status_code == 200
    assert response.json() == {"result": 20}


def test_divide_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 2})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_divide_by_zero_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 0})

    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}