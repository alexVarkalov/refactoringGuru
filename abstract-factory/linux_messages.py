from abstract_classes import (
    AbstractMessagesFactory,
    AbstractGreetings,
    AbstractFarewell,
)


class LinuxGreetings(AbstractGreetings):
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello dear {self.name}, we have special discount for you')

class LinuxFarewell(AbstractFarewell):
    def __init__(self, name):
        self.name = name

    def bye(self):
        print(f'See you later {self.name}, hope that you found everything that you had been needed')


class LinuxMessagesFactory(AbstractMessagesFactory):

    def create_greetings(self, name) -> LinuxGreetings:
        return LinuxGreetings(name)

    def create_farewell(self, name) -> LinuxFarewell:
        return LinuxFarewell(name)
