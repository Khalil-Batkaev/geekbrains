duration = int(input('Введите число: '))
seconds = 1
minutes = seconds * 60
hours = minutes * 60
days = hours * 24

if duration < minutes:
    print(duration, 'сек')
elif minutes <= duration < hours:
    print(f'{duration // minutes} мин {duration % minutes} сек')
elif hours <= duration < days:
    print(f'{duration // hours} час {(duration % hours) // minutes} мин {duration % minutes} сек')
else:
    print(
        f'{duration // days} дн {(duration % days) // hours} час {(duration % hours) // minutes} '
        f'мин {duration % minutes} сек')