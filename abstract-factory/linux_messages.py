from abstract_messages import (
    AbstractMessagesFactory,
    AbstractGreetings,
    AbstractFarewell,
)


class LinuxGreetings(AbstractGreetings):
    def __init__(self, name:str) -> None:
        self.name = name

    def hello(self) -> None:
        print(f'Hello dear {self.name}, we have special discount for you')


class LinuxFarewell(AbstractFarewell):
    def __init__(self, name:str) -> None:
        self.name = name

    def bye(self) -> None:
        print(f'See you later {self.name}, hope that you found everything that you had been needed')


class LinuxMessagesFactory(AbstractMessagesFactory):
    def create_greetings(self, name:str) -> AbstractGreetings:
        return LinuxGreetings(name)

    def create_farewell(self, name:str) -> AbstractFarewell:
        return LinuxFarewell(name)
