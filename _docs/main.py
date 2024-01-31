import logging

from valute import Valute
from bankomat import BankomatSber

logging.basicConfig(level=logging.INFO)


bank = BankomatSber()
ok, arr = bank.take_valute(1400, Valute.RUB)
print(ok)
print(arr)
