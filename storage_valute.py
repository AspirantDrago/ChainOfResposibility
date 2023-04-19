from abc import ABC, abstractmethod
import logging

from command import Command, CommandTakeOff
from banknote import Banknote, Valute


class MissingBillError(ValueError):
    pass


class Handler(ABC):
    def __init__(self):
        self._next_handler: 'Handler' | None = None

    def add_handler(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, command: Command):
        pass


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

    def handle(self, command: Command) -> None:
        if isinstance(command, CommandTakeOff):
            command: CommandTakeOff = command
            if command.name == self._name:
                value = command.value // self._nominal
                value = min(value, len(self))
                logging.info(f'Сняли {value} купюр номиналом {self._nominal} {self._name}')
                if value:
                    for _ in range(value):
                        command.append(self._storage.pop())
        logging.debug(f'{bool(command)} {self._next_handler}')
        if command and self._next_handler is not None:
            self._next_handler.handle(command)




        # if value > len(self):
        #     raise MissingBillError(f'Недостаточно купюр номиналом {self._nominal} рублей. ' +
        #                            f'Требуется {value}, в наличии {self._count} купюр')
        # for _ in range(value):
        #     target.append(self._storage.pop())
        #

    def replenishment(self, value: int) -> None:
        logging.info(f'Добавили {value} купюр номиналом {self._nominal} {self._name}')
        self._storage += [Banknote(self._nominal, self._name) for _ in range(value)]
