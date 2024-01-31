from abc import ABC

from banknote import Banknote
from valute import Valute


class Command(ABC):
    """
    Абстрактный базовый класс для команд банкомата.
    """

    pass


class CommandTakeOff(Command):
    """
    Команда снятия денег с банкомата.
    """

    def __init__(self, value: int, name: Valute, bankomat: 'Bankomat'):
        """
        Конструктор команды снятия денег с банкомата.

        :param value: Сумма снятия
        :type value: int
        :param name: Тип валюты
        :type name: Valute
        :param bankomat: Банкомат
        :type bankomat: Bankomat
        """
        self._value = value
        self._original_value = value
        self._bankomat = bankomat
        self._name = name

    def append(self, banknote: Banknote) -> None:
        """
        Добавление банкноты в банкомат.

        :param banknote: Банкнота
        :type banknote: Banknote
        """
        self._value -= int(banknote)
        self._bankomat.append(banknote)

    @property
    def value(self) -> int:
        """
        Сумма снятия.
        """
        return self._value

    @property
    def name(self) -> Valute:
        """
        Тип валюты.
        """
        return self._name

    def __bool__(self) -> bool:
        """
        Требуется ли продолжать снятие денег.
        """
        return self.value > 0


class CommandTakeOn(Command):
    """
    Команда добавления денег в банкомат.
    """

    def __init__(self, bankomat: 'Bankomat'):
        """
        Конструктор команды добавления денег в банкомат.

        :param bankomat: Банкомат
        :type bankomat: Bankomat
        """
        self._bankomat = bankomat
