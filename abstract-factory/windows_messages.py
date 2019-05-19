from abstract_classes import (
    AbstractMessagesFactory,
    AbstractGreetings,
    AbstractFarewell,
)


class WindowsGreetings(AbstractGreetings):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'{self.name}, choose quick or get outta here')


class WindowsFarewell(AbstractFarewell):
    def __init__(self, name):
        self.name = name

    def bye(self):
        print(f'From this moment {self.name} in a blacklist')


class WindowsMessagesFactory(AbstractMessagesFactory):

    def create_greetings(self, name) -> WindowsGreetings:
        return WindowsGreetings(name)

    def create_farewell(self, name) -> WindowsFarewell:
        return WindowsFarewell(name)
