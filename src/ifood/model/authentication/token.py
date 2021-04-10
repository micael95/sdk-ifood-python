from ifood.utils import auto_str
from ifood.serializer import IfoodSerializable


class Token(IfoodSerializable):

    def __init__(self):
        self.access_token = None
        self.type = None
        self.expires_in = None

    def __str__(self) -> str:
        return "{}".format(self.access_token)

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Token()
        for k, v in dict.items():
            setattr(instance, IfoodSerializable.camel_to_snake(k), v)
        return instance
