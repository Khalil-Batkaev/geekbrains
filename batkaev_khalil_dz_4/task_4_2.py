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
    id_rate = 1
    for i in range(1, len(currency_code), 2):
        for j in range(id_rate, len(currency_rate)):
            currencies[currency_code[i][1:4]] = float(currency_rate[j][1:8].replace(',', '.'))
            break
        id_rate += 2
    return currencies.get(currency.upper())


print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'JpY'))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'USD'))
print(currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', 'XXX'))
