from abc import ABC, abstractmethod


class AbstractMessages(ABC):
    pass


class AbstractGreetings(AbstractMessages):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def hello(self) -> None:
        pass


class AbstractFarewell(AbstractMessages):
    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def bye(self) -> None:
        pass


class AbstractMessagesFactory(ABC):
    @abstractmethod
    def create_greetings(self, name) -> AbstractGreetings:
        pass

    @abstractmethod
    def create_farewell(self, name) -> AbstractFarewell:
        pass
