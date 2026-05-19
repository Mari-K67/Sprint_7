import pytest
import allure
import api_requests
import helpers
from data import OderInformation
#python -B -m pytest tests/test_create_oder.py

class TestCreateOder:
    @allure.title('Проверка создания заказа в зависимости от выбранного цвета')
    @allure.description("""
                        1. запрос возвращает код ответа 201;
                        2. запрос возвращает track
                        """)
    @pytest.mark.parametrize("color", [
        OderInformation.color_black,
        OderInformation.color_grey,
        OderInformation.bouth_color,
        OderInformation.empty_color
    ])
    def test_create_oder(self, color):
        response= api_requests.create_oder(helpers.create_oder_payload(color))
        assert response.status_code == 201
        assert 'track' in response.text