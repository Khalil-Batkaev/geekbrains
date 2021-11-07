def iterator_with_yield(n):
    result = 0
    for number in range(1, n + 1, 2):
        if number ** 2 < 200:
            result += number
            yield number, result


gen_2 = iterator_with_yield(10)

while gen_2:
    print(next(gen_2))
