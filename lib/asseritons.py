from urllib import request
from requests import Response
from json.decoder import JSONDecodeError


class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, key_name: str, expected_result: str, error_msg: str):
        try:
            response_json = response.json()
        except JSONDecodeError:
            assert False, "Response has no format JSON."

        assert key_name in response_json, f"Response has no field '{key_name}'."
        assert response_json[key_name] == expected_result, error_msg

    @staticmethod
    def assert_json_has_key(response: Response, key_name: str):
        try:
            response_json = response.json()
        except JSONDecodeError:
            assert False, "Response has no format JSON."

        assert key_name in response_json, f"Response has no field '{key_name}'"

    @staticmethod
    def assert_status_code(response: Response, expected_status_code: int):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code. Expected - {expected_status_code}, Actual - {response.status_code}."
