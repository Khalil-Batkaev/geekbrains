class DateInitError(Exception):

    def __init__(self, date):
        self._date = date

    def __str__(self):
        return f'Неверно введены данные даты: {self._date}'


class Date:

    def __init__(self, date):
        if self.valid_date(date):
            self._day, self._month, self._year = self.valid_date(date)
        else:
            raise DateInitError(date)

    def __str__(self):
        return f'{self._year}.{self._month:02d}.{self._day:02d}'

    @classmethod
    def parsing_date(cls, date):
        if date.count('-') == 2:
            day, month, year = map(int, date.split('-'))
        else:
            raise ValueError(f'Разделитель должен быть "-", неверные данные - {date}')
        return day, month, year

    @staticmethod
    def valid_date(date):
        days_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        day, month, year = Date.parsing_date(date)
        if 1 <= month <= 12 and 1 <= day <= days_month[month] and len(str(year)) == 4:
            return day, month, year
        else:
            return None


try:
    date_1 = Date('20-01-2021')
    date_2 = Date('05-11-2021')
    print(date_1, date_2, sep='\n')
    date_wrong_1 = Date('20-15-2021')
    date_wrong_2 = Date('30-02-2021')
    date_wrong_3 = Date('20.05.2021')
except (DateInitError, ValueError) as e:
    print(e)
