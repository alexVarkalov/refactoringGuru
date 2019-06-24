from abc import ABC, abstractmethod

data = {
    'alex': {
        'password': '1234',
        'role': 'Admin'
    },
    'bob': {
        'password': '1234',
        'role': 'Moderator'
    },
    'mike': {
        'password': '1234',
        'role': 'User'
    },
}


class LoginHandler(ABC):
    @abstractmethod
    def __init__(self, login_handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractLogin(LoginHandler):

    _next_handler = None

    def __init__(self, login_handler=None):
        self._next_handler = login_handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Identification(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        if login in data:
            return super().handle(request)
        raise Exception('There is no customer with this login!')


class Authentication(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        password = request.get('password')
        customer = data.get(login)

        if password == customer['password']:
            return super().handle(request)
        raise Exception('Wrong password')


class AdminAuthorization(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        customer = data.get(login)
        role = customer.get('role')
        if role != 'Admin':
            raise Exception('Access denied')
        return super().handle(request)


class ModeratorAuthorization(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        customer = data.get(login)
        role = customer.get('role')
        if role != 'Moderator':
            raise Exception('Access denied')
        return super().handle(request)


class UserAuthorization(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        customer = data.get(login)
        role = customer.get('role')
        if role != 'User':
            raise Exception('Access denied')
        return super().handle(request)
