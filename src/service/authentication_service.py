from src.service import BaseService
from src.repository.url_repository import AuthenticationRepository


class AuthenticationBaseService(BaseService):
    def __init__(self, client_id, client_secret, grant_type):
        super(AuthenticationBaseService, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    def get_uri(self):
        return "{}/{}".format(super().get_uri(), AuthenticationRepository.oauthTokenV1)

    def execute(self):
        return self.send_request(AuthenticationBaseService.POST, {
            'clientId': self.client_id,
            'clientSecret': self.client_secret,
            'grantType': self.grant_type
        })
