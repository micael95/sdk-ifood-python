class BaseRepository:
    base_url = "https://merchant-api.ifood.com.br"


class AuthenticationRepository(BaseRepository):
    oauthTokenV1 = "/authentication/v1.0/oauth/token"
    oauthUserCodeV1 = "/authentication/v1.0/oauth/userCode"


class OrderRepository(BaseRepository):
    eventsPollingV1 = "/order/v1.0/events:polling"
    eventsAckV1 = "/order/v1.0/events/acknowledgment"
    orderDetailsV1 = "/order/v1.0/orders/{}"
    orderConfirmV1 = "/order/v1.0/orders/{}/confirm"
    orderReadyToPickUpV1 = "/order/v1.0/orders/{}/readyToPickup"
    orderDispatchV1 = "/order/v1.0/orders/{}/dispatch"
    orderRequestCancellationV1 = "/order/v1.0/orders/{}/requestCancellation"
    orderAcceptCancellationV1 = "/order/v1.0/orders/{}/acceptCancellation"
    orderDenyCancellationV1 = "/order/v1.0/orders/{}/denyCancellation"

class FinancialRepository(BaseRepository):
    pass


class MerchantRepository(BaseRepository):
    pass


class CatalogRepository(BaseRepository):
    pass
