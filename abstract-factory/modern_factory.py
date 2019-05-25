from abstract_classes.furniture import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class ModernSofa(AbstractSofa):
    def __init__(self, author: str, size: str) -> None:
        self.folding = True
        self.author = author
        self.size = size

    def rest(self) -> None:
        print('From Friends series')


class ModernChair(AbstractChair):
    def __init__(self, author: str, size: str) -> None:
        self.legs = 1
        self.author = author
        self.size = size

    def sit(self) -> None:
        print('Sit and drink your bear')


class ModernTable(AbstractTable):
    def __init__(self, author: str, size: str) -> None:
        self.shape = 'circle'
        self.author = author
        self.size = size

    def dinner(self) -> None:
        print('Nachos and spicy wings')

    def kitchen_set(self, chair1: ModernChair, chair2: ModernChair) -> None:
        print(f'You have simple table and two bar chairs')


class ModernFactory(AbstractFurnitureFactory):

    def create_sofa(self, author, size) -> AbstractSofa:
        return ModernSofa(author, size)

    def create_chair(self, author, size) -> AbstractChair:
        return ModernChair(author, size)

    def create_table(self, author, size) -> AbstractTable:
        return ModernTable(author, size)
