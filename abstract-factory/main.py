import platform

from abstract_classes.messages import AbstractMessagesFactory
from abstract_classes.furniture import (
    AbstractFurniture,
    AbstractFurnitureFactory,
)
from linux_messages import LinuxMessagesFactory
from windows_messages import WindowsMessagesFactory
from old_style_factory import OldStyleFactory
from modern_factory import ModernFactory
from future_factory import FutureFactory

import sys


def get_furniture_factory(adjective) -> AbstractFurnitureFactory:
    if adjective == 'старый':
        furniture_factory = OldStyleFactory()
    elif adjective == 'современный':
        furniture_factory = ModernFactory()
    elif adjective == 'футуристичный':
        furniture_factory = FutureFactory()
    else:
        raise Exception('Wrong adjective')
    return furniture_factory


def get_product(factory: AbstractFurnitureFactory, noun) -> AbstractFurniture:
    if noun == 'диван':
        product = factory.create_sofa('Alex', 'mid')
    elif noun == 'стол':
        product = factory.create_table('Alex', 'mid')
    elif noun == 'стул':
        product = factory.create_chair('Alex', 'mid')
    else:
        raise Exception('Wrong noun')
    return product


def main(messages_factory: AbstractMessagesFactory) -> None:
    if len(sys.argv) != 4:
        raise Exception('Wrong amount of params, need three words')
    *_, adjective, noun = sys.argv
    # name = input('Input your name: ')
    name = 'Alex'
    greetings = messages_factory.create_greetings(name)
    greetings.hello()
    furniture_factory = get_furniture_factory(adjective)
    product = get_product(furniture_factory, noun)
    product.print_data()


if __name__ == "__main__":
    client_os = platform.system()
    if client_os == 'Linux':
        main(LinuxMessagesFactory())
    elif client_os == 'Windows':
        main(WindowsMessagesFactory())
    else:
        print('Your os is not supported')
