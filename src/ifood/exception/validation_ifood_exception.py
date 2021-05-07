from ..utils import auto_str

@auto_str
class ValidationIfoodException(Exception):
    def __init__(self, code, message):
        super(ValidationIfoodException, self).__init__(message)
        self.code = code
