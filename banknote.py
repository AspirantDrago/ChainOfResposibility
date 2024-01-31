from uuid import uuid4

from valute import Valute


class Banknote:
    """
    Класс Купюры
    """

    def __init__(self, nominal: int, name: Valute):
        """
        Инициализатор объекта купюры

        :param nominal: Номинал купюры
        :type nominal: int
        :param name: Валюта
        :type name: Valute
        """
        self._nominal = nominal
        self._name = name
        self._number = uuid4().int

    def __hash__(self) -> int:
        """
        Вычисление хэша банкноты
        """
        return self._number

    def __str__(self) -> str:
        """
        Строковое представление банкноты.

        >>> from valute import Valute
        >>> print(Banknote(100, Valute.RUB))
        100 рубль
        """
        return f'{self._nominal} {self._name}'

    def __repr__(self) -> str:
        """
        Представление банкноты в виде строки для внутреннего использования.

        >>> from valute import Valute
        >>> print(repr(Banknote(100, Valute.RUB)))
        Banknote(100, Valute.RUB)
        """
        return f'{self.__class__.__name__}({self._nominal}, {self._name.__class__.__name__}.{self._name.name})'

    def __int__(self) -> int:
        """
        Приведение к типу int.
        Возвращает номинал купюры.
        """
        return self._nominal
