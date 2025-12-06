import requests
import Diplom_2.urls as urls
import allure

class TestLogin:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, new_user):
        with allure.step("Регистрируем нового пользователя"):
            requests.post(urls.REGISTER_URL, json=new_user)
        with allure.step("Отправляем запрос на логин"):
            response = requests.post(urls.LOGIN_URL, json={
                "email": new_user["email"],
                "password": new_user["password"]
            })
        assert response.status_code == 200
        assert "accessToken" in response.json()

    @allure.title("Логин с неверными данными")
    def test_login_wrong_credentials(self):
        with allure.step("Отправляем запрос на логин с неверными данными"):
            response = requests.post(urls.LOGIN_URL, json={
                "email": "wrong@test.com",
                "password": "wrongpass"
            })
        assert response.status_code == 401
        assert response.json()["success"] is False