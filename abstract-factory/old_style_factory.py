from abstract_classes import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class OldStyleSofa(AbstractSofa):
    def __init__(self, author, size):
        self.folding = False
        self.author = author
        self.size = size

    def rest(self) -> str:
        print('Rest like a queen')


class OldStyleChair(AbstractChair):
    def __init__(self, author, size):
        self.legs = 4
        self.author = author
        self.size = size

    def sit(self):
        print('Sit like a count')


class OldStyleTable(AbstractTable):
    def __init__(self, author, size):
        self.shape = 'square'
        self.author = author
        self.size = size

    def dinner(self):
        print('Eat like a king')

    def kitchen_set(self, chair1: OldStyleChair, chair2: OldStyleChair):
        print(f'You have beautiful old style set with two chairs and table')


class OldStyleFactory(AbstractFurnitureFactory):

    def create_sofa(self, author, size) -> OldStyleSofa:
        return OldStyleSofa(author, size)

    def create_chair(self, author, size) -> OldStyleChair:
        return OldStyleChair(author, size)

    def create_table(self, author, size) -> OldStyleTable:
        return OldStyleTable(author, size)

