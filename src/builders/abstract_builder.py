from abc import (
    ABC,
    abstractmethod,
)


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
