from ..service import AuthenticationService, OrderService, BaseService
from ..model import Token


class IfoodService(BaseService):

    def __init__(self, client_id: str, client_secret: str, grant_type='client_credentials'):
        self.grantType = grant_type
        self.clientId = client_id
        self.clientSecret = client_secret

        # Create a token instance
        self.credentials = AuthenticationService(client_id=client_id, client_secret=client_secret, grant_type=grant_type)
        self.credentials.execute()

        # Module Order
        self.order = OrderService(self.credentials.token)
