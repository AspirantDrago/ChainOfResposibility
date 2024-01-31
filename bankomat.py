from abc import ABC

from banknote import Banknote
from command import CommandTakeOff
from storage_valute import StorageValute
from valute import Valute

type Banknotes = list[Banknote]


class Bankomat(ABC):
    """
    Абстрактный базовый класс банкомата
    """

    def __init__(self):
        """
        Конструктор класса банкомата
        """
        self._chain_storages: StorageValute | None = None
        self._bill_acceptor: Banknotes = []

    def append(self, banknote: Banknote) -> None:
        """
        Метод добавления купюры в банкомат

        :param banknote: купюра
        :type banknote: Banknote
        :return: None
        """
        self._bill_acceptor.append(banknote)

    def take_valute(self, value: int, name: Valute) -> tuple[bool, Banknotes]:
        """
        Метод выдачи валюты

        :param value: желаемая сумма
        :type value: int
        :param name: тип валюты
        :type name: Valute
        :return: кортеж из двух элементов: результат операции и список купюр
        :rtype: tuple[bool, Banknotes]
        """
        if self._chain_storages is None:
            return False, []
        command = CommandTakeOff(value, name, self)
        self._chain_storages.handle(command)
        result = self._bill_acceptor
        self._bill_acceptor = []
        return not command, result


class BankomatSber(Bankomat):
    """
    Класс банкомата Сбербанка
    """

    def __init__(self):
        """
        Конструктор класса банкомата Сбербанка

        Пример банкомата, в котором уже есть купюры разных номиналов:

        - 1 купюра по 5000 рублей
        - 1 купюра по 1000 рублей
        - 5 купюр по 500 рублей
        - 1 купюра по 200 рублей
        - 5 купюр по 100 рублей
        """
        super().__init__()
        self._chain_storages = StorageValute(5000, Valute.RUB)
        self._chain_storages \
            .add_handler(StorageValute(1000, Valute.RUB)) \
            .add_handler(StorageValute(500, Valute.RUB, 5)) \
            .add_handler(StorageValute(200, Valute.RUB)) \
            .add_handler(StorageValute(100, Valute.RUB, 5))
