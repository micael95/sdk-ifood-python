import json

import requests
from ..repository import BaseRepository
from ..model import Token
from ..exception import IfoodException

class BaseService:
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    APP_URL_ENCODED = 'application/x-www-form-urlencoded'
    APP_JSON = 'application/json'

    def __init__(self):
        self.token: Token = None

    def execute(self):
        raise NotImplementedError("Not implemented")

    def get_uri(self):
        return "{}".format(BaseRepository.base_url)

    def send_request(self, method, body=None, application=APP_JSON):
        headers = {"Accept": "application/json",
                   "Content-Type": application,
                   "Authorization": "Bearer {}".format(str(self.token))}
        response = getattr(requests, method)(self.get_uri(), data=body, headers=headers)
        if response.status_code >= 400:
            error = response.json()
            raise IfoodException(response.status_code, error)
        if response.status_code > 201:
            return None

        return response.json()
