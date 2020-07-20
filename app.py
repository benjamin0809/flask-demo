from flask import Flask, request
from werkzeug.exceptions import HTTPException

from error.error import APIException
from error.error_code import ServerError

app = Flask(__name__)


@app.before_request
def  before_request():
    interface = request.path
    print(interface)


@app.errorhandler(Exception)
def framework_error(e):
    # 判断异常是不是APIException
    if isinstance(e, APIException):
        return e
    # 判断异常是不是HTTPException
    if isinstance(e, HTTPException):
        # log.error(e)
        code = e.code
        # 获取具体的响应错误信息
        msg = e.description
        error_code = 1007
        return APIException(code=code, msg=msg, error_code=error_code)
    # 异常肯定是Exception
    else:
        # 如果是调试模式,则返回e的具体异常信息。否则返回json格式的ServerException对象！
        # 针对于异常信息，我们最好用日志的方式记录下来。
        if app.config["DEBUG"]:
            # log.error(temp.format(info.f_code.co_filename, info.f_lineno, name, repr(e)))
            # log.error(e)
            return e
        else:
            # log.error(e)
            return ServerError()


@app.route('/')
def hello_world():
    test_error()
    return 'Hello World!'


def test_error():
    raise APIException('test')


if __name__ == '__main__':
    app.run()
