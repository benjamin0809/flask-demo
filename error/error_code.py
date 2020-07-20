from error.error import APIException


class ServerError(APIException):
    code = 500
    msg = "server is invalid"
    error_code = 999
    data = ''


class ClientTypeError(APIException):
    code = 400
    msg = "client is invalid"
    error_code = 1006
    data = ''


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
    data = ''


class AuthFailed(APIException):
    code = 401
    msg = 'invalid parameter'
    error_code = 1001
    data = ''


class ValError(APIException):
    code = 404
    msg = 'invalid parameter'
    error_code = 1001
    data = ''

