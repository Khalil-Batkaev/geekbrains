from sys import argv

if len(argv) <= 1:
    print('Введите номер позиции для замены и сумму продаж')
else:
    command, mark, sale_amount, *args = argv
    mark = int(mark)
    id_line = 0
    with open('bakery_adv.csv', 'r+', encoding='utf-8') as f:
        if mark == 1:
            f.seek(0)
            f.write(f"{sale_amount:<15} \n")
            exit(0)
        else:
            line = f.readline()
            while line:
                id_line += 1
                if mark - id_line == 1:
                    f.seek(0, 1)
                    f.write(f"{sale_amount:<15} \n")
                    exit(0)
                line = f.readline()
