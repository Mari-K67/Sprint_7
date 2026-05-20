import requests
import allure
from data import Url


@allure.step('запрос на создание курьера')
def create_courier(body):
    return requests.post(Url.create_courier_url, data=body)

@allure.step('запрос на авторизацию курьера в системе (возвращает id)')
def login_courier(body):
    return requests.post(Url.courier_login_in_sistem_url, data=body)

@allure.step('запрос на создание заказа')
def create_oder(body):
    return requests.post(Url.create_oder_url, json=body)

@allure.step('запрос на получение списка заказов')
def get_oder_list():
    return requests.get(Url.get_oder_list_url)

@allure.step('запрос на удаление курьера')
def delete_courier(id):
    return requests.delete(f'{Url.delete_courier}{id}')