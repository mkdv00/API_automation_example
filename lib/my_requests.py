from email import header
import requests


class MyRequests:
    @staticmethod
    def get(endpoint: str, params: dict=None, headers=None, cookies=None):
        return MyRequests._send(endpoint=endpoint, data=params, headers=headers, cookies=cookies, method='GET')

    @staticmethod
    def post(endpoint: str, data: dict=None, headers=None, cookies=None):
        return MyRequests._send(endpoint=endpoint, data=data, headers=headers, cookies=cookies, method='POST')

    @staticmethod
    def put(endpoint: str, data: dict=None, headers=None, cookies=None):
        return MyRequests._send(endpoint=endpoint, data=data, headers=headers, cookies=cookies, method='PUT')

    @staticmethod
    def delete(endpoint: str, data: dict=None, headers=None, cookies=None):
        return MyRequests._send(endpoint=endpoint, data=data, headers=headers, cookies=cookies, method='DELEETE')

    @staticmethod
    def _send(endpoint: str, data: dict, headers: dict, cookies: str, method: str):
        url = f"https://playground.learnqa.ru/api{endpoint}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad method {method}. Type: 'GET'/'POST'/'PUT or 'DELETE'.")
        return response
