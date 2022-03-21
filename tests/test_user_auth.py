from cmath import log
import requests
import pytest

from lib.base_case import BaseCase
from lib.asseritons import Assertions
from lib.my_requests import MyRequests


class TestUserAuth(BaseCase):
    expected_params = [
        ("no_cookies"),
        ("no_headers")
    ]

    def setup(self):
        payload = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        login_response = MyRequests.post("/user/login", data=payload)

        Assertions.assert_status_code(login_response, 200)

        self.auth_sid = self.get_cookie(login_response, "auth_sid")
        self.x_csrf_token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_auth = self.get_json_value(login_response, "user_id")

    def test_positive_user_auth(self):
        response = MyRequests.get("/user/auth", 
                                        cookies={"auth_sid": self.auth_sid}, 
                                        headers={"x-csrf-token": self.x_csrf_token})
        
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            self.user_id_from_auth,
            f"Wrong user id in response. Got {self.user_id_from_auth}"
        )

    @pytest.mark.parametrize("condition", expected_params)
    def test_negative_user_auth(self, condition):
        if condition == "no_cookies":
            response = MyRequests.get("/user/auth", headers={"x-csrf-token": self.x_csrf_token})
        else:
            response = MyRequests.get("/user/auth", cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(
            response,
            "user_id",
            0,
            "Authorized with no cookes and headers."
        )
