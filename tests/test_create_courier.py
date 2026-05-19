import pytest
import allure
import api_requests
import helpers
from data import ResponseBody
#python -B -m pytest tests/create_courier.py

class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    @allure.description("""
                        1. запрос возвращает код ответа 201;
                        2. запрос возвращает {"ok": True}
                        """)
    def test_create_courier_succeed(self):
        response = api_requests.create_courier(helpers.create_courier_payload(login=None, password=None, firstName=None))
        assert response.status_code == 201
        assert response.json() == ResponseBody.create_courier_code_201

#Все тесты ниже будут Fail из-за несоответствия тела ответа в документации и в реализации,
#поэтому далее во избежании будет ипользован ответ как в реализации (см. разницу в data)
    
    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description("""
                        1. запрос возвращает код ответа 409;
                        2. запрос возвращает {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
                        """)
    def test_create_two_identical_couriers(self):
        body = helpers.create_courier_payload(login=None, password=None, firstName=None)
        api_requests.create_courier(body)
        response_2 = api_requests.create_courier(body)
        assert response_2.status_code == 409
        assert response_2.json() == ResponseBody.create_courier_code_409_release


    @allure.title('Создание курьера без передачи логина')
    @allure.description("""
                        1. запрос возвращает код ответа 400;
                        2. запрос возвращает {"code": 400,"message": "Недостаточно данных для создания учетной записи"}
                        """)
    def test_create_courier_without_login(self):
        response = api_requests.create_courier(helpers.create_courier_payload(password=None, firstName=None))
        assert response.status_code == 400
        assert response.json() == ResponseBody.create_courier_code_400_release


    @allure.title('Создание курьера без передачи пароля')
    @allure.description("""
                        1. запрос возвращает код ответа 400;
                        2. запрос возвращает {"code": 400,"message": "Недостаточно данных для создания учетной записи"}
                        """)
    def test_create_courier_without_password(self):
        response = api_requests.create_courier(helpers.create_courier_payload(login=None, firstName=None))
        assert response.status_code == 400
        assert response.json() == ResponseBody.create_courier_code_400_release


    @allure.title('Создание курьера c уже существующим логином логином')
    @allure.description("""
                        1. запрос возвращает код ответа 409;
                        2. запрос возвращает {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
                        """)
    def test_create_courier_with_same_login(self):
        api_requests.create_courier(helpers.create_courier_payload(login="ninja", password=None, firstName=None))
        response_2 = api_requests.create_courier(helpers.create_courier_payload(login="ninja", password=None, firstName=None))
        assert response_2.status_code == 409
        assert response_2.json() == ResponseBody.create_courier_code_409_release