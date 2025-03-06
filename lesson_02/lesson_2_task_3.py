from math import ceil


def ceil_square(b):
    return ceil(b * b)


a = float(input('Введите значение длины стороны: '))

print(f'Округленная в большую сторону площадь - {ceil_square(a)}')
