from abc import ABC

from .storage_valute import StorageValute
from .valute import Valute



class Bankomat(ABC):
    def __init__(self):
        self._chain_storages: StorageValute | None = None


class BankomatSber(Bankomat):
    def __init__(self):
        super().__init__()
        self._chain_storages = StorageValute(5000, Valute.RUB)\
            .add_handler(StorageValute(1000, Valute.RUB))\
            .add_handler(StorageValute(500, Valute.RUB))\
            .add_handler(StorageValute(200, Valute.RUB))\
            .add_handler(StorageValute(100, Valute.RUB))\
