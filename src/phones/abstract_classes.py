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
