from sys import argv


def check_sale_amount(amount):
    """Check sale_amount for correct type."""
    is_valid = False
    if '.' in amount:
        part_1, part_2 = amount.split('.')
        if part_1.isdigit() and part_2.isdigit():
            is_valid = True
    elif amount.isdigit():
        is_valid = True
    else:
        print('Сумма продаж должна быть числом')
    return is_valid


if len(argv) <= 1:
    print('Введите сумму продаж')
else:
    command, sale_amount, *args = argv
    if check_sale_amount(sale_amount):
        with open('bakery.csv', 'ta', encoding='utf-8') as f:
            f.write(f"{sale_amount} \n")
