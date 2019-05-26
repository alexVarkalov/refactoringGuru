from abc import ABC


class Component(ABC):
    pass


class CPU(Component):
    def __init__(self, model, cores, frequency):
        self.model = model
        self.cores = cores
        self.frequency = frequency


class Screen(Component):
    def __init__(self, size, resolution_x, resolution_y, technology):
        self.size = size
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y
        self.technology = technology


class Case(Component):
    def __init__(self, material):
        self.material = material


class Camera(Component):
    def __init__(self, mp, focus):
        self.mp = mp
        self.focus = focus


class SelfieCamera(Camera):
    pass


class RAM(Component):
    def __init__(self, size):
        self.size = size


class Memory(Component):
    def __init__(self, space):
        self.space = space


class OS(Component):
    def __init__(self, os, version):
        self.os = os
        self.version = version
