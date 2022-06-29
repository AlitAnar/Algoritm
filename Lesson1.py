'''1. Найти сумму и произведение цифр трехзначного числа,
    которое вводит пользователь.'''

number = input('Введите число: ')

sum = 0
prod = 1

for f in number:
    sum += int(f)
    prod *= int(f)
print(f"Сумма цифр числа {number}: {sum}")
print(f"Произведение цифр: {number}: {prod}")

'''2. Выполнить логические побитовые операции «И», «ИЛИ» и др.
над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на
два знака. Объяснить полученный результат.'''

n1 = 5
n2 = 6

'''"ИЛИ" оператор копирует бит, если тот присутствует в хотя бы в одном
операнде.'''
bit_or = n1 | n2

'''"Исключительное ИЛИ" оператор копирует бит только если бит присутствует
в одном из операндов, но не в обоих сразу.'''
bit_xor = n1 ^ n2

'''"И" оператор, копирует бит в результат только если бит присутствует
в обоих операндах.'''
bit_and = n1 & n2

'''Побитовое отрицание меняет биты на обратные, там где была единица
становиться ноль и наоборот.'''
bit_not_n1 = ~n1
bit_not_n2 = ~n2

'''Побитовый сдвиг вправо. Значение левого операнда "сдвигается" вправо
на количество бит указанных в правом операнде.'''
bit_shift_right = n1 >> 2

'''Побитовый сдвиг влево. Значение левого операнда "сдвигается" влево
на количество бит указанных в правом операнде.'''
bit_shift_left = n1 << 2

print(f"""Побитовое «ИЛИ» (OR) для {bin(n1)} и {bin(n2)}: \
{bin(bit_or)} ({bit_or})""")

print(f"""Исключающее «ИЛИ» (XOR) для {bin(n1)} и {bin(n2)}: \
{bin(bit_xor)} ({bit_xor})""")

print(f"""Побитовое «И» (AND) для {bin(n1)} и {bin(n2)}: \
{bin(bit_and)} ({bit_and})""")

print(f"""Побитовое отрицание (NOT) для {bin(n1)}: \
{bin(bit_not_n1)} ({bit_not_n1}) и для {bin(n2)}: \
{bin(bit_not_n2)} ({bit_not_n2})""")

print(f"""Битовый сдвиг вправо для {bin(n1)}: \
{bin(bit_shift_right)} ({bit_shift_right})""")

print(f"""Битовый сдвиг влево для {bin(n1)}: \
{bin(bit_shift_left)} ({bit_shift_left})""")

'''3. По введенным пользователем координатам двух точек вывести уравнение
прямой вида y=kx+b, проходящей через эти точки.'''

x1, y1, x2, y2 = [
    int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split()
]

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'Уравнение прямой: y = {k}x + {b}')

'''4. Написать программу, которая генерирует в указанных
пользователем границах: случайное целое число; случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти
символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
включительно.'''

from os import urandom as _urandom


def random(list):
    '''Функция возвращает случайный элемент из списка.
    Случайное число возвращает функция _urandom из генератора псевдослучайных
    чисел операционной системы. Побитовый сдвиг вправо увеличивает энтропию'''
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    maxsize = len(list)
    i = random % maxsize
    return list[i]


def frange(start, stop, jump):
    '''Функция генерирует диапазон вещественных чисел
    start_float, stop_float, jump_float --> float'''
    while start < stop:
        yield start
        start += jump


print('Введите диапазон. Диапазон целых чисел \
(type_range = int start_int end_int jump_int). \
Или диапазон вещественных чисел \
(type_range = float start_float end_float jump_float). \
Или диапазон символов \
(type_range = str tart_str end_str jump_int) ')

type_range, raw_start, raw_end, raw_jump = [
    x for x in input('Введите диапазон: type_range start end jump: ').split()
]

if type_range == 'int':
    start = int(raw_start)
    stop = int(raw_end)
    jump = int(raw_jump)
    list_int = [x for x in range(start, stop + 1, jump)]
    print(list_int)
    print(
        f'Случайное целое число из диапазона {start} - {stop}: \
    {random(list_int)}'
    )

elif type_range == 'float':
    start = float(raw_start)
    stop = float(raw_end)
    jump = float(raw_jump)
    list_float = [x for x in frange(start, stop + jump, jump)]
    print(list_float)
    print(
        f'Случайное вещественное число из диапазона {start} - {stop}: \
    {random(list_float)}'
        )

elif type_range == 'str':
    start = raw_start
    stop = raw_end
    jump = int(raw_jump)
    list_abc = [chr(i) for i in range(ord(start), ord(stop) + 1, jump)]
    print(list_abc)
    print(f'Случайный символ из из диапазона {start} - {stop}: \
    {random(list_abc)}')

else:
    print('Неправильно задан диапазон')