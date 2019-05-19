from abstract_classes import (
    AbstractFurnitureFactory,
    AbstractSofa,
    AbstractTable,
    AbstractChair,
)


class ModernSofa(AbstractSofa):
    def __init__(self, author, size):
        self.folding = True
        self.author = author
        self.size = size

    def rest(self) -> str:
        print('From Friends series')


class ModernChair(AbstractChair):
    def __init__(self, author, size):
        self.legs = 1
        self.author = author
        self.size = size

    def sit(self):
        print('Sit and drink your bear')


class ModernTable(AbstractTable):
    def __init__(self, author, size):
        self.shape = 'circle'
        self.author = author
        self.size = size

    def dinner(self):
        print('Nachos and spicy wings')

    def kitchen_set(self, chair1: ModernChair, chair2: ModernChair):
        print(f'You have simple table and two bar chairs')


class ModernFactory(AbstractFurnitureFactory):

    def create_sofa(self, author, size) -> ModernSofa:
        return ModernSofa(author, size)

    def create_chair(self, author, size) -> ModernChair:
        return ModernChair(author, size)

    def create_table(self, author, size) -> ModernTable:
        return ModernTable(author, size)

