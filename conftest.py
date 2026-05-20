import pytest
import api_requests
import helpers


@pytest.fixture
def created_courier_fixture():
    created = []
    def _create_courier(**fields):
        body = helpers.create_courier_payload(**fields)
        created.append(body)
        return body

    yield _create_courier

    for body in created:
        login_response = api_requests.login_courier(body)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            api_requests.delete_courier(courier_id)
