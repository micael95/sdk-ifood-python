import json
import re


class IfoodSerializable:
    def to_json(self):
        return json.dumps(self.serialize(), cls=RecursiveEncoder)

    @staticmethod
    def camel_to_snake(name):
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

    def serialize(self):
        dict = {k: v for k, v in self.__dict__.items() if v is not None}

        for k, v in dict.items():
            if hasattr(v, "serialize"):
                dict[k] = v.serialize()

        return dict


class RecursiveEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'serialize'):
            return obj.serialize()
        else:
            return json.JSONEncoder.default(self, obj)
