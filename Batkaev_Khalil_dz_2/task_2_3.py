workers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i, _ in enumerate(workers):
    print(f"Привет, {workers[i][workers[i].rfind(' ') + 1:].title()}!")
