from math import ceil

def ceil_square(a, b):
    return ceil(a * b)


a = float(input('Введите первое значение: '))
b = float(input('Введите второе значение: '))

print(f'Округленная в большую сторону сумма - {ceil_square(a, b)}')