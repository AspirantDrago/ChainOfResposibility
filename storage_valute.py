from .banknote import Banknote, Valute
import logging


class MissingBillError(ValueError):
    pass


class Handler:
    def __init__(self):
        self._next_handler: 'Handler' | None = None

    def add_handler(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler


class StorageValute(Handler):
    '''
    Класс хранилища валюты
    '''

    def __init__(self, nominal: int, name: Valute, count: int = 0):
        '''
        Конструктор класса хранилища валюты
        :param nominal: Номинал купюр
        :param name:    Название Валюты
        :param count:   Количество купюр
        '''
        super().__init__()
        self._nominal = nominal
        self._name = name
        self._storage = [Banknote(self._nominal, self._name) for _ in range(count)]
        self._next_storage_valute: 'StorageValute' | None = None

    @property
    def nominal(self) -> int:
        '''
        :return: Номинал купюр
        '''
        return self._nominal

    @property
    def count(self) -> int:
        '''
        :return: Количество купюр
        '''
        return len(self)

    def __len__(self) -> int:
        return len(self._storage)

    def take_off(self, value: int, target) -> None:
        if value > len(self):
            raise MissingBillError(f'Недостаточно купюр номиналом {self._nominal} рублей. ' +
                                   f'Требуется {value}, в наличии {self._count} купюр')
        for _ in range(value):
            target.append(self._storage.pop())
        logging.info(f'Сняли {value} купюр номиналом {self._nominal} {self._name}')

    def replenishment(self, value: int) -> None:
        logging.info(f'Добавили {value} купюр номиналом {self._nominal} {self._name}')
        self._storage += [Banknote(self._nominal, self._name) for _ in range(value)]
