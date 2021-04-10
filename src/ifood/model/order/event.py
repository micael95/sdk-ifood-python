from datetime import datetime
from uuid import UUID
from ifood.serializer import IfoodSerializable
from ifood.utils import auto_str

from uuid import UUID


@auto_str
class Consumer(IfoodSerializable):
    financial_occurrence: str
    payment_type: str

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Consumer()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance

@auto_str
class CancellationOccurrence(IfoodSerializable):
    restaurant: Consumer
    consumer: Consumer
    logistic: Consumer

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = CancellationOccurrence()
        for k, v in dict.items():
            if k == "RESTAURANT":
                instance.restaurant = Consumer.unserialize(v)
                continue
            if k == "CONSUMER":
                instance.consumer = Consumer.unserialize(v)
                continue
            if k == "LOGISTIC":
                instance.logistic = Consumer.unserialize(v)
                continue

            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance

@auto_str
class Metadata(IfoodSerializable):
    cancel_stage: str
    cancel_code: int
    cancellation_occurrence: CancellationOccurrence
    timeout_event: bool
    cancel_origin: str
    cancel_user: str
    cancel_reason: str
    cancellation_requested_event_id: UUID

    def __init__(self) -> None:
        pass

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Metadata()
        for k, v in dict.items():

            if k == "CANCELLATION_OCCURRENCE":
                instance.cancellation_occurrence = CancellationOccurrence.unserialize(v)
                continue

            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class OrderEvent(IfoodSerializable):
    created_at: datetime
    full_code: str
    metadata: Metadata
    code: str
    order_id: UUID
    id: UUID

    def __init__(self, created_at: datetime = None, full_code: str = None, metadata: Metadata = None, code: str = None,
                 order_id: UUID = None, id: UUID = None) -> None:
        self.created_at = created_at
        self.full_code = full_code
        self.metadata = metadata
        self.code = code
        self.order_id = order_id
        self.id = id

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = OrderEvent()
        for k, v in dict.items():

            if k == "metadata":
                instance.metadata = Metadata.unserialize(v)
                continue
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance
