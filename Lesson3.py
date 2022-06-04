'''1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
кратны каждому из чисел в диапазоне от 2 до 9.'''

result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 100):
        if f % n == 0:
            result[n].append(f)
    print(
        f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.'
        )

    '''2. Во втором массиве сохранить индексы чётных элементов первого
    массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то
    во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 -
    если индексация начинается с нуля), т.к. именно в этих позициях первого
    массива стоят чётные числа.'''

    import random

    r = [random.randint(0, 99) for _ in range(10)]
    print(f'Первый массив {r}')
    index_even = []

    for n in r:
        if n % 2 == 0:
            index_even.append(r.index(n))

    print(f'Индексы чётных элементов первого массива: {index_even}')

    '''3. В массиве случайных целых чисел поменять местами минимальный и
    максимальный элементы.'''

    import random

    r = [random.randint(0, 99) for _ in range(10)]
    print(f'Массив до изменения: {r}')

    max = r[0]
    min = r[0]

    for i in r:
        if i > max:
            max = i
        elif i < min:
            min = i
    min_index = r.index(min)
    max_index = r.index(max)
    r[min_index], r[max_index] = r[max_index], r[min_index]
    print(f'Массив осле изменения элементов {min_index} и {max_index}: {r}')

    '''4. Определить, какое число в массиве встречается чаще всего.'''

    import random

    r = [random.randint(0, 99) for _ in range(100)]
    print(f'Массив: {r}')

    max_index = 0
    for i in r:
        if r.count(max_index) < r.count(i):
            max_index = r.index(i)

    print(f'Число {r[max_index]}, встречается {r.count(max_index)} раза')