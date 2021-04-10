from unittest import TestCase, main

from ifood.service import AuthenticationService, OrderService
from ifood.exception import IfoodException
from ifood.model import Token

class AuthenticationTest(TestCase):

    # Return a token object
    def test_should_return_auth_object(self):
        service = AuthenticationService(client_id='',
                                        client_secret='',
                                        grant_type='client_credentials')
        service.execute()
        self.token = service.token
        self.assertTrue(isinstance(service.token, Token), True)

    # Validate if returns a class of exception on Error
    def test_should_return_error_ifood_exception(self):
        service = AuthenticationService(client_id='wrong',
                                        client_secret='wrong',
                                        grant_type='client_credentials')
        with self.assertRaises(IfoodException):
            service.execute()
