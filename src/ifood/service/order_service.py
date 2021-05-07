import json
from typing import List

from ..model import Order, OrderEvent,Token
from ..exception import ValidationIfoodException
from ..repository import OrderRepository
from ..service import BaseService

# Just requests to module Order
class OrderService(BaseService):

    def __init__(self, token: Token):
        super(OrderService, self).__init__()
        self.uri = None
        self.token = token

    def get_events_polling(self) -> List[OrderEvent]:
        self.uri = OrderRepository.eventsPollingV1
        response = self.send_request(self.GET, None, self.APP_JSON)
        if response is None:
            return []
        result_list = []
        for d in response:
            event = OrderEvent.unserialize(d)
            result_list.append(event)
        return result_list

    def get_order_details(self, id: str) -> Order:
        self.uri = OrderRepository.orderDetailsV1.format(id)
        response = self.send_request(self.GET, None, self.APP_JSON)
        return Order.unserialize(response)

    # Statuses order

    def post_order_confirm(self, id: str):
        self.uri = OrderRepository.orderConfirmV1.format(id)
        self.send_request(self.POST, None, self.APP_JSON)

    def post_order_ready_to_pickup(self, id: str):
        self.uri = OrderRepository.orderReadyToPickUpV1.format(id)
        self.send_request(self.POST, None, self.APP_JSON)

    def post_order_dispatch(self, id: str):
        self.uri = OrderRepository.orderDispatchV1.format(id)
        self.send_request(self.POST, None, self.APP_JSON)

    def post_order_accept_cancellation(self, id: str):
        self.uri = OrderRepository.orderAcceptCancellationV1.format(id)
        self.send_request(self.POST, None, self.APP_JSON)

    def post_order_deny_cancellation(self, id: str):
        self.uri = OrderRepository.orderDenyCancellationV1.format(id)
        self.send_request(self.POST, None, self.APP_JSON)

    def post_order_request_cancellation(self, id: str, reason: str, cancellation_code: str = "801"):
        self.uri = OrderRepository.orderRequestCancellationV1.format(id)
        self.send_request(self.POST, json.dumps({'reason': reason, 'cancellationCode': cancellation_code}), self.APP_JSON)

    # The documentation says that we have to send a list of events, but i made one for one at the moment
    def post_events_ack(self, event: OrderEvent):
        if not isinstance(event, OrderEvent):
            raise ValidationIfoodException('wrong-instance', 'Required an OrderEvent object')

        self.uri = OrderRepository.eventsAckV1
        self.send_request(self.POST, json.dumps([json.loads(event.to_json())]), self.APP_JSON)

    def get_uri(self):
        return "{}{}".format(super().get_uri(), self.uri)
