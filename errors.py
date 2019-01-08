
class BaseError(Exception):
    message = None
    code = None


class AccountDoesNotExist(BaseError):
    message = 'The specified account does not exist'
    code = 400


class ApiKeyExpired(BaseError):
    message = 'The API key is expired'
    code = 401


class DataError(BaseError):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class JsonError(BaseError):
    message = 'failed of decoding json'
    code = 402


class ServerError(BaseError):
    message = 'The server has encountered a situation it doesnt know how to handle.'
    code = 500
