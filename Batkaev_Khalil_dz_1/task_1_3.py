number = 0
while number <= 234:
    if number % 10 == 1 and number != 11 and number % 100 != 11:
            print(number, 'процент')
    elif 2 <= number % 10 <= 4 and not 12 <= number <= 14 and not 12 <= number % 100 <= 14:
        print(number, 'процента')
    else:
        print(number, 'процентов')
    number += 1
