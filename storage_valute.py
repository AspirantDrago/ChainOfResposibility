import logging
from abc import ABC, abstractmethod

from overrides import overrides

from banknote import Banknote, Valute
from command import Command, CommandTakeOff


class MissingBillError(ValueError):
    """
    Исключение, возникающее при отсутствии купюр в хранилище.
    """

    pass


class Handler(ABC):
    """
    Абстрактный класс обработчика команды.
    """

    def __init__(self):
        """
        Конструктор по-умолчанию для обработчика команды.
        """
        self._next_handler: 'Handler' | None = None

    def add_handler(self, handler: 'Handler') -> 'Handler':
        """
        Добавление следующего обработчика команды.

        :param handler: Следующий обработчик команды.
        :type handler: Handler
        :return: Следующий обработчик команды.
        :rtype: Handler
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, command: Command) -> None:
        """
        Абстрактный метод обработки команды.

        :param command: Команда.
        :type command: Command
        :return: None
        """
        pass


class StorageValute(Handler):
    '''
    Класс хранилища валюты.

    Дочерний класс от Handler
    '''

    def __init__(self, nominal: int, name: Valute, count: int = 0):
        '''
        Конструктор класса хранилища валюты

        :param nominal: Номинал купюр
        :type nominal: int
        :param name:    Тип валюты
        :type name:     Valute
        :param count:   Количество купюр
        :type count:    int
        '''
        super().__init__()
        self._nominal = nominal
        self._name = name
        self._storage = [Banknote(self._nominal, self._name) for _ in range(count)]

    @property
    def nominal(self) -> int:
        '''
        Номинал купюр
        '''
        return self._nominal

    @property
    def count(self) -> int:
        '''
        Количество купюр
        '''
        return len(self)

    def __len__(self) -> int:
        """
        Количество купюр в хранилище.
        """
        return len(self._storage)

    @overrides
    def handle(self, command: Command) -> None:
        """
        Обработка команды.

        :param command: Команда.
        :type command: Command
        :return: None
        """
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
        """
        Пополнение хранилища купюрами.

        :param value: Количество купюр.
        :type value: int
        :return: None
        """
        logging.info(f'Добавили {value} купюр номиналом {self._nominal} {self._name}')
        self._storage += [Banknote(self._nominal, self._name) for _ in range(value)]
