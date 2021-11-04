import sys
from utils import currency_rates


def currency_rates_cmd(argv, url='http://www.cbr.ru/scripts/XML_daily.asp'):
    """Give the currency rate from marked url"""
    program, currency, *args = argv
    if currency_rates(url, currency):
        print(currency.upper() + ':', currency_rates(url, currency))
    else:
        print(f'{currency.upper()}: Валюта не найдена')


currency_rates_cmd(sys.argv)
