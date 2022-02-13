x = int(input('a = '))
y = int(input('b = '))


def square_and_perimeter(a, b):
    return f'Площадь прямоугольника: {a * b} ' \
           f'\nПериметр прямоугольника: {2 * a + 2 * b}'


res = square_and_perimeter(x, y)
print(res)



