import pytest
import requests
from Lesson8.websait import URL

@pytest.fixture()
def get_token(username='leonardo', password='leads'):
    auth = {
        'username': username,
        'password': password
    }
    resp_token = requests.post(URL + '/auth/login', json=auth)
    token = resp_token.json()['userToken']
    return token