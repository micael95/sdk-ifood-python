from ..utils import auto_str

@auto_str
class IfoodException(Exception):
    def __init__(self, code, message):
        super(IfoodException, self).__init__(message)
        self.code = code
