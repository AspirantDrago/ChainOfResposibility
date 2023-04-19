from uuid import uuid4

from valute import Valute


class Banknote:
    '''
    класс Купюры
    '''

    def __init__(self, nominal: int, name: Valute):
        self._nominal = nominal
        self._name = name
        self._number = uuid4().int

    def __hash__(self) -> int:
        return self._number

    def __str__(self) -> str:
        return f'{self._nominal} {self._name}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._nominal}, {self._name})'

    def __int__(self) -> int:
        return self._nominal
