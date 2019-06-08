from .abstract_builder import AbstractPhoneBuilder


class IPhoneManualBuilder(AbstractPhoneBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._manual = ''

    @property
    def manual(self):
        manual = self._manual
        self.reset()
        return manual

    def add_cpu(self):
        self._manual += 'Apple A10 Fusion with 4 cores and with 2340 Gh frequency\n'

    def add_screen(self):
        self._manual += 'IPS LCD screen, 5.5", resolution: 1080x1920\n'

    def add_case(self):
        self._manual += 'Cool metal case\n'

    def add_camera(self):
        self._manual += 'High quality camera with 12mp and focus length 2.8\n'

    def add_front_camera(self):
        self._manual += 'High quality front camera with 7mp and focus length 2.2\n'

    def add_ram(self):
        self._manual += '3 GB RAM'

    def add_memory(self):
        self._manual += '32 GB space memory'

    def add_os(self):
        self._manual += 'IOS, version 10.0.1'
