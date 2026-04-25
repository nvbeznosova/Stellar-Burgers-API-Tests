import requests
import Diplom_2.urls as urls
import allure

class TestOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, auth_token, ingredient_ids):
        with allure.step("Отправляем запрос на создание заказа с авторизацией"):
            response = requests.post(
                urls.ORDERS_URL,
                headers={"Authorization": auth_token},
                json={"ingredients": ingredient_ids[:2]}
            )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredient_ids):
        with allure.step("Отправляем запрос на создание заказа без авторизации"):
            response = requests.post(
                urls.ORDERS_URL,
                json={"ingredients": ingredient_ids[:1]}
            )
        assert response.status_code == 401
        assert response.json()["success"] is False

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token, ingredient_ids):
        with allure.step("Отправляем запрос на создание заказа с ингредиентами"):
            response = requests.post(
                urls.ORDERS_URL,
                headers={"Authorization": auth_token},
                json={"ingredients": ingredient_ids[:1]}
            )
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        with allure.step("Отправляем запрос на создание заказа без ингредиентов"):
            response = requests.post(
                urls.ORDERS_URL,
                headers={"Authorization": auth_token},
                json={"ingredients": []}
            )
        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, auth_token):
        with allure.step("Отправляем запрос на создание заказа с неверным хешем"):
            response = requests.post(
                urls.ORDERS_URL,
                headers={"Authorization": auth_token},
                json={"ingredients": ["invalid_hash"]}
            )
        assert response.status_code in (400, 500)
        assert response.json()["success"] is False