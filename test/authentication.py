from unittest import TestCase, main

from src.ifood.service import AuthenticationService, OrderService
from src.ifood.exception import IfoodException
from src.ifood.model import Token

class AuthenticationTest(TestCase):

    # Return a token object
    def test_should_return_auth_object(self):
        service = AuthenticationService(client_id='8c692442-e77e-4d32-bb0b-a3d36fe06f25',
                                        client_secret='al27wvtjt3x2sfewrlkdtpukh7yt1au9soqdl11ygoajrem3n7srbnltejpnjf2xltpwsvz1lz5wz1wg4wz27j0tauug4zd2j8t',
                                        grant_type='client_credentials')
        service.execute()
        self.token = service.token
        print(self.token)
        self.assertTrue(isinstance(service.token, Token), True)

    # Validate if returns a class of exception on Error
    def test_should_return_error_ifood_exception(self):
        service = AuthenticationService(client_id='wrong',
                                        client_secret='wrong',
                                        grant_type='client_credentials')
        with self.assertRaises(IfoodException):
            service.execute()
