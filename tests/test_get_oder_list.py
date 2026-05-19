import allure
import api_requests
#python -B -m pytest tests/get_oder_list.py

class TestGetOderList:
    @allure.title('Проверка, что тело возвращает список заказов')
    def test_create_oder(self):
        response = api_requests.get_oder_list()
        assert response.status_code == 200
        assert 'orders' in response.text