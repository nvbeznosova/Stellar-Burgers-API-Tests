import requests
import Diplom_API_tests.urls as urls

def test_create_unique_user(new_user):
    response = requests.post(urls.REGISTER_URL, json=new_user)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_create_existing_user(new_user):
    requests.post(urls.REGISTER_URL, json=new_user)
    response = requests.post(urls.REGISTER_URL, json=new_user)
    assert response.status_code == 403
    assert response.json()["message"] == "User already exists"

def test_create_user_missing_field(new_user):
    user = new_user.copy()
    user.pop("email")
    response = requests.post(urls.REGISTER_URL, json=user)
    assert response.status_code == 403
    assert response.json()["success"] is False