from messages_factories.abstract_messages import (
    AbstractMessagesFactory,
    AbstractGreetings,
    AbstractFarewell,
)


class WindowsGreetings(AbstractGreetings):
    def __init__(self, name:str) -> None:
        self.name = name

    def hello(self) -> None:
        print(f'{self.name}, choose quick or get outta here')


class WindowsFarewell(AbstractFarewell):
    def __init__(self, name:str) -> None:
        self.name = name

    def bye(self) -> None:
        print(f'From this moment {self.name} in a blacklist')


class WindowsMessagesFactory(AbstractMessagesFactory):

    def create_greetings(self, name) -> AbstractGreetings:
        return WindowsGreetings(name)

    def create_farewell(self, name) -> AbstractFarewell:
        return WindowsFarewell(name)
