from enum import Enum


class BaseRepository:
    base_url = "https://merchant-api.ifood.com.br"


class AuthenticationRepository(BaseRepository):
    oauthTokenV1 = "/authentication/v1.0/oauth/token"
    oauthUserCodeV1 = "/authentication/v1.0/oauth/userCode"


class OrderRepository(BaseRepository):
    pass


class FinancialRepository(BaseRepository):
    pass


class MerchantRepository(BaseRepository):
    pass


class CatalogRepository(BaseRepository):
    pass
