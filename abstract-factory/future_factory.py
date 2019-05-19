from abstract_classes import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class FutureSofa(AbstractSofa):
    def __init__(self, author, size):
        self.folding = True
        self.author = author
        self.size = size

    def rest(self) -> str:
        print('Choose your dreams')


class FutureChair(AbstractChair):
    def __init__(self, author, size):
        self.legs = 0
        self.author = author
        self.size = size

    def sit(self):
        print('No legs, no gravity')


class FutureTable(AbstractTable):
    def __init__(self, author, size):
        self.shape = 'tesseract'
        self.author = author
        self.size = size

    def dinner(self):
        print('Eat like an astronaut')

    def kitchen_set(self, chair1: FutureChair, chair2: FutureChair):
        print(f'You have imposable tesseract table and two levitated chairы')


class FutureFactory(AbstractFurnitureFactory):

    def create_sofa(self, author, size) -> FutureSofa:
        return FutureSofa(author, size)

    def create_chair(self, author, size) -> FutureChair:
        return FutureChair(author, size)

    def create_table(self, author, size) -> FutureTable:
        return FutureTable(author, size)

