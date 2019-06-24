from login_classes import (
    LoginHandler,
    Identification,
    Authentication,
    AdminAuthorization,
    ModeratorAuthorization,
    UserAuthorization,
)


def get_admin_auth_chain():
    identification = Identification()
    authentication = Authentication()
    authorization = AdminAuthorization()
    identification.set_next(authentication).set_next(authorization)
    return identification


def get_moderator_auth_chain():
    identification = Identification()
    authentication = Authentication()
    authorization = ModeratorAuthorization()
    identification.set_next(authentication).set_next(authorization)
    return identification


def get_user_auth_chain():
    identification = Identification()
    authentication = Authentication()
    authorization = UserAuthorization()
    identification.set_next(authentication).set_next(authorization)
    return identification


def client_code(login_handler: LoginHandler):
    login = input('Your login --> ')
    password = input('Your password --> ')
    request = {
        'login': login,
        'password': password,
    }
    try:
        login_handler.handle(request)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    auth = get_admin_auth_chain()
    # auth = get_moderator_auth_chain()
    # auth = get_user_auth_chain()
    client_code(auth)
