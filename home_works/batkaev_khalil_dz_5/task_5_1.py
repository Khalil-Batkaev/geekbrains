def iterator_without_yield(n):
    return (number for number in range(1, n + 1, 2) if number ** 2 < 200)


gen_1 = iterator_without_yield(10)

while gen_1:
    print(next(gen_1))
