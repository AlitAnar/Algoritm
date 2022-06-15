# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()

import hashlib


def substring_count(input_string):
    """
    функция принимает на вход строку состоящую только из маленьких латинских букв
    функция возвращает количество различных подстрок с использованием хеш-функции
    """

    input_string = str(input_string).lower()

    length = len(input_string)

    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


some_string = 'hello'

print(f'Количество различных подстрок в строке {some_string}: {substring_count(some_string)}')

# 2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(input_string):
    counter = Counter(input_string)

    deq = deque(sorted(counter.items(), key=lambda x: x[1]))

    while len(deq) > 1:

        weight = deq[0][1] + deq[1][1]
        node = MyNode(left=deq.popleft()[0], right=deq.popleft()[0])

        for index, item in enumerate(deq):
            if weight > item[1]:
                continue
            else:
                deq.insert(index, (node, weight))
                break
        else:
            deq.append((node, weight))

    return deq[0][0]


def encode_tree(tree, encode_table, path=''):
    if not isinstance(tree, MyNode):
        encode_table[tree] = path
    else:
        encode_tree(tree=tree.left,  encode_table=encode_table, path=f'{path}0')
        encode_tree(tree=tree.right, encode_table=encode_table, path=f'{path}1')


some_string = 'beep boop beer!'
encode_dict = dict()
encode_tree(huffman_tree(some_string), encode_dict)

encoded_list = []

for element in some_string:
    encoded_list.append(encode_dict[element])

encoded_string = ''.join(encoded_list)

print(f'Оригинальная строка:   {some_string}')
print(f'Закодированная строка: {encoded_string}')