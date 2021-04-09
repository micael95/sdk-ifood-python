import json

import requests
from src import IfoodException
from src.repository.url_repository import BaseRepository


class BaseService:
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"

    def __init__(self):
        pass

    def execute(self):
        raise NotImplementedError("Not implemented")

    def get_uri(self):
        return "{}/".format(BaseRepository.base_url)

    def send_request(self, method, body=None):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/x-www-form-urlencoded"}

        response = getattr(requests, method)(self.get_uri(), data=body, headers=headers)

        if response.status_code >= 400:
            error = response.json()
            raise IfoodException(error, response.status_code)

        return response.json()
