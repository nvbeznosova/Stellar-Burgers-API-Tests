import pytest
import requests
import Diplom_2.urls as urls
from Diplom_2.helpers import random_email

@pytest.fixture
def new_user():
    return {
        "email": random_email(),
        "password": "password123",
        "name": "Test User"
    }

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