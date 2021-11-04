from requests import get, utils
from datetime import date


def get_content_url(url):
    """Give the decoded content in string from the marked url"""
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    return response.content.decode(encoding=encodings)


def currency_rates(url, currency):
    """Give the currency rate from marked url"""
    currencies = {}
    currency_code, currency_rate = get_content_url(url).split('CharCode'), get_content_url(url).split('Value')
    id_rate = 1
    for i in range(1, len(currency_code), 2):
        for j in range(id_rate, len(currency_rate)):
            currencies[currency_code[i][1:4]] = float(currency_rate[j][1:8].replace(',', '.'))
            break
        id_rate += 2
    return currencies.get(currency.upper())


def currency_rates_adv(url, currency):
    """Give the date of value and the currency rate from marked url"""
    date_lst = get_content_url(url)
    day, month, year = date_lst[date_lst.find('Date="') + 6:date_lst.find('Date="') + 16].split('.')
    return [date(int(year), int(month), int(day))], currency_rates(url, currency)

if __name__ == '__main__':
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'JpY'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'USD'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))

    print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'gbP'))
    print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR'))
    print(currency_rates_adv('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))