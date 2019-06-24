from login_classes import (
    LoginHandler,
    Identification,
    Authentication,
    AdminAuthorization,
    ModeratorAuthorization,
    UserAuthorization,
)


def get_admin_auth_chain():
    return Identification(Authentication(AdminAuthorization()))


def get_moderator_auth_chain():
    return Identification(Authentication(ModeratorAuthorization()))


def get_user_auth_chain():
    return Identification(Authentication(UserAuthorization()))


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
    chain = get_admin_auth_chain()
    # chain = get_moderator_auth_chain()
    # chain = get_user_auth_chain()
    client_code(chain)
