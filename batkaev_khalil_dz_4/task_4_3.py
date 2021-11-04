from datetime import date
from utils import get_content_url, currency_rates


def currency_rates_adv(url, currency):
    """Give the date of value and the currency rate from marked url"""
    date_lst = get_content_url(url)
    day, month, year = date_lst[date_lst.find('Date="') + 6:date_lst.find('Date="') + 16].split('.')
    return [date(int(year), int(month), int(day))], currency_rates(url, currency)


print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'gbP'))
print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR'))
print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))
