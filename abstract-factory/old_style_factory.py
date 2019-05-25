from abstract_classes.furniture import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class OldStyleSofa(AbstractSofa):
    def __init__(self, author: str, size: str) -> None:
        self.folding = False
        self.author = author
        self.size = size

    def stay(self) -> None:
        pass

    def rest(self) -> str:
        print('Rest like a queen')


class OldStyleChair(AbstractChair):
    def __init__(self, author: str, size: str) -> None:
        self.legs = 4
        self.author = author
        self.size = size

    def sit(self) -> None:
        print('Sit like a count')


class OldStyleTable(AbstractTable):
    def __init__(self, author: str, size: str) -> None:
        self.shape = 'square'
        self.author = author
        self.size = size

    def dinner(self) -> None:
        print('Eat like a king')

    def kitchen_set(self, chair1: OldStyleChair, chair2: OldStyleChair) -> None:
        print(f'You have beautiful old style set with two chairs and table')


class OldStyleFactory(AbstractFurnitureFactory):

    def create_sofa(self, author, size) -> AbstractSofa:
        return OldStyleSofa(author, size)

    def create_chair(self, author, size) -> AbstractChair:
        return OldStyleChair(author, size)

    def create_table(self, author, size) -> AbstractTable:
        return OldStyleTable(author, size)
