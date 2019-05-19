from abc import ABC, abstractmethod


class AbstractSofa(ABC):
    @abstractmethod
    def __init__(self, author, size):
        pass

    @abstractmethod
    def rest(self) -> str:
        pass

    def print_data(self):
        self.rest()



class AbstractChair(ABC):
    @abstractmethod
    def __init__(self, author, size):
        pass

    @abstractmethod
    def sit(self) -> None:
        pass

    def print_data(self):
        self.sit()


class AbstractTable(ABC):
    @abstractmethod
    def __init__(self, author, size):
        pass

    @abstractmethod
    def dinner(self) -> str:
        pass

    @abstractmethod
    def kitchen_set(self, chair1: AbstractChair, chair2: AbstractChair) -> None:
        pass

    def print_data(self):
        self.dinner()


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_sofa(self, author, size) -> AbstractSofa:
        pass

    @abstractmethod
    def create_chair(self, author, size) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self, author, size) -> AbstractTable:
        pass


class AbstractGreetings(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def hello(self):
        pass


class AbstractFarewell(ABC):
    @abstractmethod
    def __init__(self, name):
        pass

    @abstractmethod
    def bye(self):
        pass


class AbstractMessagesFactory(ABC):
    @abstractmethod
    def create_greetings(self, name) -> AbstractGreetings:
        pass

    @abstractmethod
    def create_farewell(self, name) -> AbstractFarewell:
        pass

