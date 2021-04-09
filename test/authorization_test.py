from unittest import TestCase

from src import AuthenticationBaseService, IfoodException
from src.model.authorization.token import Token


class AuthorizationTest(TestCase):
    token = None

    # Return a token object
    def testShouldReturnTokenObject(self):
        service = AuthenticationBaseService(client_id='9539f566-38cc-4aca-adbc-51636e08b296',
                                            client_secret='wj46d9vvwa0rxda44nqdqbe2xrs1beg9nogqxuq3er2z3kvedt3js3x8wez98x8uqr5j1fyz42npjf8mefoetyt4csnze4g173i',
                                            grant_type='client_credentials')
        response = service.execute()
        self.token = Token.unserialize(response)

        self.assertTrue(isinstance(self.token, Token), True)

    # Validate if returns a class of exception on Error
    def testShouldReturnIfoodException(self):
        service = AuthenticationBaseService(client_id='9539f566-38cc-4aca-adbc-51636e08b296',
                                            client_secret='wj46d9vvwa0rxda44nqdqbe2xrs1beg9nogqxuq3er2z3kvedt3js3x8wez98x8uqr5j1fyz42npjf8mefoetyt4csnze4g173',
                                            grant_type='client_credentials')
        with self.assertRaises(IfoodException):
            response = service.execute()
