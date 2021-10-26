prices = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 10.55, 2.15, 334.99, 2.25, 23.01]
print('Исходный список:', prices, sep='\n')
for price in prices:
  print(f'{int(price)} руб {round((price - int(price)) * 100):02d} коп', end=', ')
print()
print('Доказательство операции in place:')
print(f'id перед сортировкой {id(prices)}')
prices.sort()
print(*prices)
print(f'id после сортировки {id(prices)}')
prices_new = prices.copy()
prices_new.sort(reverse = True)
print('5 самых дорогих товаров:', *prices_new[0:5], sep='\n')
