import requests
import Diplom_API_tests.urls as urls

def test_login_existing_user(new_user):
    requests.post(urls.REGISTER_URL, json=new_user)
    response = requests.post(urls.LOGIN_URL, json={
        "email": new_user["email"],
        "password": new_user["password"]
    })
    assert response.status_code == 200
    assert "accessToken" in response.json()

def test_login_wrong_credentials():
    response = requests.post(urls.LOGIN_URL, json={
        "email": "wrong@test.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
    assert response.json()["success"] is False