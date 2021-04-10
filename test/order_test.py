from unittest import TestCase

from ifood.service import OrderService, IfoodService

class OrderTest(TestCase):

    def setUp(self) -> None:
        self.service = IfoodService(
            client_id='',
            client_secret='',
            grant_type='client_credentials'
        )

    def test_should_return_events_polling(self):
        event_list = self.service.order.get_events_polling()
        for event in event_list:

            if event.full_code == 'PLACED':
                self.service.order.get_order_details(event.order_id)
                self.service.order.post_order_request_cancellation(event.order_id,
                                                                   reason="Teste de integração com python")
            self.service.order.post_events_ack(event)
        self.assertTrue(True)
