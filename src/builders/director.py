from .abstract_builder import AbstractPhoneBuilder


class Director:
    def __init__(self, builder: AbstractPhoneBuilder):
        self._builder = builder

    @property
    def builder(self):
        return self._builder

    def build_cheep_phone(self):
        self._builder.add_cpu()
        self._builder.add_screen()
        self._builder.add_case()
        self._builder.add_ram()
        self._builder.add_memory()
        self._builder.add_os()

    def build_expensive_phone(self):
        self._builder.add_cpu()
        self._builder.add_screen()
        self._builder.add_case()
        self._builder.add_camera()
        self._builder.add_front_camera()
        self._builder.add_ram()
        self._builder.add_memory()
        self._builder.add_os()
