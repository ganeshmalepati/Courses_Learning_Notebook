import pytest
import requests


@pytest.fixture(scope="session")
def auth_token():
    url = "https://reqres.in/api/login"
    response = requests.post(
        url, 
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )
    return response.json()["token"]


@pytest.fixture(scope="class")
def auth_http_url_request():
    return "https://jsonplaceholder.typicode.com/"
