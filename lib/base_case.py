from requests import Response
from json.decoder import JSONDecodeError


class BaseCase:

    def get_cookie(self, response: Response, cookie_name: str):
        assert cookie_name in response.cookies, f"Response has no cookie witn name '{cookie_name}'."
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name: str):
        assert header_name in response.headers, f"Response has no headers with name '{header_name}'."
        return response.headers[header_name]

    def get_json_value(self, response: Response, key_name: str):
        try:
            response_json = response.json()
        except JSONDecodeError:
            assert False, "Response from the serve has no JSON format."
        
        assert key_name in response_json, f"Response has no key with name '{key_name}'"
        return response_json[key_name]