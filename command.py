from abc import ABC

from .valute import Valute


class Command(ABC):
    pass


class CommandTakeOff(Command):
    def __init__(self, value: int, name: Valute, bankomat):
        self.value = value
        self._original_value = value
        self._bankomat = bankomat
        self._name = name

    def append(self, obj) -> None:
        self._bankomat.append(obj)
    