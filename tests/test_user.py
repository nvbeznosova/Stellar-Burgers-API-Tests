import requests
import Diplom_2.urls as urls
import allure

class TestUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, new_user):
        with allure.step("Отправляем запрос на регистрацию нового пользователя"):
            response = requests.post(urls.REGISTER_URL, json=new_user)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, new_user):
        with allure.step("Регистрируем пользователя первый раз"):
            requests.post(urls.REGISTER_URL, json=new_user)
        with allure.step("Пытаемся зарегистрировать того же пользователя ещё раз"):
            response = requests.post(urls.REGISTER_URL, json=new_user)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_missing_field(self, new_user):
        user = new_user.copy()
        user.pop("email")
        with allure.step("Отправляем запрос на регистрацию без email"):
            response = requests.post(urls.REGISTER_URL, json=user)
        assert response.status_code == 403
        assert response.json()["success"] is False