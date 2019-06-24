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
    def set_next(self, login_handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractLogin(LoginHandler):

    _next_handler = None

    def set_next(self, login_handler):
        self._next_handler = login_handler
        return login_handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Identification(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        if login in data:
            request['identified'] = True
            return super().handle(request)
        raise Exception('There is no customer with this login!')


class Authentication(AbstractLogin):
    def handle(self, request):
        if not request.get('identified', False):
            raise Exception('Identification is required')

        login = request.get('login')
        password = request.get('password')
        customer = data.get(login)

        if password == customer['password']:
            request['authenticated'] = True
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
