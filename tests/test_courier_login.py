import pytest
import allure
import api_requests
import helpers
from data import ResponseBody

class TestCourierLogin:
    @allure.title('Успешная авторизация курьера')
    @allure.description("""
                        1. запрос возвращает код ответа 200;
                        2. запрос возвращает id
                        """)
    def test_login_courier_succeed(self, created_courier_fixture):
        body = created_courier_fixture(login=None, password=None)
        api_requests.create_courier(body)
        response_2= api_requests.login_courier(body)
        assert response_2.status_code == 200
        assert 'id' in response_2.text

    @allure.title('Авторизация курьера без логина')
    @allure.description("""
                        1. запрос возвращает код ответа 400;
                        2. запрос возвращает {"code": 400,"message": "Недостаточно данных для входа"}
                        """)
    def test_login_courier_without_login(self, created_courier_fixture):
        body = created_courier_fixture(login='', password=None)
        api_requests.create_courier(body)
        response_2= api_requests.login_courier(body)
        assert response_2.status_code == 400
        assert response_2.json() == ResponseBody.login_courier_code_400_release

    @allure.title('Авторизация курьера без пароля')
    @allure.description("""
                        1. запрос возвращает код ответа 400;
                        2. запрос возвращает {"code": 400,"message": "Недостаточно данных для входа"}
                        """)
    def test_login_courier_without_password(self, created_courier_fixture):
        body = created_courier_fixture(login=None, password='')
        api_requests.create_courier(body)
        response_2= api_requests.login_courier(body)
        assert response_2.status_code == 400
        assert response_2.json() == ResponseBody.login_courier_code_400_release

    @allure.title('Авторизация курьера c некорректным логином')
    @allure.description("""
                        1. запрос возвращает код ответа 404;
                        2. запрос возвращает {"code": 404,"message": "Учетная запись не найдена"}
                        """)
    def test_login_courier_with_wrong_login(self, created_courier_fixture):
        body_with_correct_login = created_courier_fixture(login='ninja', password='1234')
        body_with_wrong_login = created_courier_fixture(login='ninja_11', password='1234')
        api_requests.create_courier(body_with_correct_login)
        response_2= api_requests.login_courier(body_with_wrong_login)
        assert response_2.status_code == 404
        assert response_2.json() == ResponseBody.login_courier_code_404_release

    @allure.title('Авторизация курьера c некорректным паролем')
    @allure.description("""
                        1. запрос возвращает код ответа 404;
                        2. запрос возвращает {"code": 404,"message": "Учетная запись не найдена"}
                        """)
    def test_login_courier_with_wrong_password(self, created_courier_fixture):
        body_with_correct_login = created_courier_fixture(login='ninja', password='1234')
        body_with_wrong_login = created_courier_fixture(login='ninja', password='12347')
        api_requests.create_courier(body_with_correct_login)
        response_2= api_requests.login_courier(body_with_wrong_login)
        assert response_2.status_code == 404
        assert response_2.json() == ResponseBody.login_courier_code_404_release

    @allure.title('Авторизация курьера c несуществующим логином и паролем')
    @allure.description("""
                        1. запрос возвращает код ответа 404;
                        2. запрос возвращает {"code": 404,"message": "Учетная запись не найдена"}
                        """)
    def test_login_courier_with_nonexistent_login_and_password(self):
        body = helpers.create_courier_payload(login=None, password=None)
        response_2= api_requests.login_courier(body)
        assert response_2.status_code == 404
        assert response_2.json() == ResponseBody.login_courier_code_404_release