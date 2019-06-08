from .abstract_builder import AbstractPhoneBuilder
from phones.components import (
    Camera,
    CPU,
    Screen,
    Case,
    SelfieCamera,
    RAM,
    Memory,
    OS,
)
from phones.i_phone import IPhone


class IPhoneBuilder(AbstractPhoneBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._phone = IPhone()

    @property
    def phone(self):
        phone = self._phone
        self.reset()
        return phone

    def add_cpu(self):
        self._phone.cpu = CPU('Apple A10 Fusion', 4, 2340)

    def add_screen(self):
        self._phone.screen = Screen(5.5, 1080, 1920, 'IPS LCD')

    def add_case(self):
        self._phone.case = Case('metal')

    def add_camera(self):
        self._phone.camera = Camera(12, 2.8)

    def add_front_camera(self):
        self._phone.camera = SelfieCamera(7, 2.2)

    def add_ram(self):
        self._phone.ram = RAM(3)

    def add_memory(self):
        self._phone.memory = Memory(32)

    def add_os(self):
        self._phone.os = OS('IOS', '10.0.1')
