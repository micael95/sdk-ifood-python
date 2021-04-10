from datetime import datetime
from uuid import UUID
from typing import List

from ifood.utils import auto_str
from ifood.serializer import IfoodSerializable


@auto_str
class Phone:
    number: str
    localizer: int
    localizer_expiration: datetime

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Phone()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Customer:
    id: UUID
    name: str
    document_number: str
    phone: Phone
    orders_count_on_merchant: int

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Customer()
        for k, v in dict.items():

            if k == 'phone':
                instance.phone = Phone.unserialize(v)
                continue

            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Coordinates:
    latitude: float
    longitude: float

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Coordinates()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class DeliveryAddress:
    street_name: str
    street_number: int
    formatted_address: str
    neighborhood: str
    complement: str
    postal_code: str
    city: str
    state: str
    country: str
    coordinates: Coordinates

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = DeliveryAddress()
        for k, v in dict.items():
            if k == "coordinates":
                instance.coordinates = Coordinates.unserialize(v)
                continue
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Delivery:
    mode: str
    delivered_by: str
    delivery_date_time: datetime
    delivery_address: DeliveryAddress

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Delivery()

        for k, v in dict.items():
            if k == "deliveryAddress":
                instance.delivery_address = DeliveryAddress.unserialize(v)
                continue
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)

        return instance


@auto_str
class Option:
    index: int
    id: UUID
    name: str
    unit: str
    quantity: int
    unit_price: float
    price: float

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Option()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Item:
    index: int
    id: UUID
    name: str
    external_code: str
    unit: str
    quantity: int
    unit_price: float
    price: float
    options_price: float
    total_price: float
    options: List[Option]

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Item()
        for k, v in dict.items():

            if k == "options":
                instance.options = []
                for u in dict.get("options", []):
                    instance.options.append(Option.unserialize(u))

                continue

            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Merchant:
    id: UUID
    name: str

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Merchant()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Cash:
    change_for: float

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Cash()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Method:
    value: float
    currency: str
    method: str
    type: str
    cash: Cash
    prepaid: bool

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Method()
        for k, v in dict.items():
            if k == 'cash':
                instance.cash = Cash.unserialize(v)
                continue
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Payments:
    prepaid: int
    pending: float
    methods: List[Method]

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Payments()
        for k, v in dict.items():
            if k == "methods":
                instance.methods = []

                for u in dict.get("methods", []):
                    instance.methods.append(Method.unserialize(u))

                continue
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Total:
    sub_total: float
    delivery_fee: float
    benefits: int
    order_amount: float

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}
        instance = Total()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance


@auto_str
class Order:
    id: UUID
    delivery: Delivery
    order_type: str
    order_timing: str
    display_id: int
    created_at: datetime
    preparation_start_date_time: datetime
    is_test: bool
    merchant: Merchant
    customer: Customer
    items: List[Item]
    sales_channel: str
    total: Total
    payments: Payments

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Order()

        for k, v in dict.items():
            if k == "delivery":
                instance.delivery = Delivery.unserialize(v)
                continue

            if k == "merchant":
                instance.merchant = Merchant.unserialize(v)
                continue

            if k == "customer":
                instance.customer = Merchant.unserialize(v)
                continue

            if k == "items":
                instance.items = []

                for u in dict.get("items", []):
                    instance.items.append(Item.unserialize(u))

                continue

            if k == "total":
                instance.total = Total.unserialize(v)

                continue

            if k == "payments":
                instance.payments = Payments.unserialize(v)

                continue

            setattr(instance, IfoodSerializable.camel_to_snake(k), v)

        return instance
