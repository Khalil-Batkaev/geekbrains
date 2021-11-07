src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_numbers = set()
numbers_all = set()
for number in src:
    if number not in numbers_all:
        unique_numbers.add(number)
    else:
        unique_numbers.discard(number)
    numbers_all.add(number)
result = [number for number in src if number in unique_numbers]
print(src, result, sep='\n')
