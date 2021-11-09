from requests import get, utils


def get_content_url(url):
    """Give the decoded content in string from the marked url"""
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    return response.content.decode(encoding=encodings)


def currency_rates(url, currency):
    """Give the currency rate from marked url"""
    currencies = {}
    content = get_content_url(url)
    currency_code, currency_rate = content.split('CharCode'), content.split('Value')
    for i in range(1, len(currency_code), 2):
        currencies[currency_code[i][1:4]] = float(currency_rate[i][1:8].replace(',', '.'))
    return currencies.get(currency.upper())


print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'JpY'))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'USD'))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))
