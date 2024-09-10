import pytest
import requests

URL = "https://x-clients-be.onrender.com"

@pytest.fixture()
def get_token(username='leonardo', password='leads'):
    auth = {
        'username': username,
        'password': password
    }
    resp_token = requests.post(URL + '/auth/login', json=auth)
    token = resp_token.json()['userToken']
    return token