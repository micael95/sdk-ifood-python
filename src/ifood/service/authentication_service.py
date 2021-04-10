from .base_service import BaseService
from ifood.repository import AuthenticationRepository
from ifood.model import Token


class AuthenticationService(BaseService):
    def __init__(self, client_id, client_secret, grant_type):
        super(AuthenticationService, self).__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type

    def get_uri(self):
        return "{}{}".format(super().get_uri(), AuthenticationRepository.oauthTokenV1)

    def execute(self):
        response = self.send_request(
            AuthenticationService.POST,
            {
                'clientId': self.client_id,
                'clientSecret': self.client_secret,
                'grantType': self.grant_type

            }, self.APP_URL_ENCODED)

        self.token = Token.unserialize(response)
