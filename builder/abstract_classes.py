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
    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_screen(self):
        pass

    @abstractmethod
    def add_case(self):
        pass

    @abstractmethod
    def add_camera(self):
        pass

    @abstractmethod
    def add_front_camera(self):
        pass

    @abstractmethod
    def add_ram(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_os(self):
        pass
