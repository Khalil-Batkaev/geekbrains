from sys import argv

if len(argv) <= 1:
    print('Введите сумму продаж')
else:
    command, sale_amount, *args = argv
    with open('bakery.csv', 'ta', encoding='utf-8') as f:
        f.write(f"{sale_amount} \n")
