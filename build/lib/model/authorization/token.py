from src import IfoodSerializable


class Token(IfoodSerializable):

    def __init__(self):
        self.accessToken = None
        self.type = None
        self.expiresIn = None

    def __str__(self) -> str:
        return "{} , {} , {}".format(self.accessToken, self.type, self.expiresIn)

    @staticmethod
    def unserialize(dict=None):
        if dict is None:
            dict = {}

        instance = Token()
        for k, v in dict.items():
            setattr(instance, k, v)
        return instance