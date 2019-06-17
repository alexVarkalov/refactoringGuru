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
        return request


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


class Authorization(AbstractLogin):
    def handle(self, request):
        login = request.get('login')
        customer = data.get(login)
        role = customer.get('role')
        #todo add other chain for permissions
        if role == 'Admin':
            permissions = ['Create', 'Read', 'Update', 'Delete']
        elif role == 'Moderator':
            permissions = ['Create', 'Read']
        elif role == 'User':
            permissions = ['Read']
        else:
            permissions = []
        request['permissions'] = permissions
        return super().handle(request)

