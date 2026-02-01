import json
import pytest
from pathlib import Path
import requests



CONFIG = json.loads(Path('config.json').read_text())
BASE_URL = CONFIG['BASE_URL']



class TestUsersApiGet:
    def test_get_single_user_live(self):
        url = f"{BASE_URL}/users/2"
        response = requests.get(url, timeout=10)
        assert response.status_code == 200, (
            f"Expected 200 but got {response.status_code}. "
            f"URL: {url}\n"
            f"Response headers: {response.headers}\n"
            
            f"Body (first 500 chars): {response.text[:500]}"
        )
        data = response.json()
        print(data)
        print(url)
        assert data["id"] == 2

    
    def test_get_multi_users_live(self):
        url = f"{BASE_URL}/users"
        resp = requests.get(url, timeout=10)
        assert resp.status_code == 200, (
            f"Expected 200 but got {resp.status_code}. "
            f"URL: {url}\n"
            f"Response headers: {resp.headers}\n"
            f"Body (first 500 chars): {resp.text[:500]}"
        )
        payload = resp.json()
        print("Data: {}".format(payload))
        print("Absolute URL: {}".format(url))


    
    def test_get_user_with_headers(self):
        url = f"{BASE_URL}/users"

        headers = {
            "Accept": "application/json"
        }

        response = requests.get(url, headers=headers)
        print("URL: {}".format(response.json()))
        assert response.status_code == 200
        assert response.headers["Content-Type"].startswith("application/json")

    

    """
        Query parameters filter, sort, or paginate data.  :- /users?page=2&limit=10
        ✅ When to Use
            Pagination
            Searching
            Filtering
            Sorting

        

    """

    def test_get_users_with_query_parameters(self):
        url = f"{BASE_URL}/posts"
        params = {
            "_start": 2,
            "_limit": 4
        }
        response = requests.get(url, params=params)
        json_response_data = response.json()
        assert response.status_code ==  200
        for item in json_response_data:
            assert 'id' in item
            assert 'title' in item
        print("Data:- {}".format(json_response_data))
        print("Complete URL: {}".format(url))
        assert len(json_response_data) == 4




"""
    ✅ What is Request Body?

    The request body sends data to the server (mainly for:
        POST
        PUT
        PATCH)
    Formats:
        JSON (most common)
        XML
        Form-data

    
    {
        "name": "Subrit",
        "job": "QA Automation Engineer"
    }

"""


class TestUsersApiPost:
    def test_user_post_data(self):
        url = f"{BASE_URL}/users"
        payload = {
            "id": 11,
            "name": "Ganesh Malepati",
            "username": "malepati.ganesh",
            "email": "malepatiganesh3@gmail.com",
            "job": "SDET"
        }
        headers = {
            "Content-type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        assert response.status_code == 201
        assert response.json()["name"] == "Ganesh Malepati"
        print("\nData:- {}".format(response.json()))
    







"""
    Authentication verifies who you are.
    
    ✅ Common Authentication Types
        Type	            Usage
        API Key	            Simple services
        Basic Auth	        Username & password
        Bearer Token	    OAuth / JWT
        OAuth 2.0	        Enterprise APIs
    
        
"""

from requests.auth import HTTPBasicAuth


class TestUserApiAuthentication:
    @pytest.mark.skip
    def test_user_data_basic_authentication(self):
        url = "https://httpbin.org/basic-auth/user/pass"
        response = requests.get(
            url,
            auth=HTTPBasicAuth("user", "pass") 
            )
        assert response.status_code == 200
        print("\nData:- {}".format(response.json()))

    @pytest.mark.skip
    def test_user_bearer_token_auth(auth_token):
        url = "https://api.example.com/protected"
        headers = {
            "Authorization": f"Bearer your access token: {auth_token}"
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200


    @pytest.mark.skip
    def test_user_not_found(self):
        """
            Negative Testing
        """
        response = requests.get("https://reqres.in/api/users/9999")
        assert response.status_code == 404

    
    def test_get_posts(self, auth_http_url_request):
        response = requests.get(f"{auth_http_url_request}/posts")
        assert response.status_code == 200


    




class TestJsonDataValidation:
    def test_response_body_json(self, auth_http_url_request):
        response = requests.get(f"{auth_http_url_request}/users")

        body = response.json()
        for element in body:
            assert "email" in element


    
    def test_complete_response_validation(self, auth_http_url_request):
        response = requests.get(f"{auth_http_url_request}/users", timeout=10)

        # Status Code
        assert response.status_code == 200
        print("Status Code: {}".format(response.status_code))

        # Headers
        assert response.headers["Content-Type"].startswith("application/json")
        print("Content-Type: {}".format(response.headers))

        # Body
        body = response.json()
        print("Data: {}".format(body))
        for item in body:
            assert "id" in item
            assert "username" in item

        # Response Time
        assert response.elapsed.total_seconds() < 2
        print("Reponse Time: {}".format(response.elapsed.total_seconds()))

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_users_with_parametarize(self, auth_http_url_request, user_id):
        response = requests.get(f"{auth_http_url_request}/users/{user_id}")
        assert response.status_code == 200
        print("Overall Data: {}".format(response.json()))
        print("Absolute URL: {}".format(response.url))




