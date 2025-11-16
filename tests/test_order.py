import requests
import pytest
import Diplom_API_tests.urls as urls

@pytest.fixture
def auth_token(new_user):
    requests.post(urls.REGISTER_URL, json=new_user)
    response = requests.post(urls.LOGIN_URL, json=new_user)
    return response.json()["accessToken"]

@pytest.fixture
def ingredient_ids():
    response = requests.get(urls.INGREDIENTS_URL)
    data = response.json()["data"]
    return [item["_id"] for item in data]

def test_create_order_with_auth(auth_token, ingredient_ids):
    response = requests.post(
        urls.ORDERS_URL,
        headers={"Authorization": auth_token},
        json={"ingredients": ingredient_ids[:2]}
    )
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_create_order_without_auth(ingredient_ids):
    response = requests.post(
        urls.ORDERS_URL,
        json={"ingredients": ingredient_ids[:1]}
    )
    # API может вернуть 200 (гостевой заказ) или 401 (ошибка авторизации)
    if response.status_code == 200:
        assert response.json()["success"] is True
    elif response.status_code == 401:
        assert response.json()["success"] is False
    else:
        pytest.fail(f"Unexpected status code: {response.status_code}")

def test_create_order_with_ingredients(auth_token, ingredient_ids):
    response = requests.post(
        urls.ORDERS_URL,
        headers={"Authorization": auth_token},
        json={"ingredients": ingredient_ids[:1]}
    )
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_create_order_without_ingredients(auth_token):
    response = requests.post(
        urls.ORDERS_URL,
        headers={"Authorization": auth_token},
        json={"ingredients": []}
    )
    assert response.status_code == 400
    assert response.json()["success"] is False

def test_create_order_invalid_hash(auth_token):
    response = requests.post(
        urls.ORDERS_URL,
        headers={"Authorization": auth_token},
        json={"ingredients": ["invalid_hash"]}
    )
    assert response.status_code in (400, 500)
    assert response.json()["success"] is False