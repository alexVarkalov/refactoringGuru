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
from phones.sony_phone import SonyPhone


class SonyPhoneBuilder(AbstractPhoneBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._phone = SonyPhone()

    @property
    def phone(self):
        phone = self._phone
        self.reset()
        return phone

    def add_cpu(self):
        self._phone.cpu = CPU('Qualcomm Snapdragon 835 MSM8998', 8, 2500)

    def add_screen(self):
        self._phone.screen = Screen(5.2, 1080, 1920, 'IPS')

    def add_case(self):
        self._phone.case = Case('metal')

    def add_camera(self):
        self._phone.camera = Camera(19, 2.0)

    def add_front_camera(self):
        self._phone.camera = SelfieCamera(13, 2.0)

    def add_ram(self):
        self._phone.ram = RAM(4)

    def add_memory(self):
        self._phone.memory = Memory(64)

    def add_os(self):
        self._phone.os = OS('Android', '8.0')
