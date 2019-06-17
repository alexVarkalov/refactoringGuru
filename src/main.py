from login_classes import (
    LoginHandler,
    Identification,
    Authentication,
    Authorization,
)


def client_code(login_handler: LoginHandler):
    login = input('Your login --> ')
    password = input('Your password --> ')
    request = {
        'login': login,
        'password': password,
    }
    try:
        permissions = login_handler.handle(request)
        print(permissions)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    identification = Identification()
    authentication = Authentication()
    authorization = Authorization()
    identification.set_next(authentication).set_next(authorization)
    client_code(identification)
