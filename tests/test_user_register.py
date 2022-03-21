import requests
from datetime import datetime

from lib.base_case import BaseCase
from lib.asseritons import Assertions
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    def setup(self):
        prefix = 'learnqa'
        domain = 'example.com'
        random_text = datetime.now().strftime("%d%m%Y%H%M%S")
        self.email = f"{prefix}{random_text}@{domain}"

    def test_create_user_succesfully(self):
        payload = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234',
            'email': self.email
        }

        response = MyRequests.post("/user/", data=payload)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, 'id')

    def test_regisrer_user_exist(self):
        email = 'vinkotov@example.com'
        payload = {
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234',
            'email': email
        }

        response = MyRequests.post("/user/", data=payload)

        Assertions.assert_status_code(response, 400)
        assert response.content.decode('utf-8') == f"Users with email '{email}' already exists", \
            f"Unexpected response {response.content}"
