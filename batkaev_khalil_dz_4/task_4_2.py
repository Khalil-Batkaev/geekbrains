from requests import get, utils


def get_content_url(url):
    """Give the decoded content in string from the marked url"""
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    return response.content.decode(encoding=encodings)


def currency_rates(url, currency):
    """Give the currency rate from marked url"""
    currencies = {}
    currency_code, currency_rate = get_content_url(url).split('CharCode'), get_content_url(url).split('Value')
    id_rate = 0
    for _currency in currency_code:
        if _currency.isupper() and len(_currency) == 6:
            for i in range(id_rate, len(currency_rate)):
                if ',' in currency_rate[i]:
                    currencies[_currency[1:4]] = float(currency_rate[i][1:8].replace(',', '.'))
                    break
        id_rate += 1
    return currencies.get(currency.upper())


if __name__ == '__main__':
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'JpY'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'USD'))
    print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))
