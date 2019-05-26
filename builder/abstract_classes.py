from abc import ABC, abstractmethod


class AbstractPhone(ABC):
    def __init__(self):
        self.cpu = None
        self.screen = None
        self.case = None
        self.camera = None
        self.ram = None
        self.space = None
        self.os = None


class AbstractPhoneBuilder(ABC):
    @property
    @abstractmethod
    def phone(self):
        pass

    def add_cpu(self):
        pass

    def add_screen(self):
        pass

    def add_case(self):
        pass

    def add_camera(self):
        pass

    def add_front_camera(self):
        pass

    def add_ram(self):
        pass

    def add_memory(self):
        pass

    def add_os(self):
        pass
