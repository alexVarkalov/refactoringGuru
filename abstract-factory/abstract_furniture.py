from abc import ABC, abstractmethod


class AbstractFurniture(ABC):
    pass


class AbstractSofa(AbstractFurniture):
    @abstractmethod
    def __init__(self, author: str, size: str) -> None:
        pass

    @abstractmethod
    def rest(self) -> None:
        pass

    def print_data(self) -> None:
        self.rest()


class AbstractChair(AbstractFurniture):
    @abstractmethod
    def __init__(self, author: str, size: str) -> None:
        pass

    @abstractmethod
    def sit(self) -> None:
        pass

    def print_data(self) -> None:
        self.sit()


class AbstractTable(AbstractFurniture):
    @abstractmethod
    def __init__(self, author: str, size: str) -> None:
        pass

    @abstractmethod
    def dinner(self) -> None:
        pass

    @abstractmethod
    def kitchen_set(self, chair1: AbstractChair, chair2: AbstractChair) -> None:
        pass

    def print_data(self) -> None:
        self.dinner()


class AbstractFurnitureFactory(ABC):
    @abstractmethod
    def create_sofa(self, author: str, size: str) -> AbstractSofa:
        pass

    @abstractmethod
    def create_chair(self, author: str, size: str) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self, author: str, size: str) -> AbstractTable:
        pass
