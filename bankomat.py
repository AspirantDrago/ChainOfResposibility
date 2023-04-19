from abc import ABC

from banknote import Banknote
from command import CommandTakeOff
from storage_valute import StorageValute
from valute import Valute



class Bankomat(ABC):
    def __init__(self):
        self._chain_storages: StorageValute | None = None
        self._bill_acceptor: list[Valute] = []

    def append(self, banknote: Banknote):
        self._bill_acceptor.append(banknote)

    def take_valute(self, value: int, name: str) -> tuple[bool, list[Valute]]:
        if self._chain_storages is None:
            return False, []
        command = CommandTakeOff(value, name, self)
        self._chain_storages.handle(command)
        result = self._bill_acceptor
        self._bill_acceptor = []
        return not command, result

class BankomatSber(Bankomat):
    def __init__(self):
        super().__init__()
        self._chain_storages = StorageValute(5000, Valute.RUB)
        self._chain_storages\
            .add_handler(StorageValute(1000, Valute.RUB))\
            .add_handler(StorageValute(500, Valute.RUB, 5))\
            .add_handler(StorageValute(200, Valute.RUB))\
            .add_handler(StorageValute(100, Valute.RUB, 5))\
