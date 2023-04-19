from abc import ABC

from banknote import Banknote
from valute import Valute


class Command(ABC):
    pass


class CommandTakeOff(Command):

    def __init__(self, value: int, name: Valute, bankomat: 'Bankomat'):
        self._value = value
        self._original_value = value
        self._bankomat = bankomat
        self._name = name

    def append(self, banknote: Banknote) -> None:
        self._value -= int(banknote)
        self._bankomat.append(banknote)

    @property
    def value(self) -> int:
        return self._value

    @property
    def name(self) -> Valute:
        return self._name

    def __bool__(self) -> bool:
        return self.value > 0


class CommandTakeOn(Command):
    def __init__(self, bankomat: 'Bankomat'):
        self._bankomat = bankomat

    def __iter__(self) -> 'CommandTakeOn':
        return self

    def __next__(self):
        pass
