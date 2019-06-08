from styles_factories.abstract_furniture import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class FutureSofa(AbstractSofa):
    def __init__(self, author: str, size: int) -> None:
        self.folding = True
        self.author = author
        self.size = size

    def rest(self) -> None:
        print('Choose your dreams')


class FutureChair(AbstractChair):
    def __init__(self, author: str, size: int) -> None:
        self.legs = 0
        self.author = author
        self.size = size

    def sit(self) -> None:
        print('No legs, no gravity')


class FutureTable(AbstractTable):
    def __init__(self, author: str, size: int) -> None:
        self.shape = 'tesseract'
        self.author = author
        self.size = size

    def dinner(self) -> None:
        print('Eat like an astronaut')

    def kitchen_set(self, chair1: FutureChair, chair2: FutureChair) -> None:
        print(f'You have imposable tesseract table and two levitated chairы')


class FutureFactory(AbstractFurnitureFactory):

    def create_sofa(self, author: str, size: int) -> FutureSofa:
        return FutureSofa(author, size)

    def create_chair(self, author: str, size: int) -> FutureChair:
        return FutureChair(author, size)

    def create_table(self, author: str, size: int) -> FutureTable:
        return FutureTable(author, size)

